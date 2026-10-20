# delegate

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

A delegate that the authorization controller informs about the success or failure of an authorization attempt.

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
weak var delegate: (any ASAuthorizationControllerDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<ASAuthorizationControllerDelegate> delegate;
```

## See Also

### Responding to request completion
- [func authorizationController(ASAuthorizationController, didCompleteWithCustomMethod: ASAuthorizationCustomMethod)](../asauthorizationcontrollerdelegate/authorizationcontroller%28_,didcompletewithcustommethod%29.md)
  Informs the delegate when authorization completes, and specifies the custom method the user selected.
- [protocol ASAuthorizationControllerDelegate](../asauthorizationcontrollerdelegate.md)
  An interface for providing information about the outcome of an authorization request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationcontroller/delegate)*