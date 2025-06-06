# includePreviousRefreshTokenInLoginRequest

**Framework**: Authentication Services  
**Kind**: property

A Boolean value that indicates whether to include the previous refresh token in the authentation request.

**Availability**:
- macOS 13.0+

## Declaration

```swift
var includePreviousRefreshTokenInLoginRequest: Bool { get set }
```

## Mentions

- [Creating and validating a login request](creating-and-validating-a-login-request.md)

#### Discussion

If the value is `true` and there’s a `refresh_token` for the user in the SSO tokens, it’s included in the authentication request.

## See Also

- [var previousRefreshTokenClaimName: String](asauthorizationproviderextensionloginconfiguration/previousrefreshtokenclaimname.md)
  The claim name for the previous single sign-on token value in the authentication request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginconfiguration/includepreviousrefreshtokeninloginrequest)*