# Fetch Apple’s public key to verify token signatures

**Framework**: SigninwithAppleRESTAPI  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Fetch Apple’s public key to verify ID token and server notification signatures.

**Availability**:
- Sign in with Apple REST API 1.0+

## Mentions

- [Processing changes for Sign in with Apple accounts](../SigninwithApple/processing-changes-for-sign-in-with-apple-accounts.md)

## Discussion

If successful, the HTTP status code is 200 (OK) and the [`JWKSet.Keys`](./jwkset/keys-data.dictionary.md) object contains Apple’s public key. For more information, see [Verifying a user](../SigninwithApple/verifying-a-user.md) and [Decode and validate the notifications](../SigninwithApple/processing-changes-for-sign-in-with-apple-accounts.md#Decode-and-validate-the-notifications).

> **Note**:  The endpoint can return multiple keys, and the count of keys can vary over time. From this set of keys, select the key with the matching key identifier (`kid`) to verify the signature of any JSON Web Token (JWT) issued by Apple. For more information, see the [JSON Web Signature](https://tools.ietf.org/html/rfc7515) specification.

## Endpoint

`GET https://appleid.apple.com/auth/keys`

## Responses

- `200` OK (`JWKSet`, `application/json`): The request was successful.

## See Also

### Generating and revoking tokens
- [Creating a client secret](../AccountOrganizationalDataSharing/creating-a-client-secret.md)
  Generate a signed token to identify your client application.
- [Token validation](./generate-and-validate-tokens.md)
  Validate an authorization grant code delivered to your app to obtain tokens, or validate an existing refresh token.
- [Token revocation](./revoke-tokens.md)
  Invalidate the tokens and associated user authorizations for a user when they are no longer associated with your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/signinwithapplerestapi/fetch-apple's-public-key-for-verifying-token-signature)*