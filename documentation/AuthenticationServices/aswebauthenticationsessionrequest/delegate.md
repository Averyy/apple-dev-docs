# delegate

**Framework**: Authentication Services  
**Kind**: property

A delegate that the session request instance informs about authentication completion.

**Availability**:
- macOS 10.15+

## Declaration

```swift
weak var delegate: (any ASWebAuthenticationSessionRequestDelegate)? { get set }
```

## See Also

- [protocol ASWebAuthenticationSessionRequestDelegate](aswebauthenticationsessionrequestdelegate.md)
  An interface through which the session request can inform its delegate, which is typically a browser, about the outcome of the authentication attempt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsessionrequest/delegate)*