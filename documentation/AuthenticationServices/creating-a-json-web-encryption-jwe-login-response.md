# Creating a JSON Web Encryption (JWE) login response

**Framework**: Authentication Services

Create an encrypted login response and configure the concatenation key derivation function (Concat KDF).

#### Overview

The identity provider (IdP) creates a login response, which is a JWE that’s encrypted according to RFC 7516 Section 5.1 with JWE Compact Serialization. The supported key agreement algorithm is ECDH-ES per RFC 7518 Section 4.6. See the following section for a description of the concatenation key derivation function (Concat KDF) inputs.

Key agreement uses the public key for the `UserDeviceEncryptionKey` that’s exchanged during registration. The supported encryption algorithm is A256GCM per RFC 7518 Section 5.3.

##### Configure Concat Kdf

RFC 7518 Section 4.6.2 and NIST.800-56A sections 5.8.1 and 6.2.2.2 describe the configuration of Concat KDF for Platform SSO. See the table below for input definitions. The system concatenates the values per NIST.800-56A sections 5.8.1, and then computes a SHA-256 hash that it uses to create the key. The login response header needs to contain the `PartyUInfo`.

| Key | Value | Notes |
| --- | --- | --- |
| `AlgorithmID` | Set to the octets of the ASCII representation of the enc (algorithm) Header Parameter value. | Per RFC 7518 Section 4.6.2 when using direct key agreement |
| `PartyUInfo` | ` |  |
| `PartyVInfo` | This needs to use the `jwe_crypto.apv` value from the login request. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) ` |  |
| `SuppPubInfo` | Set to the number of bits in the desired output key. | Per RFC 7518 Section 4.6.2 |
| `SuppPrivInfo` | `NULL` | Per RFC 7518 Section 4.6.2 |

> **Note**:  The key agreement algorithm ECDH-ES is actually ECIES, a proven-secure algorithm with the public keys included.

Here’s an example of the Concat KDF inputs:

`3491708C92422BB807EDF2B8183A42737C5DAA6C39BA9535321D51C836D7ADA1`

Length || data = `00000007||4132353647434D`

Length || data = `00000005||4150504C45`

Ephemeral Public Key (EPK):

`“epk” : {`

```None
`“y” : “jbOoWZbgDFTEfLa1O_7ZuJy3R8d2XAw0CHWUKmJLsbU”,`

`“x” : “BkFHRYQoleq39LplGqlcmsEdnw64w0wbcbHAEjrM4pw”,`

`“kty” : “EC”,`

`“crv” : “P-256”`
```

`}`

Length || data =

`00000041||0406414745842895EAB7F4BA651AA95C9AC11D9F0EB8C34C1B71B1C0123ACCE29C8DB3A85996E00C54C47CB6B53BFED9B89CB747C7765C0C340875942A624BB1B5`

Final `partyUInfo` length || data:

`0000004E||000000054150504C45000000410406414745842895EAB7F4BA651AA95C9AC11D9F0EB8C34C1B71B1C0123ACCE29C8DB3A85996E00C54C47CB6B53BFED9B89CB747C7765C0C340875942A624BB1B5`

Response JWE `apu` header is the base-64 URL encoded `partyUInfo`:

`AAAABUFQUExFAAAAQQSf34Uch3TYF27T8SpbtNWCjpKUSjHGDwoiUz8Yoh1nrQidjfO6iMRZIqrsNERt8JnlI2aUwAlZktJ8DZFGWKaB`````

Device Encryption Public Key:

`{`

```None
`“crv” : “P-256”,`

`“kty” : “EC”,`

`“x” : “mcJyr2BqUQHlscaGoWTw_4QNxDUqI1lR11kCRAzLJkk”,`

`“y” : “P_mLtZKoMMC3G8PtRleKzm1c5D0afPZX_61s70Cx75I”`
```

`}`

Length || data =

`00000041||0499C272AF606A5101E5B1C686A164F0FF840DC4352A235951D75902440CCB26493FF98BB592A830C0B71BC3ED46578ACE6D5CE43D1A7CF657FFAD6CEF40B1EF92`

Nonce: `B7F1FC32-9121-4E2A-9E32-8417E03675DD`

Length || data =

`00000024||42374631464333322D393132312D344532412D394533322D383431374530333637354444`

Final `partyVInfo` length || data:

`000000054||170706C65000000410499C272AF606A5101E5B1C686A164F0FF840DC4352A235951D75902440CCB26493FF98BB592A830C0B71BC3ED46578ACE6D5CE43D1A7CF657FFAD6CEF40B1EF920000002442374631464333322D393132312D344532412D394533322D383431374530333637354444`

The login request `jwe_crypto.apv` header is the base 64 URL encoded `partyVInfo`:

`AAAABUFwcGxlAAAAQQSZwnKvYGpRAeWxxoahZPD_hA3ENSojWVHXWQJEDMsmST_5i7WSqDDAtxvD7UZXis5tXOQ9Gnz2V_-tbO9Ase-SAAAAJEI3RjFGQzMyLTkxMjEtNEUyQS05RTMyLTg0MTdFMDM2NzVERA```

The complete SHA-256 input is:

`000000013491708C92422BB807EDF2B8183A42737C5DAA6C39BA9535321D51C836D7ADA1000000074132353647434D0000004E000000054150504C45000000410406414745842895EAB7F4BA651AA95C9AC11D9F0EB8C34C1B71B1C0123ACCE29C8DB3A85996E00C54C47CB6B53BFED9B89CB747C7765C0C340875942A624BB1B500000076000000054170706C65000000410499C272AF606A5101E5B1C686A164F0FF840DC4352A235951D75902440CCB26493FF98BB592A830C0B71BC3ED46578ACE6D5CE43D1A7CF657FFAD6CEF40B1EF920000002442374631464333322D393132312D344532412D394533322D38343137453033363735444400000100`

The Concat KDF result is:

`A146E4A23BDA2E53826C04D2F442BCFBD87BC2719D74B8A7DA00AF976267712E`

##### Create the Response Jwe Header

The response is a JWE that’s decrypted according to RFC 7516 Section 5.2 with JWE Compact Serialization.

The JWE response header contains the following values:

| Key | Value | Notes |
| --- | --- | --- |
| `typ` | `JWT` | Required if the extension SDK is macOS 13.x. |
|  | `platformsso-login-response+jwt` | Optional if the extension SDK is macOS 14.x or later. |
| `enc` | `A256GCM` | Required. The supported encryption algorithm per RFC 7518 Section 4.6. |
| `alg` | `ECDH-ES` | Required. The supported key agreement algorithm per RFC 7518 Section 5.3. |
| `epk` | The ephemeral public key for the key exchange | Required. Per RFC 7518 Section 4.6.1.1, formatted per RFC 7517. |
| `kid` | The `kid` of the ephemeral public key. | Optional. |
| `apu` | The base-64 URL encoded `PartyUInfo` for Concat KDF. | Required. Per RFC 7518 Section 4.6.1.2. |
| `apv` | The base-64 URL encoded `PartyVInfo` for Concat KDF | Optional. Per RFC 7518 Section 4.6.1.3, the client uses the value from the request. |

The following code provides an example of a login response JWE header:

```javascript
{
    "enc" : "A256GCM",
    "kid" : "d20/VkvmbjLfmi1ufWQqSzzPx+CFHH4N/57Smjk34FE=",
    "epk" : {
        "y" : "doNOTncIN5cjSujnX2qiuHOFL-fag2iypIpDXx1eLdo",
        "x" : "43ZFsDGBnttfDSiNBbsdmXnj3N9ieZaT0nEsEZHk7eo",
        "kty" : "EC",
        "crv" : "P-256"
    }, 
    "apu" : "AAAABUFQUExFAAAAQQTjdkWwMYGe218NKI0Fux2ZeePc32J5lpPScSwRkeTt6naDTk53CDeXI0ro519qorhzhS_n2oNosqSKQ18dXi3a",
    "typ" : "platformsso-login-response+jwt",
    "alg" : "ECDH-ES"
}
```

##### Create the Response Jwe Body

The IdP creates a successful login response formatted per the OpenID spec, including an `id_token` and `refresh_token`. The `refresh_token` is the token that the system uses for SSO.

The JWE response body contains the following values:

| Key | Value | Notes |
| --- | --- | --- |
| `id_token` | Base-64 URL encoded `id_token` JOSE signed by the IdP. | Required. |
| `refresh_token` | `refresh_token`, which is treated as an opaque value. | Required. |
| `refresh_token_expires_in` | The time (in seconds) until the refresh token expires. If not present, the system uses `expires_in`. | Recommended. |
| `expires_in` | The time in seconds until the tokens expire. | Required, if `refresh_token_expires_in` isn’t present |
| `token_type` | `Bearer` | Expected, but not verified |
| Kerberos TGT | Kerberos TGT, if [`kerberosTicketMappings`](asauthorizationproviderextensionloginconfiguration/kerberosticketmappings.md) is defined. | Optional. |

The following code provides an example of a login response JWE body:

```javascript
{
    "refresh_token" : "AwABA...0t4B4",
    "id_token" : "ewogI...lEvVQ",
    "expires_on" : 1685766415,
    "token_type" : "Bearer",
    "expires_in" : 28800,
    "refresh_token_expires_in" : 28800
}
```

##### Handle a Failed Response

If the response returns a status code other than `200`, Platform SSO checks whether there’s a credential failure. If the credential is incorrect, the system prompts the user to enter it again. Other errors require another login attempt at a later time.

By default, a HTTP response code of `401` is a credential error. The IdP can optionally specify a predicate to parse a JSON formatted response to determine if the result is a credential error or not, when the response code is `400` or `401`. The [`invalidCredentialPredicate`](asauthorizationproviderextensionloginconfiguration/invalidcredentialpredicate.md) specifies the predicate.

For example, the system can use the predicate `errorCode = ‘C0000006’ AND suberror = ‘invalid_password’` with the following failed response to match to a credential error:

```javascript
HTTP/1.1 400 Bad Request
Cache-Control: no-store, no-cache
Pragma: no-cache
Content-Type: application/json; charset=utf-8

{
    "errorCode": "C0000006",
    "suberror": "invalid_password"
}
```

##### Use the Kerberos Mapping

The SSO response from the IdP can optionally include Kerberos ticket-granting tickets (TGTs) for the user. Platform SSO uses the kerberos mapping from the login configuration to import the TGTs into a Kerberos cache and optionally use the TGT with the Kerberos extension.

The Kerberos mapping is an instance of [`ASAuthorizationProviderExtensionKerberosMapping`](asauthorizationproviderextensionkerberosmapping.md) in the [`kerberosTicketMappings`](asauthorizationproviderextensionloginconfiguration/kerberosticketmappings.md). It indicates the SSO response entries to use for each of the elements, with each ticket being a sub-dictionary of the login response. The mapping entry maps the response JSON entry names for each ticket.

The following code sample provides an example of a login response body:

```javascript
{

    "expires_in" : 3600,
    "expires_on" : "1646867283.216107",
    "id_token" : "ewogIC...hyI9w",
    "refresh_token" : "abcd1234",
    "token_type" : "Bearer",
    "login_tgt" : {
        "clientName" "foo",
        "encryptionKeyType" : 18,
        "messageBuffer" : "a4IGhDCCBoC...h3YEY6IQ==",
        "realm" : "EXAMPLE.COM",
        "serviceName" : "krbtgt/EXAMPLE.COM",
        "sessionKey" : "EjzbGACRvT1WnSeBkQDnvevt7A7/MuGw0oEVAQRZutU="
    }
}
```

For the above login response, the Kerberos ticket mapping is:

| Key | Value | Notes |
| --- | --- | --- |
| `ticketKeyPath` | `login_tgt` | The keypath in the response JSON that uses this set of mappings. |
| `messageBufferKeyName` | `messageBuffer` | The key name that contains the base-64 encoded kerberos AS-REP string. |
| `realmKeyName` | `realm` | The key name that contains the Kerberos Realm string. |
| `serviceNameKeyName` | `serviceName` | The key name that contains the Kerberos service name string. |
| `clientNameKeyName` | `clientName` | The key name that contains the Kerberos client name string. |
| `encryptionKeyTypeKeyName` | `encryptionKeyType` | The key name that contains the Kerberos session key type number. The value for this key should be the correct encryption type per RFC 3962 Section 7 for the session key. |
| `sessionKeyKeyName` | `sessionKey` | The key name that contains the Kerberos session key. |

The [`ASAuthorizationProviderExtensionKerberosMapping`](asauthorizationproviderextensionkerberosmapping.md) is:

```swift
var mapping = ASAuthorizationProviderExtensionKerberosMapping()
mapping.ticketKeyPath = "login_tgt"
mapping.clientNameKeyName = "clientName"
mapping.encryptionKeyTypeKeyName = "encryptionKeyType"
mapping.messageBufferKeyName = "messageBuffer"
mapping.realmKeyName = "realm"
mapping.serviceNameKeyName = "serviceName"
mapping.sessionKeyKeyName = "sessionKey"
```

If the sytem finds all the values, it imports the ticket into a Kerberos cache that the Kerberos extension can use.

If the Kerberos ticket is from a read-only domain controller (RODC) per MS-KILE Section 3.1.5.8, a refresh request to the key distribution center (KDC) uses the ticket to exchange it for a TGT that contains a privileged attribute certificate (PAC).

## See Also

- [Processing the JSON Web Encryption (JWE) login response](processing-the-json-web-encryption-jwe-login-response.md)
  Validate the encrypted response.
- [Performing encryption verification](performing-encryption-verification.md)
  Verify the login request and create a JSON Web Encryption (JWE) response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/creating-a-json-web-encryption-jwe-login-response)*