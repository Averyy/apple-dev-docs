# ASWebAuthenticationPresentationContextProviding

**Framework**: Authentication Services  
**Kind**: protocol

An interface the session uses to ask a delegate for a presentation context.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol ASWebAuthenticationPresentationContextProviding : NSObjectProtocol
```

## Mentions

- [Authenticating a User Through a Web Service](authenticating-a-user-through-a-web-service.md)

## Topics

### Specifying the Anchor
- [func presentationAnchor(for: ASWebAuthenticationSession) -> ASPresentationAnchor](aswebauthenticationpresentationcontextproviding/presentationanchor(for:).md)
  Tells the delegate from which window it should present content to the user.
- [typealias ASPresentationAnchor](aspresentationanchor.md)
  A platform-specific type that indicates the kind of user interface element to use as a presentation anchor.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var presentationContextProvider: (any ASWebAuthenticationPresentationContextProviding)?](aswebauthenticationsession/presentationcontextprovider.md)
  A delegate that provides a display context in which the system can present an authentication session to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationpresentationcontextproviding)*