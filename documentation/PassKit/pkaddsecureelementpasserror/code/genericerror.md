# PKAddSecureElementPassError.Code.genericError

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: case  
**Role**: Case

Represents the default error case.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
case genericError
```

```c
PKAddSecureElementPassGenericError
```

## See Also

### Error codes
- [PKAddSecureElementPassError.Code.deviceNotReadyError](./devicenotreadyerror.md)
  The reader for the pass isn’t ready to start pairing.
- [PKAddSecureElementPassError.Code.deviceNotSupportedError](./devicenotsupportederror.md)
  The reader for the pass isn’t supported or has an invalid version.
- [PKAddSecureElementPassError.Code.invalidConfigurationError](./invalidconfigurationerror.md)
  The configuration for the pass is invalid for either Wallet or the reader.
- [PKAddSecureElementPassError.Code.osVersionNotSupportedError](./osversionnotsupportederror.md)
- [PKAddSecureElementPassError.Code.unavailableError](./unavailableerror.md)
  Provisioning for secure element passes isn’t available on the device, or the app is missing the entitlement.
- [PKAddSecureElementPassError.Code.userCanceledError](./usercancelederror.md)
  The user canceled adding the pass.
- [static var unknownError: PKAddSecureElementPassError.Code](./unknownerror.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddsecureelementpasserror/code/genericerror)*