# Creating an encrypted embedded assertion

**Framework**: Authentication Services

Request an encrypted embedded assertion for login types that require password encryption.

#### Overview

During authentication, if the SSO extension requests password encryption by setting the [`loginRequestEncryptionPublicKey`](asauthorizationproviderextensionloginconfiguration/loginrequestencryptionpublickey.md) in the login configuration, the system doesn’t send the password in the login request. Instead, it creates an encrypted embedded assertion instead, that contains the password. The assertion is a JSON Web Encryption (JWE) object that’s encrypted according to RFC 7516 Section 5.1 with JWE Compact Serialization. The supported key agreement algorithm is `ECDH-ES` per RFC 7518 Section 4.6. This algorithm is `ECIES`, a proven-secure algorithm with the public keys included. See the Configure concatenation key derivation function (Concat KDF) section below for input values. Key agreement uses the public key for the [`loginRequestEncryptionPublicKey`](asauthorizationproviderextensionloginconfiguration/loginrequestencryptionpublickey.md) that’s supplied during registration. The supported encryption algorithm is `A256GCM` per RFC 7518 Section 5.3.

The following table specifies the header parameters that the system uses to create an encrypted embedded assertion:

| Key | Value | Notes |
| --- | --- | --- |
| `typ` | `platformsso-encrypted-login-assertion+jwt` | Required. |
| `enc` | `A256GCM` | Required. The supported encryption algorithm per RFC 7518 Section 4.6. |
| `alg` | `ECDH-ES` | Required. The supported key agreement algorithm per RFC 7518 Section 5.3. |
| `epk` | The ephemeral public key for the key exchange | Required. Per RFC 7518 Section 4.6.1.1, formatted per RFC 7517. |
| `kid` | The `kid` of the ephemeral public key | Optional. |
| `apu` | The base-64 URL encoded `PartyUInfo` for Concat KDF | Required. Per RFC 7518 Section 4.6.1.2. |
| `apv` | The base-64 URL encoded `PartyVInfo` for Concat KDF | Required. Per RFC 7518 Section 4.6.1.3, the client uses the value from the request. |
| `loginConfiguration.customAssertionRequestHeaderClaims` merged with `userLoginConfiguration.customAssertionRequestHeaderClaims` |  | Optional. If present, adds key value pairs to the assertion. |

The following table specifies the body parameters that the system uses to create an encrypted embedded assertion:

| Key | Value | Notes |
| --- | --- | --- |
| `aud` | [`audience`](asauthorizationproviderextensionloginconfiguration/audience.md) | Required. The identity provider (IdP) needs to verify the value to ensure that the system created the assertion for them. |
| `iat` | The current time | Required. The IdP needs to verify the value. |
| `exp` | 5 minutes from now | Required. The IdP needs to verify the value. |
| `iss` | [`loginUserName`](asauthorizationproviderextensionuserloginconfiguration/loginusername.md) | Required. If not set, the system uses the local account name. |
| `sub` | [`loginUserName`](asauthorizationproviderextensionuserloginconfiguration/loginusername.md) | Required. If not set, the system uses the local account name. |
| `nonce` | A nonce value | Required: If included, the IdP needs to verify that this value matches the nonce in the login request. |
| `scope` | `openid offline_access` and [`additionalScopes`](asauthorizationproviderextensionloginconfiguration/additionalscopes.md) | Required. The requested scope for the assertion. The default value is `openid offline_access` and the system appends any additional ones to it. The default additional scope is `urn:apple:platformsso`. This value needs to match the scope in the login request. |
| `password` | The password for authentication | Required. |
| [`serverNonceClaimName`](asauthorizationproviderextensionloginconfiguration/servernonceclaimname.md) or `request_nonce` | The value returned from the nonce request | Required: The key name is either the [`serverNonceClaimName`](asauthorizationproviderextensionloginconfiguration/servernonceclaimname.md) or the default value `request_nonce`. |
| `loginConfiguration.customAssertionRequestBodyClaims` merged with `userLoginConfiguration.customAssertionRequestBodyClaims` |  | Optional: If present, adds the key value pairs to the assertion. |

##### Configure Concatenation Key Derivation Function Concat Kdf

Configuration of Concat KDF for platform SSO is per RFC 7518 Section 4.6.2 and NIST.800-56A sections 5.8.1 and 6.2.2.2. See the input definitions in the table below. The system concatenates these values per NIST.800-56A sections 5.8.1 and then it computes a SHA-256 hash to create the key. Then, it sends the `PartyUInfo` and `PartyVInfo` values to the server in the header.

| Key | Value | Notes |
| --- | --- | --- |
| `AlgorithmID` | Set to the octets of the ASCII representation of the `enc` (algorithm) header parameter value. | Per RFC 7518 Section 4.6.2 when using direct key agreement |
| `PartyUInfo` | ` |  |
| `PartyVInfo` | This needs to use the `jwe_crypto.apv` value from the login request.  ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) ` |  |
| `SuppPubInfo` | Set to the number of bits in the desired output key. | Per RFC 7518 Section 4.6.2 |
| `SuppPrivInfo` | `NULL` | Per RFC 7518 Section 4.6.2 |

The following code sample provides an example of an encrypted embedded assertion request:

```javascript
{
  "enc" : "A256GCM",
  "apv" : "AAAADUFQUExFRU1CRURERUQAAABBBCX87eqonWyNUNz2JeH2wG68_WiPfQlJw6AiDvHSD08n5Hdn1oDUBxhL_TRarvhUUGDYsnBRk2HRH_ZoXGtpUncAAABuQXdBQkFBQUFBQUFEQU96X0JBRHZfeHRndV9TTTFNdm9xMDJQWXpfWWZYeHg1RkFnY0xITE5pa0g2Z2pyQld3Y3FuUldfaGF4cU85SkNpUGF0NUtma1RpbHkwNFM4RUgzQVF3VnNXQ3hIWVFnQUE",
  "alg" : "ECDH-ES",
  "epk" : {
    "y" : "1wfUpcnhOq7SPl77UBfkanXdQObiBXDIDLx0n1_zlJI",
    "x" : "NUnMKzz81Fl0SilEVYgWWjL_4lTAaXHeJ4uJGQ19AAk",
    "kty" : "EC",
    "crv" : "P-256"
  },
  "kid" : "7y1xXc4I6iAyldmVkIeGtQxo8NRq2FgKFb++Or13jxU=",
  "apu" : "AAAABUFQUExFAAAAQQQ1ScwrPPzUWXRKKURViBZaMv_iVMBpcd4ni4kZDX0ACdcH1KXJ4Tqu0j5e-1AX5Gp13UDm4gVwyAy8dJ9f85SS",
  "typ" : "platformsso-encrypted-login-assertion+jwt"
}.{
  "iat" : 1685732130,
  "password" : "bar",
  "iss" : "foo",
  "request_nonce" : "AwABAAAAAAADAOz_BADv_xtgu_SM1Mvoq02PYz_YfXxx5FAgcLHLNikH6gjrBWwcqnRW_haxqO9JCiPat5KfkTily04S8EH3AQwVsWCxHYQgAA",
  "sub" : "foo",
  "scope" : "openid offline_access urn:apple:platformsso",
  "exp" : 1685732430,
  "aud" : "060798FF-814E-4C38-97F8-28C954B7E058",
  "nonce" : "D1DEE607-0F44-43F5-8B3E-042E91F425A7"
}.[Signature]

```

For more information, see [`Authentication process`](authentication-process.md).

## See Also

- [Performing a WS-Trust login request](performing-a-ws-trust-login-request.md)
  Create a WS-Trust login request using the metadata exchange data (MEX) response.
- [Creating an embedded assertion](creating-an-embedded-assertion.md)
  Request an embedded assertion for login types that require a digital signature for authentication.
- [Creating and validating a login request](creating-and-validating-a-login-request.md)
  Create a signed JOSE login request.
- [Creating a refresh request](creating-a-refresh-request.md)
  Refresh a non-expired token instead of sending a new login request.
- [Supporting key requests and key exchange requests](supporting-key-requests-and-key-exchange-requests.md)
  Support the platform SSO 2.0 protocol for encryption and decryption operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/creating-an-encrypted-embedded-assertion)*