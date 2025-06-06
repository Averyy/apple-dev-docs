# PKAddSecureElementPassError.Code.genericError

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: case

Represents the default error case.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS ?+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
case genericError
```

## See Also

- [PKAddSecureElementPassError.Code.deviceNotReadyError](pkaddsecureelementpasserror/code/devicenotreadyerror.md)
  The reader for the pass isn’t ready to start pairing.
- [PKAddSecureElementPassError.Code.deviceNotSupportedError](pkaddsecureelementpasserror/code/devicenotsupportederror.md)
  The reader for the pass isn’t supported or has an invalid version.
- [PKAddSecureElementPassError.Code.invalidConfigurationError](pkaddsecureelementpasserror/code/invalidconfigurationerror.md)
  The configuration for the pass is invalid for either Wallet or the reader.
- [PKAddSecureElementPassError.Code.osVersionNotSupportedError](pkaddsecureelementpasserror/code/osversionnotsupportederror.md)
- [PKAddSecureElementPassError.Code.unavailableError](pkaddsecureelementpasserror/code/unavailableerror.md)
  Provisioning for secure element passes isn’t available on the device, or the app is missing the entitlement.
- [PKAddSecureElementPassError.Code.userCanceledError](pkaddsecureelementpasserror/code/usercancelederror.md)
  The user canceled adding the pass.
- [static var unknownError: PKAddSecureElementPassError.Code](pkaddsecureelementpasserror/code/unknownerror.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddsecureelementpasserror/code/genericerror)*