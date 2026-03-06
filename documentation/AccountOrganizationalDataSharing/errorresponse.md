# ErrorResponse

**Framework**: Account & Organizational Data Sharing  
**Kind**: dictionary

The error object returned after an unsuccessful request.

**Availability**:
- AccountOrganizationalDataSharing 1.0+

## Declaration

```swift
object ErrorResponse
```

#### Overview

The `error` property is one of the following values:

- **`invalid_request`**: A malformed request, typically because it’s missing a parameter, contains an unsupported parameter, includes multiple credentials, or uses more than one mechanism for authenticating the client.
- **`invalid_client`**: The client authentication failed, typically due to a mismatched or invalid client identifier, invalid client secret (expired token, malformed claims, or invalid signature), or mismatched or invalid redirect URI.
- **`invalid_grant`**: The authorization grant or refresh token is invalid, typically due to a mismatched or invalid client identifier, invalid code (expired or previously used authorization code), or invalid refresh token.
- **`unauthorized_client`**: The client isn’t authorized to use this authorization grant type.
- **`unsupported_grant_type`**: The authenticated client isn’t authorized to use this grant type.
- **`invalid_scope`**: The requested scope is invalid.

## Properties

- `error` (string): A string that describes the reason for the unsuccessful request. The string is one of the allowed values, listed below.

## See Also

- [object JWKSet](jwkset.md)
  A set of JSON web keys.
- [object TokenResponse](tokenresponse.md)
  The response token object returned on a successful request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accountorganizationaldatasharing/errorresponse)*