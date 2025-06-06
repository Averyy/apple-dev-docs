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
- [var code: Code](../passkit_apple_pay_and_wallet/pkidentityerror/3931637-code.md)
  The error code.
- [PKIdentityError.Code](pkidentityerror-swift.struct/code.md)
  Error codes for identity operations.
- [Error constants](error-constants.md)
  Error code constants for identity operations.
- [var errorCode: Int](../passkit_apple_pay_and_wallet/pkidentityerror/3931638-errorcode.md)
  The integer error code.
- [var userInfo: [String : Any]](../passkit_apple_pay_and_wallet/pkidentityerror/3931651-userinfo.md)
  The user information for the error.
- [var errorUserInfo: [String : Any]](../passkit_apple_pay_and_wallet/pkidentityerror/3931640-erroruserinfo.md)
  The error user information dictionary for the error.
### Comparing errors
- [static func == (PKIdentityError, PKIdentityError) -> Bool](../passkit_apple_pay_and_wallet/pkidentityerror/3931635.md)
  Returns a Boolean value that indicates whether two values are equal.
### Accessing the hash value
- [func hash(into: inout Hasher)](../passkit_apple_pay_and_wallet/pkidentityerror/3931641-hash.md)
  Hashes the essential components of the value by passing them into the hasher.
- [var hashValue: Int](../passkit_apple_pay_and_wallet/pkidentityerror/3931642-hashvalue.md)
  The hash value.
### Creating an identity error
- [init(Code, userInfo: [String : Any])](../passkit_apple_pay_and_wallet/pkidentityerror/3931643-init.md)
  Creates an identity error with an error code and user information.
### Type Properties
- [static var errorDomain: String](pkidentityerror-swift.struct/errordomain.md)
- [static var regionNotSupported: PKIdentityError.Code](pkidentityerror-swift.struct/regionnotsupported.md)

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