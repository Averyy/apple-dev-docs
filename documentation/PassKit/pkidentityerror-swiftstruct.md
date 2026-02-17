# PKIdentityError

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: struct

A structure that represents an identity error.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct PKIdentityError
```

## Topics

### Inspecting an error
- [static var errorDomain: String](pkidentityerror-swift.struct/errordomain.md)
- [PKIdentityError.Code](pkidentityerror-swift.struct/code.md)
  Error codes for identity operations.
- [Error constants](error-constants.md)
  Error code constants for identity operations.
- [var errorCode: Int](../Foundation/CustomNSError/errorCode-2opgi.md)
  The error code within the given domain.
- [var errorUserInfo: [String : Any]](../Foundation/CustomNSError/errorUserInfo-1aas5.md)
  The default user-info dictionary.
### Type Properties
- [static var regionNotSupported: PKIdentityError.Code](pkidentityerror-swift.struct/regionnotsupported.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct PKPassKitError](pkpasskiterror.md)
  Errors that the PassKit framework uses.
- [struct PKAddSecureElementPassError](pkaddsecureelementpasserror.md)
  An error object that PassKit uses when it adds Secure Element passes.
- [PKPassKitError.Code](pkpasskiterror/code.md)
  Errors that the PassKit framework uses.
- [PKAddSecureElementPassError.Code](pkaddsecureelementpasserror/code.md)
  Error codes for problems that occur when you add a secure element passes.
- [enum PKAddPaymentPassError](pkaddpaymentpasserror.md)
  Error codes for adding payment passes.
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

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkidentityerror-swift.struct)*