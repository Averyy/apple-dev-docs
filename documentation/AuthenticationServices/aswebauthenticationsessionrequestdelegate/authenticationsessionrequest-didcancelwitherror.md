# authenticationSessionRequest(_:didCancelWithError:)

**Framework**: Authentication Services  
**Kind**: method

Tells the delegate, typically a browser, that the authentication was canceled.

**Availability**:
- macOS 10.15+

## Declaration

```swift
optional func authenticationSessionRequest(_ authenticationSessionRequest: ASWebAuthenticationSessionRequest, didCancelWithError error: any Error)
```

## Parameters

- `authenticationSessionRequest`: The request sending the message.
- `error`: An error that indicates the reason for the cancelation.

## See Also

- [func authenticationSessionRequest(ASWebAuthenticationSessionRequest, didCompleteWithCallbackURL: URL)](aswebauthenticationsessionrequestdelegate/authenticationsessionrequest(_:didcompletewithcallbackurl:).md)
  Tells the delegate, typically a browser, that the authentication completed successfully.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsessionrequestdelegate/authenticationsessionrequest(_:didcancelwitherror:))*