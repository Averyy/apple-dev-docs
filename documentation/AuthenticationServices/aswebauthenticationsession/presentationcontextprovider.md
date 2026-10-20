# presentationContextProvider

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

A delegate that provides a display context in which the system can present an authentication session to the user.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
weak var presentationContextProvider: (any ASWebAuthenticationPresentationContextProviding)? { get set }
```

```objc
@property (nonatomic, weak) id<ASWebAuthenticationPresentationContextProviding> presentationContextProvider;
```

## Mentions

- [Authenticating a User Through a Web Service](../authenticating-a-user-through-a-web-service.md)

## See Also

### Presenting a Session
- [protocol ASWebAuthenticationPresentationContextProviding](../aswebauthenticationpresentationcontextproviding.md)
  An interface the session uses to ask a delegate for a presentation context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aswebauthenticationsession/presentationcontextprovider)*