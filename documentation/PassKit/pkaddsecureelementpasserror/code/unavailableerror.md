# PKAddSecureElementPassError.Code.unavailableError

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: case  
**Role**: Case

Provisioning for secure element passes isn’t available on the device, or the app is missing the entitlement.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
case unavailableError
```

```c
PKAddSecureElementPassUnavailableError
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
- [PKAddSecureElementPassError.Code.userCanceledError](./usercancelederror.md)
  The user canceled adding the pass.
- [static var unknownError: PKAddSecureElementPassError.Code](./unknownerror.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddsecureelementpasserror/code/unavailableerror)*