# unknownError

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Type Property

**Availability**:
- iOS 13.4+ - Deprecated in 18.0
- iPadOS 13.4+ - Deprecated in 18.0
- Mac Catalyst 13.4+ - Deprecated in 18.0
- macOS
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: Use PKAddSecureElementPassGenericError instead.

## Declaration

```swift
static var unknownError: PKAddSecureElementPassError.Code { get }
```

## See Also

### Error codes
- [PKAddSecureElementPassError.Code.deviceNotReadyError](./devicenotreadyerror.md)
  The reader for the pass isn’t ready to start pairing.
- [PKAddSecureElementPassError.Code.deviceNotSupportedError](./devicenotsupportederror.md)
  The reader for the pass isn’t supported or has an invalid version.
- [PKAddSecureElementPassError.Code.genericError](./genericerror.md)
  Represents the default error case.
- [PKAddSecureElementPassError.Code.invalidConfigurationError](./invalidconfigurationerror.md)
  The configuration for the pass is invalid for either Wallet or the reader.
- [PKAddSecureElementPassError.Code.osVersionNotSupportedError](./osversionnotsupportederror.md)
- [PKAddSecureElementPassError.Code.unavailableError](./unavailableerror.md)
  Provisioning for secure element passes isn’t available on the device, or the app is missing the entitlement.
- [PKAddSecureElementPassError.Code.userCanceledError](./usercancelederror.md)
  The user canceled adding the pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddsecureelementpasserror/code/unknownerror)*