# operationLogout

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Type Property

An operation that ends an authenticated session.

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
static let operationLogout: ASAuthorization.OpenIDOperation
```

```c
extern ASAuthorizationOpenIDOperation const ASAuthorizationOperationLogout;
```

## See Also

### Operation Types
- [static let operationLogin: ASAuthorization.OpenIDOperation](./operationlogin.md)
  An operation used to authenticate a user.
- [static let operationRefresh: ASAuthorization.OpenIDOperation](./operationrefresh.md)
  An operation that refreshes the logged-in user’s credentials.
- [static let operationImplicit: ASAuthorization.OpenIDOperation](./operationimplicit.md)
  An operation that depends on the particular kind of credential provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorization/openidoperation/operationlogout)*