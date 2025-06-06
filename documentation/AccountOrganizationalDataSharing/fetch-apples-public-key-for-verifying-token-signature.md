# Fetch Apple's public key for verifying token signature

**Framework**: Account & Organizational Data Sharing  
**Kind**: httpRequest

Retrieve the public key associated with the cryptographic identity Apple uses to sign the token.

**Availability**:
- AccountOrganizationalDataSharing 1.0+

#### Overview

If successful, the HTTP status code is 200 (OK), and the [`JWKSet.Keys`](jwkset/jwkset.keys.md) object contains Apple’s public key.

## See Also

- [Creating a client secret](creating-a-client-secret.md)
  Generate a signed token to identify your client application.
- [Generate and validate tokens](generate-and-validate-tokens.md)
  Validate an authorization grant code delivered to your app to obtain tokens, or validate an existing refresh token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accountorganizationaldatasharing/fetch-apple's-public-key-for-verifying-token-signature)*