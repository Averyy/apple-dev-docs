# PKAddSecureElementPassError.Code

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: enum

Error codes for problems that occur when you add a secure element passes.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS ?+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
enum Code
```

## Topics

### Error codes
- [PKAddSecureElementPassError.Code.deviceNotReadyError](pkaddsecureelementpasserror/code/devicenotreadyerror.md)
  The reader for the pass isn’t ready to start pairing.
- [PKAddSecureElementPassError.Code.deviceNotSupportedError](pkaddsecureelementpasserror/code/devicenotsupportederror.md)
  The reader for the pass isn’t supported or has an invalid version.
- [PKAddSecureElementPassError.Code.genericError](pkaddsecureelementpasserror/code/genericerror.md)
  Represents the default error case.
- [PKAddSecureElementPassError.Code.invalidConfigurationError](pkaddsecureelementpasserror/code/invalidconfigurationerror.md)
  The configuration for the pass is invalid for either Wallet or the reader.
- [PKAddSecureElementPassError.Code.osVersionNotSupportedError](pkaddsecureelementpasserror/code/osversionnotsupportederror.md)
- [PKAddSecureElementPassError.Code.unavailableError](pkaddsecureelementpasserror/code/unavailableerror.md)
  Provisioning for secure element passes isn’t available on the device, or the app is missing the entitlement.
- [PKAddSecureElementPassError.Code.userCanceledError](pkaddsecureelementpasserror/code/usercancelederror.md)
  The user canceled adding the pass.
- [static var unknownError: PKAddSecureElementPassError.Code](pkaddsecureelementpasserror/code/unknownerror.md)
### Initializers
- [init?(rawValue: Int)](pkaddsecureelementpasserror/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct PKPassKitError](pkpasskiterror.md)
  Errors that the PassKit framework uses.
- [struct PKAddSecureElementPassError](pkaddsecureelementpasserror.md)
  An error object that PassKit uses when it adds Secure Element passes.
- [PKPassKitError.Code](pkpasskiterror/code.md)
  Errors that the PassKit framework uses.
- [enum PKAddPaymentPassError](pkaddpaymentpasserror.md)
  Error codes for adding payment passes.
- [struct PKIdentityError](pkidentityerror-swift.struct.md)
  A structure that represents an identity error.
- [PKIdentityError.Code](pkidentityerror-swift.struct/code.md)
  Error codes for identity operations.
- [struct PKShareSecureElementPassError](pksharesecureelementpasserror.md)
- [PKShareSecureElementPassError.Code](pksharesecureelementpasserror/code.md)
- [enum PKVehicleConnectionErrorCode](pkvehicleconnectionerrorcode.md)
- [enum PayWithApplePayButtonPaymentAuthorizationPhase](paywithapplepaybuttonpaymentauthorizationphase.md)
- [let PKPassKitErrorDomain: String](pkpasskiterrordomain.md)
  The error domain for PassKit errors.
- [let PKIdentityErrorDomain: String](pkidentityerrordomain.md)
  The error domain for identity errors.
- [let PKAddSecureElementPassErrorDomain: String](pkaddsecureelementpasserrordomain.md)
  The error domain for errors that occur when adding a secure pass.
- [let PKShareSecureElementPassErrorDomain: String](pksharesecureelementpasserrordomain.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddsecureelementpasserror/code)*