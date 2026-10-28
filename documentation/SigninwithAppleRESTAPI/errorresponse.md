# ErrorResponse

**Framework**: SigninwithAppleRESTAPI  
**Kind**: dictionary  
**Role**: Object

The error object returned after an unsuccessful request.

**Availability**:
- Sign in with Apple REST API 1.0+

## Declaration

```
object ErrorResponse
```

## Mentions

- [Incorporating Sign in with Apple into other platforms](../SigninwithApple/incorporating-sign-in-with-apple-into-other-platforms.md)

## Discussion

The `error` property contains exactly one of the following values:

- **`invalid_request`**: The request is malformed, typically because it’s missing a parameter, contains an unsupported parameter, includes multiple credentials, or uses more than one mechanism for authenticating the client.
- **`invalid_client`**: The client authentication failed, typically due to a mismatched or invalid client identifier, invalid client secret (expired token, malformed claims, or invalid signature), or mismatched or invalid redirect URI.
- **`invalid_grant`**: The authorization grant or refresh token is invalid, typically due to a mismatched or invalid client identifier, invalid code (expired or previously used authorization code), or invalid refresh token.
- **`unauthorized_client`**: The client isn’t authorized to use this authorization grant type.
- **`unsupported_grant_type`**: The authenticated client isn’t authorized to use this grant type.
- **`invalid_scope`**: The requested scope is invalid.

## Properties

- `error` (string): A string that describes the reason for the unsuccessful request. The string consists of a single allowed value.

  **Allowed Values**: `invalid_request`, `invalid_client`, `invalid_grant`, `unauthorized_client`, `unsupported_grant_type`, `invalid_scope`

## See Also

### Common objects
- [object JWKSet](./jwkset.md)
  A set of JSON Web Key objects.
- [object TokenResponse](./tokenresponse.md)
  The response token object returned on a successful request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/signinwithapplerestapi/errorresponse)*