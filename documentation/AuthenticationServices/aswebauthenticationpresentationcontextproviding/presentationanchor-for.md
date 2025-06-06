# presentationAnchor(for:)

**Framework**: Authentication Services  
**Kind**: method  
**Required**: Yes

Tells the delegate from which window it should present content to the user.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func presentationAnchor(for session: ASWebAuthenticationSession) -> ASPresentationAnchor
```

## Mentions

- [Authenticating a User Through a Web Service](authenticating-a-user-through-a-web-service.md)

#### Return Value

A user interface element that can act as the anchor for the authentication presentation.

## Parameters

- `session`: The session asking for the presentation anchor.

## See Also

- [typealias ASPresentationAnchor](aspresentationanchor.md)
  A platform-specific type that indicates the kind of user interface element to use as a presentation anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationpresentationcontextproviding/presentationanchor(for:))*