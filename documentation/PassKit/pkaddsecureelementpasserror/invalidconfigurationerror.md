# invalidConfigurationError

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Type Property

An error that occurs when they system attempts to add a Secure Element pass using an invalid configuration.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
static var invalidConfigurationError: PKAddSecureElementPassError.Code { get }
```

#### Discussion

Before you attempt to add a Secure Element pass, validate its configuration using the [`canAddSecureElementPass(configuration:)`](../pkaddsecureelementpassviewcontroller/canaddsecureelementpass%28configuration%29.md) method.

## See Also

### Identifying errors
- [static var deviceNotReadyError: PKAddSecureElementPassError.Code](./devicenotreadyerror.md)
  The device isn’t ready to add Secure Element passes.
- [static var deviceNotSupportedError: PKAddSecureElementPassError.Code](./devicenotsupportederror.md)
  The device doesn’t support adding Secure Element passes.
- [static var unavailableError: PKAddSecureElementPassError.Code](./unavailableerror.md)
  PassKit is temporarily unable to add Secure Element passes.
- [static var unknownError: PKAddSecureElementPassError.Code](./unknownerror.md)
  An error that occurs when PassKit cancels the addition of a Secure Element pass due to an unknown failure.
- [static var userCanceledError: PKAddSecureElementPassError.Code](./usercancelederror.md)
  An error that occurs when the user cancels the addition of a Secure Element pass.
- [PKAddSecureElementPassError.Code](./code.md)
  Error codes for problems that occur when you add a secure element passes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddsecureelementpasserror/invalidconfigurationerror)*