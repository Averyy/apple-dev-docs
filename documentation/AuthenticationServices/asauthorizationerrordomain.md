# ASAuthorizationErrorDomain

**Framework**: Authentication Services  
**Kind**: var  
**Role**: Global Variable

The domain of authorization errors.

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
let ASAuthorizationErrorDomain: String
```

```c
extern NSErrorDomain const ASAuthorizationErrorDomain;
```

## See Also

### Handling Authorization Errors
- [func authorizationController(controller: ASAuthorizationController, didCompleteWithError: any Error)](./asauthorizationcontrollerdelegate/authorizationcontroller%28controller,didcompletewitherror%29.md)
  Tells the delegate when authorization fails, and provides an error explaining why.
- [struct ASAuthorizationError](./asauthorizationerror-swift.struct.md)
  Errors that can occur during authorization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationerrordomain)*