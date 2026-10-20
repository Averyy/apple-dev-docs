# PKIdentityError.Code

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: enum  
**Role**: Enumeration

Error codes for identity operations.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
enum Code
```

```c
enum PKIdentityError : NSInteger;
```

## Topics

### Error codes
- [PKIdentityError.Code.cancelled](./code/cancelled.md)
  An error that indicates the user cancels the presented sheet.
- [PKIdentityError.Code.invalidElement](./code/invalidelement.md)
  An error that indicates an element the app requests isn’t valid.
- [PKIdentityError.Code.invalidNonce](./code/invalidnonce.md)
  An error that indicates the number is too large or unsuitable.
- [PKIdentityError.Code.notSupported](./code/notsupported.md)
  An error that indicates the request originates from a device the framework doesn’t support.
- [PKIdentityError.Code.networkUnavailable](./code/networkunavailable.md)
  An error that indicates a network isn’t available.
- [PKIdentityError.Code.noElementsRequested](./code/noelementsrequested.md)
  An error that indicates the elements aren’t supported.
- [PKIdentityError.Code.requestAlreadyInProgress](./code/requestalreadyinprogress.md)
  An error that indicates a request is already in progress.
- [PKIdentityError.Code.unknown](./code/unknown.md)
  An error that indicates an unknown error.
### Enumeration Cases
- [PKIdentityError.Code.regionNotSupported](./code/regionnotsupported.md)
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Errors
- [struct PKPassKitError](../pkpasskiterror.md)
  Errors that the PassKit framework uses.
- [struct PKAddSecureElementPassError](../pkaddsecureelementpasserror.md)
  An error object that PassKit uses when it adds Secure Element passes.
- [PKPassKitError.Code](../pkpasskiterror/code.md)
  Errors that the PassKit framework uses.
- [PKAddSecureElementPassError.Code](../pkaddsecureelementpasserror/code.md)
  Error codes for problems that occur when you add a secure element passes.
- [enum PKAddPaymentPassError](../pkaddpaymentpasserror.md)
  Error codes for adding payment passes.
- [struct PKIdentityError](../pkidentityerror-swift.struct.md)
  A structure that represents an identity error.
- [struct PKShareSecureElementPassError](../pksharesecureelementpasserror.md)
- [PKShareSecureElementPassError.Code](../pksharesecureelementpasserror/code.md)
- [enum PKVehicleConnectionErrorCode](../pkvehicleconnectionerrorcode.md)
- [enum PayWithApplePayButtonPaymentAuthorizationPhase](../paywithapplepaybuttonpaymentauthorizationphase.md)
- [let PKPassKitErrorDomain: String](../pkpasskiterrordomain.md)
  The error domain for PassKit errors.
- [let PKIdentityErrorDomain: String](../pkidentityerrordomain.md)
  The error domain for identity errors.
- [let PKAddSecureElementPassErrorDomain: String](../pkaddsecureelementpasserrordomain.md)
  The error domain for errors that occur when adding a secure pass.
- [let PKShareSecureElementPassErrorDomain: String](../pksharesecureelementpasserrordomain.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkidentityerror-swift.struct/code)*