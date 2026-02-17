# PKPassKitError

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: struct

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
struct PKPassKitError
```

## Topics

### Error information
- [var errorCode: Int](../Foundation/CustomNSError/errorCode-2opgi.md)
  The error code within the given domain.
- [var errorUserInfo: [String : Any]](../Foundation/CustomNSError/errorUserInfo-1aas5.md)
  The default user-info dictionary.
### Error codes
- [static var invalidDataError: PKPassKitError.Code](pkpasskiterror/invaliddataerror.md)
- [static var invalidSignature: PKPassKitError.Code](pkpasskiterror/invalidsignature.md)
- [static var notEntitledError: PKPassKitError.Code](pkpasskiterror/notentitlederror.md)
- [static var unknownError: PKPassKitError.Code](pkpasskiterror/unknownerror.md)
- [static var unsupportedVersionError: PKPassKitError.Code](pkpasskiterror/unsupportedversionerror.md)
- [PKPassKitError.Code](pkpasskiterror/code.md)
  Errors that the PassKit framework uses.
- [enum PKAddPaymentPassError](pkaddpaymentpasserror.md)
  Error codes for adding payment passes.
### Error domain
- [static var errorDomain: String](pkpasskiterror/errordomain.md)
- [let PKPassKitErrorDomain: String](pkpasskiterrordomain.md)
  The error domain for PassKit errors.

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct PKAddSecureElementPassError](pkaddsecureelementpasserror.md)
  An error object that PassKit uses when it adds Secure Element passes.
- [PKPassKitError.Code](pkpasskiterror/code.md)
  Errors that the PassKit framework uses.
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

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpasskiterror)*