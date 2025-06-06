# delegate

**Framework**: Authentication Services  
**Kind**: property

An object that receives notifications about the request’s status.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any ASAccountAuthenticationModificationControllerDelegate)? { get set }
```

## See Also

- [var presentationContextProvider: (any ASAccountAuthenticationModificationControllerPresentationContextProviding)?](asaccountauthenticationmodificationcontroller/presentationcontextprovider.md)
  An object that provides a presentation context for the account modification request’s user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asaccountauthenticationmodificationcontroller/delegate)*