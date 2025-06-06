# ASAuthorization.OpenIDOperation

**Framework**: Authentication Services  
**Kind**: struct

The kinds of operations that you can perform with OpenID authentication.

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
struct OpenIDOperation
```

#### Discussion

Use one of these values as the [`requestedOperation`](asauthorizationopenidrequest/requestedoperation.md) property in an OpenID request that you make with an instance of either [`ASAuthorizationAppleIDRequest`](asauthorizationappleidrequest.md) or [`ASAuthorizationSingleSignOnRequest`](asauthorizationsinglesignonrequest.md).

## Topics

### Operation Types
- [static let operationLogin: ASAuthorization.OpenIDOperation](asauthorization/openidoperation/operationlogin.md)
  An operation used to authenticate a user.
- [static let operationRefresh: ASAuthorization.OpenIDOperation](asauthorization/openidoperation/operationrefresh.md)
  An operation that refreshes the logged-in user’s credentials.
- [static let operationLogout: ASAuthorization.OpenIDOperation](asauthorization/openidoperation/operationlogout.md)
  An operation that ends an authenticated session.
- [static let operationImplicit: ASAuthorization.OpenIDOperation](asauthorization/openidoperation/operationimplicit.md)
  An operation that depends on the particular kind of credential provider.
### Creating an Operation
- [init(String)](asauthorization/openidoperation/init(_:).md)
  Creates an operation from the given string.
- [init(rawValue: String)](asauthorization/openidoperation/init(rawvalue:).md)
  Creates an operation from the given string.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var requestedOperation: ASAuthorization.OpenIDOperation](asauthorizationopenidrequest/requestedoperation.md)
  The OpenID authentication operation you want this request to perform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorization/openidoperation)*