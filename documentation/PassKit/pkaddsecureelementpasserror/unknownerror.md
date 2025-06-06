# unknownError

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

An error that occurs when PassKit cancels the addition of a Secure Element pass due to an unknown failure.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS ?+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
static var unknownError: PKAddSecureElementPassError.Code { get }
```

## See Also

- [static var deviceNotReadyError: PKAddSecureElementPassError.Code](pkaddsecureelementpasserror/devicenotreadyerror.md)
  The device isn’t ready to add Secure Element passes.
- [static var deviceNotSupportedError: PKAddSecureElementPassError.Code](pkaddsecureelementpasserror/devicenotsupportederror.md)
  The device doesn’t support adding Secure Element passes.
- [static var invalidConfigurationError: PKAddSecureElementPassError.Code](pkaddsecureelementpasserror/invalidconfigurationerror.md)
  An error that occurs when they system attempts to add a Secure Element pass using an invalid configuration.
- [static var unavailableError: PKAddSecureElementPassError.Code](pkaddsecureelementpasserror/unavailableerror.md)
  PassKit is temporarily unable to add Secure Element passes.
- [static var userCanceledError: PKAddSecureElementPassError.Code](pkaddsecureelementpasserror/usercancelederror.md)
  An error that occurs when the user cancels the addition of a Secure Element pass.
- [PKAddSecureElementPassError.Code](pkaddsecureelementpasserror/code.md)
  Error codes for problems that occur when you add a secure element passes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddsecureelementpasserror/unknownerror)*