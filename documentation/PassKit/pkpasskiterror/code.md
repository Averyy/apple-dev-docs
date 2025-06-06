# PKPassKitError.Code

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: enum

Errors that the PassKit framework uses.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
enum Code
```

## Topics

### Error codes
- [PKPassKitError.Code.unknownError](pkpasskiterror/code/unknownerror.md)
  Unknown error.
- [PKPassKitError.Code.invalidDataError](pkpasskiterror/code/invaliddataerror.md)
  Invalid pass data.
- [PKPassKitError.Code.unsupportedVersionError](pkpasskiterror/code/unsupportedversionerror.md)
  Unsupported pass version.
- [PKPassKitError.Code.invalidSignature](pkpasskiterror/code/invalidsignature.md)
  Invalid pass signature.
- [PKPassKitError.Code.notEntitledError](pkpasskiterror/code/notentitlederror.md)
  Error caused by absence of the required entitlements for the given operation.
### Initializers
- [init?(rawValue: Int)](pkpasskiterror/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct PKPassKitError](pkpasskiterror.md)
  Errors that the PassKit framework uses.
- [struct PKAddSecureElementPassError](pkaddsecureelementpasserror.md)
  An error object that PassKit uses when it adds Secure Element passes.
- [PKAddSecureElementPassError.Code](pkaddsecureelementpasserror/code.md)
  Error codes for problems that occur when you add a secure element passes.
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

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasskiterror/code)*