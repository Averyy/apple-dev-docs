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
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func presentationAnchor(for controller: ASAuthorizationController) -> ASPresentationAnchor
```

#### Return Value

A user interface element that can act as the anchor for the authorization presentation.

## Parameters

- `controller`: The controller asking for the presentation anchor.

## See Also

- [typealias ASPresentationAnchor](aspresentationanchor.md)
  A platform-specific type that indicates the kind of user interface element to use as a presentation anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationcontrollerpresentationcontextproviding/presentationanchor(for:))*