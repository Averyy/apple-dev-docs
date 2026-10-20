# previousRefreshTokenClaimName

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

The claim name for the previous single sign-on token value in the authentication request.

**Availability**:
- macOS 13.0+

## Declaration

```swift
var previousRefreshTokenClaimName: String { get set }
```

```objc
@property (nonatomic, copy) NSString * previousRefreshTokenClaimName;
```

## Mentions

- [Creating and validating a login request](../creating-and-validating-a-login-request.md)

## See Also

### Configuring the previous refresh token
- [var includePreviousRefreshTokenInLoginRequest: Bool](./includepreviousrefreshtokeninloginrequest.md)
  A Boolean value that indicates whether to include the previous refresh token in the authentation request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginconfiguration/previousrefreshtokenclaimname)*