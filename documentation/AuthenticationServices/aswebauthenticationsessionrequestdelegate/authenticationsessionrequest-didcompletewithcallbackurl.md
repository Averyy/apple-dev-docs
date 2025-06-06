# authenticationSessionRequest(_:didCompleteWithCallbackURL:)

**Framework**: Authentication Services  
**Kind**: method

Tells the delegate, typically a browser, that the authentication completed successfully.

**Availability**:
- macOS 10.15+

## Declaration

```swift
optional func authenticationSessionRequest(_ authenticationSessionRequest: ASWebAuthenticationSessionRequest, didCompleteWithCallbackURL callbackURL: URL)
```

## Parameters

- `authenticationSessionRequest`: The request sending the message.
- `callbackURL`: A URL using the scheme indicated by the request’s   property that indicates the outcome of the authentication attempt.

## See Also

- [func authenticationSessionRequest(ASWebAuthenticationSessionRequest, didCancelWithError: any Error)](aswebauthenticationsessionrequestdelegate/authenticationsessionrequest(_:didcancelwitherror:).md)
  Tells the delegate, typically a browser, that the authentication was canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsessionrequestdelegate/authenticationsessionrequest(_:didcompletewithcallbackurl:))*