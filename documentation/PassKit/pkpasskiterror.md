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

### Creating a pass error object
- [init(Code, userInfo: [String : Any])](../passkit_apple_pay_and_wallet/pkpasskiterror/3727669-init.md)
  Creates a pass error object of the specified type with the specified user information.
### Error information
- [var code: Code](../passkit_apple_pay_and_wallet/pkpasskiterror/3727666-code.md)
  The code that provides context for the error.
- [var errorCode: Int](../passkit_apple_pay_and_wallet/pkpasskiterror/2887005-errorcode.md)
  The code that provides context for the error.
- [var userInfo: [String : Any]](../passkit_apple_pay_and_wallet/pkpasskiterror/3727670-userinfo.md)
  A dictionary that contains custom information that relates to the error.
- [var errorUserInfo: [String : Any]](../passkit_apple_pay_and_wallet/pkpasskiterror/2887007-erroruserinfo.md)
  A dictionary that contains custom information that relates to the error.
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
- [let PKPassKitErrorDomain: String](pkpasskiterrordomain.md)
  The error domain for PassKit errors.
### Comparison operator
- [static func == (PKPassKitError, PKPassKitError) -> Bool](../passkit_apple_pay_and_wallet/pkpasskiterror/3727665.md)
  Returns a Boolean value indicating whether two pass error objects are equal.
### Hashing
- [func hash(into: inout Hasher)](../passkit_apple_pay_and_wallet/pkpasskiterror/3727667-hash.md)
  Hashes the pass error object by feeding the item into the given hasher.
- [var hashValue: Int](../passkit_apple_pay_and_wallet/pkpasskiterror/3727668-hashvalue.md)
  The hash value for the Secure Element pass error.
### Type Properties
- [static var errorDomain: String](pkpasskiterror/errordomain.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

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