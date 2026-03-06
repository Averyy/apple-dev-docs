# TokenResponse

**Framework**: Account & Organizational Data Sharing  
**Kind**: dictionary

The response token object returned on a successful request.

**Availability**:
- AccountOrganizationalDataSharing 1.0+

## Declaration

```swift
object TokenResponse
```

## Properties

- `access_token` (string): A token used to access allowed data.
- `expires_in` (number): The amount of time, in seconds, before the access token expires.
- `id_token` (string): A JWT that contains the user’s identity information.
- `refresh_token` (string): The refresh token used to regenerate new access tokens when validating an authorization code. Store this token securely on your server. The refresh token isn’t returned when validating an existing refresh token.
- `token_type` (string): The type of access token, which is always `bearer`.

## See Also

- [object JWKSet](jwkset.md)
  A set of JSON web keys.
- [object ErrorResponse](errorresponse.md)
  The error object returned after an unsuccessful request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accountorganizationaldatasharing/tokenresponse)*