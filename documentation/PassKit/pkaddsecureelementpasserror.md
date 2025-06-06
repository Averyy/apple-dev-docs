# PKAddSecureElementPassError

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: struct

An error object that PassKit uses when it adds Secure Element passes.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS ?+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
struct PKAddSecureElementPassError
```

## Topics

### Creating a secure element pass error object
- [init(Code, userInfo: [String : Any])](../passkit_apple_pay_and_wallet/pkaddsecureelementpasserror/3727663-init.md)
  Creates a Secure Element payment pass error object of the specified type with the specified user information.
### Identifying errors
- [static var deviceNotReadyError: PKAddSecureElementPassError.Code](pkaddsecureelementpasserror/devicenotreadyerror.md)
  The device isn’t ready to add Secure Element passes.
- [static var deviceNotSupportedError: PKAddSecureElementPassError.Code](pkaddsecureelementpasserror/devicenotsupportederror.md)
  The device doesn’t support adding Secure Element passes.
- [static var invalidConfigurationError: PKAddSecureElementPassError.Code](pkaddsecureelementpasserror/invalidconfigurationerror.md)
  An error that occurs when they system attempts to add a Secure Element pass using an invalid configuration.
- [static var unavailableError: PKAddSecureElementPassError.Code](pkaddsecureelementpasserror/unavailableerror.md)
  PassKit is temporarily unable to add Secure Element passes.
- [static var unknownError: PKAddSecureElementPassError.Code](pkaddsecureelementpasserror/unknownerror.md)
  An error that occurs when PassKit cancels the addition of a Secure Element pass due to an unknown failure.
- [static var userCanceledError: PKAddSecureElementPassError.Code](pkaddsecureelementpasserror/usercancelederror.md)
  An error that occurs when the user cancels the addition of a Secure Element pass.
- [PKAddSecureElementPassError.Code](pkaddsecureelementpasserror/code.md)
  Error codes for problems that occur when you add a secure element passes.
### Getting error information
- [var code: Code](../passkit_apple_pay_and_wallet/pkaddsecureelementpasserror/3727660-code.md)
  The code that provides context for the error.
- [var errorCode: Int](../passkit_apple_pay_and_wallet/pkaddsecureelementpasserror/3543377-errorcode.md)
  The code that provides context for the error.
- [var userInfo: [String : Any]](../passkit_apple_pay_and_wallet/pkaddsecureelementpasserror/3727664-userinfo.md)
  A dictionary that contains custom information that relates to the error.
- [var errorUserInfo: [String : Any]](../passkit_apple_pay_and_wallet/pkaddsecureelementpasserror/3543379-erroruserinfo.md)
  A dictionary that contains custom information that relates to the error.
- [let PKAddSecureElementPassErrorDomain: String](pkaddsecureelementpasserrordomain.md)
  The error domain for errors that occur when adding a secure pass.
### Comparing errors
- [static func == (PKAddSecureElementPassError, PKAddSecureElementPassError) -> Bool](../passkit_apple_pay_and_wallet/pkaddsecureelementpasserror/3727659.md)
  Returns a Boolean value that indicates whether the two add secure element pass errors are equal.
### Hashing
- [func hash(into: inout Hasher)](../passkit_apple_pay_and_wallet/pkaddsecureelementpasserror/3727661-hash.md)
  Hashes the Secure Element pass error object by feeding the item into the given hasher.
- [var hashValue: Int](../passkit_apple_pay_and_wallet/pkaddsecureelementpasserror/3727662-hashvalue.md)
  The hash value for the Secure Element pass error.
### Type Properties
- [static var errorDomain: String](pkaddsecureelementpasserror/errordomain.md)
- [static var genericError: PKAddSecureElementPassError.Code](pkaddsecureelementpasserror/genericerror.md)
- [static var osVersionNotSupportedError: PKAddSecureElementPassError.Code](pkaddsecureelementpasserror/osversionnotsupportederror.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct PKPassKitError](pkpasskiterror.md)
  Errors that the PassKit framework uses.
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

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddsecureelementpasserror)*