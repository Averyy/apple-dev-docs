# Supporting key requests and key exchange requests

**Framework**: Authentication Services

Support the Platform SSO 2.0 protocol for encryption and decryption operations.

#### Overview

Key requests and key exchange requests require the SSO extension and the server to support the Platform SSO 2.0 protocol. To do so, the server needs to fully support requests, shared device keys, and the modified flows for registration, login, and unlock.

These requests are similar to login requests. They start with a server nonce request, sign the JSON Web Token (JWT) using the device signing key, and require an encrypted response that uses the device encryption key.

##### Request the Key

The system uses a key request to ask the server to provision an `EC256` key for the supplied purpose. The server needs to issue a public key in a certificate so that normal keychain operations can find it and use the key. In macOS, encryption operations for login and unlock use the public key. The server can also return a context that’s stored with the key and sent with all key exchange requests. The use of the context isn’t required, but the server can encrypt it to store key material for the key, for example, to rotate encryption values. Storage of the context doesn’t include additional encryption.

After user registration completes, macOS sends the key request. However, macOS can also send the request if it detects a problem or if it needs to rotate the keys.

The following flowchart provides a high-level overview of the key request flow:

![A flowchart shows a Device icon and Identity provider icon at the top of a looping process that starts with requesting and receiving a server nonce value and then JSON Object Signing and Encryption (JOSE) key request, followed by decrypting and validating the key response, saving the key and key context, and binding the key to the user account. ](https://docs-assets.developer.apple.com/published/4cb86b9083b10065750ae5b107991c14/media-4294341%402x.png)

The request is a JSON Object Signing and Encryption object (JOSE) that’s formatted per RFC 7519 and signed with the `DeviceSigningKey` and `ES256` per RFC 7515.

The following table specifies the header parameters for a key request:

| Key | Value | Notes |
| --- | --- | --- |
| `typ` | `platformsso-key-request+jwt` | Required. |
| `alg` | `ES256` | Required. The signing algorithm, only `ES256` is supported. |
| `kid` | The base-64 encoded SHA256 hash of the ANSI X9.63 formatted public key for the signing key | Required. |
| `x5c` | The base-64 encoded device signing certificate from [`saveCertificate(_:keyType:)`](asauthorizationproviderextensionloginmanager/savecertificate(_:keytype:).md) | Optional: The value is base-64 encoded per RFC 7517. |
| [`setCustomKeyRequestHeaderClaims(_:)`](asauthorizationproviderextensionloginconfiguration/setcustomkeyrequestheaderclaims(_:).md) |  |  |

The following table specifies the body parameters for a key request:

| Key | Value | Notes |
| --- | --- | --- |
| `version` | 1.0 | Required. |
| `request_type` | key_request | Required. |
| `key_purpose` | user_unlock | Required. |
| `aud` | [`audience`](asauthorizationproviderextensionloginconfiguration/audience.md) | Required. The identity provider (IdP) needs to verify this value to ensure that the assertion was created for them. |
| `iss` | [`clientID`](asauthorizationproviderextensionloginconfiguration/clientid.md) | Required. Per RFC 7523 Section 3. |
| `iat` | The current time | Required. The IdP needs to verify this value. |
| `exp` | 5 minutes from now | Required. The IdP needs to verify this value. |
| `nonce` | A nonce value | Required. A unique nonce value for this request. |
| [`serverNonceClaimName`](asauthorizationproviderextensionloginconfiguration/servernonceclaimname.md) or `request_nonce` | The value returned from the nonce request | Required. The key name is either the [`serverNonceClaimName`](asauthorizationproviderextensionloginconfiguration/servernonceclaimname.md) or the default value `request_nonce`. |
| `username` | [`loginUserName`](asauthorizationproviderextensionuserloginconfiguration/loginusername.md) | Required. The login user name. If not set, the system uses the local account name. |
| `sub` | [`loginUserName`](asauthorizationproviderextensionuserloginconfiguration/loginusername.md) | Required. Per RFC 7523 Section 3. |
| `refresh_token` | The current refresh token | Required. |
| `loginConfiguration.customKeyRequestBodyClaims` |  | Optional. If present, adds the key value pairs to the assertion. |

The following code provides an example of a key request:

```javascript
{
    "kid" : "6cgzt+gMK7vzj4iXhQj4AA4lyJUQ4ZVA/wTnA2kaYcg=",
    "x5c" : "MIIBg...Mhw==",
    "typ" : "platformsso-key-request+jwt",
    "alg" : "ES256"
}.{
    "jwe_crypto" : {
        "alg" : "ECDH-ES",
        "enc" : "A256GCM",
        "apv" : "AAAAB...TNGMQ"
    },
    "exp" : 1685756137,
    "request_type" : "key_request",
    "nonce" : "EA7D38B1-B9EA-444B-9141-97FFE7D0E3F1",
    "version" : "1.0",
    "request_nonce" : "AwABA...YQgAA",
    "refresh_token" : "abcd1234",
    "iss" : "aaff1524-fa35-40c5-94e3-2b233c5f2965",
    "key_purpose" : "user_unlock",
    "sub" : "foo",
    "username" : "foo",
    "iat" : 1685755837
}.[Signature]
```

The key network request is an HTTP POST to the [`keyEndpointURL`](asauthorizationproviderextensionloginconfiguration/keyendpointurl.md) that’s formatted per RFC 7523 and includes the following parameters:

| Key | Value | Notes |
| --- | --- | --- |
| `platform_sso_version` | `2.0` | Required. The version of the login protocol. |
| `grant_type` | `urn:ietf:params:oauth:grant-type:jwt-bearer` | Required. The assertion type. |
| [`customRequestJWTParameterName`](asauthorizationproviderextensionloginconfiguration/customrequestjwtparametername.md) or assertion | The base-64 URL encoded signed key request | Required. |
| [`customKeyRequestValues`](asauthorizationproviderextensionloginconfiguration/customkeyrequestvalues.md) |  | Optional. If present, adds the key value pairs to the key request. |

The following code provides an example of a key network request:

```http
POST /oauth2/token HTTP/1.1
Host: auth.example.com
Accept: application/platformsso-key-response+jwt
Content-Type: application/x-www-form-urlencoded
client-request-id: DCAB01D3-B1FE-4E1C-802F-B3EBDCDF9E67
platform_sso_version2.0&grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer&assertion=ewogI...HGuQg
```

##### Create the Key Response Json Web Encryption Jwe

The response is a JWE that’s decrypted according to RFC 7516 Section 5.2 with JWE Compact Serialization.

The JWE key response header contains the following values:

| Key | Value | Notes |
| --- | --- | --- |
| `typ` | `platformsso-key-response+jwt` | Required. |
| `enc` | `A256GCM` | Required. The supported encryption algorithm per RFC 7518 Section 4.6. |
| `alg` | `ECDH-ES` | Required: The supported key agreement algorithm per RFC 7518 Section 5.3. |
| `epk` | The ephemeral public key for the key exchange | Required. Per RFC 7518 Section 4.6.1.1, formatted per RFC 7517. |
| `kid` | The `kid` of the ephemeral public key | Optional. |
| `apu` | The base-64 URL encoded `PartyUInfo` for Concat KDF | Required. Per RFC 7518 Section 4.6.1.2. |
| `apv` | The base-64 URL encoded `PartyVInfo` for Concat KDF | Optional. Per RFC 7518 Section 4.6.1.3, the client uses the value from the request. |

The following code provides an example of a key response JWE header:

```javascript
{
    "enc" : "A256GCM",
    "kid" : "8fWc60nKm8I07JE3yG+xf9Kb61wUNrjWnVBV9zIB5mQ=",
    "epk" : {
        "y" : "SwUUA5FVmbe5K8OZ7ElRH5_qB8Z9klZyiGVvrTMyn8A",
        "x" : "o7YsVVlHr5VrMLFX6rqT5MQkNip9_GgYAnm8nQYIrVQ",
        "kty" : "EC",
        "crv" : "P-256"
    }, 
    "apu" : "AAAAB...zMp_A",
    "typ" : "platformsso-key-response+jwt",
    "alg" : "ECDH-ES"
}
```

The JWE key response body contains the following values:

| Key | Value | Notes |
| --- | --- | --- |
| `certificate` | The base-64 URL encoded certificate that contains the provisioned public key | Required. |
| `exp` | 5 minutes from now | Required. Per RFC 7523 Section 3. |
| `iat` | The current time | Required. Per RFC 7523 Section 3. |
| `key_context` | The key context for the key | Optional. |

The following code provides an example of a key response JWE body:

```javascript
{
    "certificate" : "MIIBc...2dGpb",
    "exp" : 1685756137,
    "iat" : 1685755837,
    "key_context" : "BHmTq...scA=="
}
```

##### Request the Key Exchange

The system uses the key exchange request when using the keys to decrypt data. Typically there are two or three requests occuring at the same time, depending on the number of decryption calls and required checks. These calls need to return quickly because the user is waiting for them to complete.

The following graph provides a high-level overview of the key exchange flow:

![A flowchart shows a Device icon, Token extension icon, and Identity provider icon at the top of a looping process that starts with obtaining a certificate with the user public key and performing Diffie-Hellman (DH) key exchange, followed by decrypting data and obtaining a server nonce to exchange the key and return it to the device.](https://docs-assets.developer.apple.com/published/0787a3d10079c1d6229796291e5d5fdd/media-4294343%402x.png)

The key exchange request is a JOSE that’s formatted per RFC 7519 and signed with the `DeviceSigningKey` and `ES256` per RFC 7515.

The following table specifies the header parameters for a key exchange request:

| Key | Value | Notes |
| --- | --- | --- |
| `typ` | `platformsso-key-request+jwt` | Required. |
| `alg` | `ES256` | Required. The signing algorithm. The system only supports `ES256`. |
| `kid` | The base-64 encoded SHA256 hash of the ANSI X9.63 formatted public key for the signing key | Required. |
| `x5c` | The base-64 encoded device signing certificate from [`saveCertificate(_:keyType:)`](asauthorizationproviderextensionloginmanager/savecertificate(_:keytype:).md) | Optional. The value is base-64 encoded per RFC 7517. |
| `loginConfiguration.customKeyExchangeRequestHeaderClaims` |  | Optional. If present, adds the key value pairs to the assertion. |

The following table specifies the body parameters for a key exchange request:

| Key | Value | Notes |
| --- | --- | --- |
| `version` | `1.0` | Required. |
| `request_type` | `key_exchange` | Required. |
| `key_purpose` | `user_unlock` | Required. |
| `aud` | [`audience`](asauthorizationproviderextensionloginconfiguration/audience.md) | Required. The identity provider (IdP) needs to verify the value to ensure that the assertion was created for them. |
| `iss` | [`clientID`](asauthorizationproviderextensionloginconfiguration/clientid.md) | Required. Per RFC 7523 Section 3. |
| `iat` | The current time | Required. The identity provider (IdP) needs to verify the value. |
| `exp` | 5 minutes from now | Required. The identity provider (IdP) needs to verify the value. |
| `nonce` | A nonce value | Required. A unique nonce value for this request. |
| [`serverNonceClaimName`](asauthorizationproviderextensionloginconfiguration/servernonceclaimname.md) or `request_nonce` | The value returned from the nonce request | Required. The key name is either the [`serverNonceClaimName`](asauthorizationproviderextensionloginconfiguration/servernonceclaimname.md) or the default value `request_nonce`. |
| `username` | [`loginUserName`](asauthorizationproviderextensionuserloginconfiguration/loginusername.md) | Required. If not set, the system uses the local account name. |
| `sub` | [`loginUserName`](asauthorizationproviderextensionuserloginconfiguration/loginusername.md) | Required. Per RFC 7523 Section 3. If not set, the system uses the local account name. |
| `refresh_token` | The current refresh token | Required. |
| `other_publickey` | The base-64 encoded other party public key | Required. |
| `key_context` | The context for the key | Optional. |
| `loginConfiguration.customKeyRequestBodyClaims` |  | Optional. If present, adds the key value pairs to the assertion. |

The following code provides an example of a key exchange request:

```javascript
{
    "kid" : "NKuTL/WHlroXidcyrxgA2Eqpt/cXjh5s22NAkJl7Acs=",
    "x5c" : "MIIBg...YtQ==",
    "typ" : "platformsso-key-request+jwt",
    "alg" : "ES256"
}.{
    "jwe_crypto" : {
        "alg" : "ECDH-ES",
        "enc" : "A256GCM",
        "apv" : "AAAAB...UEwRQ"
    },
    "exp" : 1685759411,
    "request_type" : "key_exchange",
    "nonce" : "7F48971A-E559-4668-A680-97D1BCF7AA0E",
    "version" : "1.0",
    "request_nonce" : "AwABA...HYQgAA",
    "other_publickey" : "BCdD2...RJIv0=",
    "refresh_token" : "abcd1234",
    "key_context" : "BHp+H...Axw==",
    "iss" : "aaff1524-fa35-40c5-94e3-2b233c5f2965",
    "key_purpose" : "user_unlock",
    "sub" : "foo",
    "username" : "foo",
    "iat" : 1685759111
}.[Signature]
```

The key exchange network request is an HTTP POST to the [`keyEndpointURL`](asauthorizationproviderextensionloginconfiguration/keyendpointurl.md) that’s formatted per RFC 7523 and includes the following parameters:

| Key | Value | Notes |
| --- | --- | --- |
| `platform_sso_version` | `2.0` | Required. The version of the login protocol. |
| `grant_type` | `urn:ietf:params:oauth:grant-type:jwt-bearer` | Required. The assertion type. |
| [`customRequestJWTParameterName`](asauthorizationproviderextensionloginconfiguration/customrequestjwtparametername.md) or `assertion` | The base-64 URL encoded signed key exchange request | Required. |
| [`customKeyExchangeRequestValues`](asauthorizationproviderextensionloginconfiguration/customkeyexchangerequestvalues.md) |  | Optional. If present, adds the key value pairs to the key exchange request. |

The following code sample provides an example of a key exchange network request:

```http
POST /oauth2/token HTTP/1.1
Host: auth.example.com
Accept: application/platformsso-key-response+jwt
Content-Type: application/x-www-form-urlencoded
client-request-id: DCAB01D3-B1FE-4E1C-802F-B3EBDCDF9E67
platform_sso_version=2.0&grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer&assertion=ewogIC...JmVhg
```

##### Receive the Key Exchange Response Jwe

The response is a JWE that’s decrypted according to RFC 7516 Section 5.2 with JWE Compact Serialization.

The JWE key exchange response header contains the following values:

| Key | Value | Notes |
| --- | --- | --- |
| `typ` | `platformsso-key-response+jwt` | Required. |
| `enc` | `A256GCM` | Required: The supported encryption algorithm per RFC 7518 Section 4.6. |
| `alg` | `ECDH-ES` | Required. The supported key agreement algorithm per RFC 7518 Section 5.3. |
| `epk` | The ephemeral public key for the key exchange | Required: Per RFC 7518 Section 4.6.1.1, formatted per RFC 7517. |
| `kid` | The `kid` of the ephemeral public key | Optional. |
| `apu` | The base-64 URL encoded `PartyUInfo` for Concat KDF | Required. Per RFC 7518 Section 4.6.1.2. |
| `apv` | The base-64 URL encoded `PartyVInfo` for Concat KDF | Optional. Per RFC 7518 Section 4.6.1.3, the client uses the value from the request. |

The following code provides an example of a key exchange response JWE header:

```javascript
{
    "enc" : "A256GCM",
    "kid" : "cNYXaKrqHO+mBB0MHxuaEUZ2edf0T/GgMNB/tlHGews=",
    "epk" : {
        "y" : "WFUG_Llu2uD70NfbIFOkP5LaNsZlJ1JGIme2DPdbijU",
        "x" : "kXzpm4kt-sbm5QlOJPNZAHhaW8rQ5QE_E2HLFcz2uNs",
        "kty" : "EC",
        "crv" : "P-256"
    }, 
    "apu" : "AAAAB...z3W4o1",
    "typ" : "platformsso-key-response+jwt",
    "alg" : "ECDH-ES"
}
```

The IdP creates a successful key response. The JWE key exchange response body contains the following values:

| Key | Value | Notes |
| --- | --- | --- |
| `exp` | 5 minutes from now | Required. Per RFC 7523 Section 3. |
| `iat` | The current time | Required. Per RFC 7523 Section 3. |
| `key` | The result of Diffie-Hellman standard key exchange with the `other_publickey` in the key exchange request and the private key for the provisioned key | Required. |
| `key_context` | The updated key context for the key | Optional. |

The following code provides an example of a key exchange response JWE body:

```javascript
{
    "exp" : 1685756137,
    "iat" : 1685755837,
    "key" : "DpWD3c4SPmfYteESkRYk+pKVHHuryb1EtnuzhF9OjTc=",
    "key_context" : "BHp+H...Axw=="
}
```

## See Also

- [Performing a WS-Trust login request](performing-a-ws-trust-login-request.md)
  Create a WS-Trust login request using the metadata exchange data (MEX) response.
- [Creating an embedded assertion](creating-an-embedded-assertion.md)
  Request an embedded assertion for login types that require a digital signature for authentication.
- [Creating an encrypted embedded assertion](creating-an-encrypted-embedded-assertion.md)
  Request an encrypted embedded assertion for login types that require password encryption.
- [Creating and validating a login request](creating-and-validating-a-login-request.md)
  Create a signed JOSE login request.
- [Creating a refresh request](creating-a-refresh-request.md)
  Refresh a non-expired token instead of sending a new login request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/supporting-key-requests-and-key-exchange-requests)*