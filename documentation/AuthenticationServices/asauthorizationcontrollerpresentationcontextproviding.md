# ASAuthorizationControllerPresentationContextProviding

**Framework**: Authentication Services  
**Kind**: protocol  
**Role**: Protocol

An interface the controller uses to ask a delegate for a presentation context.

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
protocol ASAuthorizationControllerPresentationContextProviding : NSObjectProtocol
```

```objc
@protocol ASAuthorizationControllerPresentationContextProviding <NSObject>
```

## Mentions

- [Authenticating people by using passkeys in browser apps](./authenticating-people-by-using-passkeys-in-browser-apps.md)

## Topics

### Specifying the Anchor
- [func presentationAnchor(for: ASAuthorizationController) -> ASPresentationAnchor](./asauthorizationcontrollerpresentationcontextproviding/presentationanchor%28for%29.md)
  Tells the delegate from which window it should present content to the user.
- [typealias ASPresentationAnchor](./aspresentationanchor.md)
  A platform-specific type that indicates the kind of user interface element to use as a presentation anchor.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Presenting requests
- [var presentationContextProvider: (any ASAuthorizationControllerPresentationContextProviding)?](./asauthorizationcontroller/presentationcontextprovider.md)
  A delegate that provides a display context in which the system can present an authorization interface to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationcontrollerpresentationcontextproviding)*