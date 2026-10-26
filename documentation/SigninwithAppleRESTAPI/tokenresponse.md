# TokenResponse

**Framework**: SigninwithAppleRESTAPI  
**Kind**: dictionary  
**Role**: Object

The response token object returned on a successful request.

**Availability**:
- Sign in with Apple REST API 1.0+

## Declaration

```
object TokenResponse
```

## Properties

- `access_token` (string): A token used to access allowed data, such as generating and exchanging transfer identifiers during user migration, or to invalidate tokens after a user revokes consent for your app to use their Apple Account. For more information, see [Transferring your apps and users to another team](../SigninwithApple/transferring-your-apps-and-users-to-another-team.md), [Bringing new apps and users into your team](../SigninwithApple/bringing-new-apps-and-users-into-your-team.md), [Processing changes for Sign in with Apple accounts](../SigninwithApple/processing-changes-for-sign-in-with-apple-accounts.md), and [`Token revocation`](./revoke-tokens.md).
- `expires_in` (number): The amount of time, in seconds, before the access token expires.
- `id_token` (string): A JSON Web Token (JWT) that contains the user’s identity information. For more information, see [`id_token`](../SigninwithAppleJS/authorizationi/id_token.md).
- `refresh_token` (string): The refresh token used to regenerate new access tokens when validating an authorization code. Store this token securely on your server. The refresh token isn’t returned when validating an existing refresh token. The refresh token can also be invalidated after a user revokes consent for your app to use their Apple Account. For more information, see [`Token validation`](./generate-and-validate-tokens.md), [Processing changes for Sign in with Apple accounts](../SigninwithApple/processing-changes-for-sign-in-with-apple-accounts.md), and [`Token revocation`](./revoke-tokens.md).
- `token_type` (string): The type of access token, which is always `bearer`.

## See Also

### Common objects
- [object JWKSet](./jwkset.md)
  A set of JSON Web Key objects.
- [object ErrorResponse](./errorresponse.md)
  The error object returned after an unsuccessful request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/signinwithapplerestapi/tokenresponse)*