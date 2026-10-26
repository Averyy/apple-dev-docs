# JWKSet.Keys

**Framework**: SigninwithAppleRESTAPI  
**Kind**: dictionary  
**Role**: Object

An object that defines a single JSON Web Key.

**Availability**:
- Sign in with Apple REST API 1.0+

## Declaration

```
object JWKSet.Keys
```

## Properties

- `alg` (string): The encryption algorithm used to encrypt the token.
- `e` (string): The exponent value for the RSA public key.
- `kid` (string): A 10-character identifier key, obtained from your developer account.
- `kty` (string): The key type parameter setting. You must set to “RSA”.
- `n` (string): The modulus value for the RSA public key.
- `use` (string): The intended use for the public key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/signinwithapplerestapi/jwkset/keys-data.dictionary)*