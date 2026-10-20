# operationImplicit

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Type Property

An operation that depends on the particular kind of credential provider.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
static let operationImplicit: ASAuthorization.OpenIDOperation
```

```c
extern ASAuthorizationOpenIDOperation const ASAuthorizationOperationImplicit;
```

## See Also

### Operation Types
- [static let operationLogin: ASAuthorization.OpenIDOperation](./operationlogin.md)
  An operation used to authenticate a user.
- [static let operationRefresh: ASAuthorization.OpenIDOperation](./operationrefresh.md)
  An operation that refreshes the logged-in user’s credentials.
- [static let operationLogout: ASAuthorization.OpenIDOperation](./operationlogout.md)
  An operation that ends an authenticated session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorization/openidoperation/operationimplicit)*