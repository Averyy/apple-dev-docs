# JWKSet.Keys

**Framework**: Account & Organizational Data Sharing  
**Kind**: dictionary

An object that defines a single JSON Web Key.

**Availability**:
- AccountOrganizationalDataSharing 1.0+

## Declaration

```swift
object JWKSet.Keys
```

#### Overview

JWK is an open standard ([`RFC 7517`](https://developer.apple.comhttps://www.rfc-editor.org/rfc/rfc7517)) that defines a data structure to represent cryptographic keys.

## Properties

- `alg` (string): The encryption algorithm used to encrypt the token.
- `e` (string): The exponent value for the RSA public key.
- `kid` (string): A 10-character identifier key, obtained from your developer account.
- `kty` (string): The key type parameter setting. Use the value `RSA`.
- `n` (string): The modulus value for the RSA public key.
- `use` (string): The intended use for the public key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accountorganizationaldatasharing/jwkset/jwkset.keys)*