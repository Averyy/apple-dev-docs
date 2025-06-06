# presentationContextProvider

**Framework**: Authentication Services  
**Kind**: property

A delegate that provides a display context in which the system can present an authorization interface to the user.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
weak var presentationContextProvider: (any ASAuthorizationControllerPresentationContextProviding)? { get set }
```

## See Also

- [protocol ASAuthorizationControllerPresentationContextProviding](asauthorizationcontrollerpresentationcontextproviding.md)
  An interface the controller uses to ask a delegate for a presentation context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationcontroller/presentationcontextprovider)*