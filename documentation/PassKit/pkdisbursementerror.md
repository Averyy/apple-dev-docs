# PKDisbursementError

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: struct

A structure that describes errors that can occur while processing the disbursement.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
struct PKDisbursementError
```

## Topics

### Initializers
- [init(Code, userInfo: [String : Any])](../passkit_apple_pay_and_wallet/pkdisbursementerror/4156691-init.md)
  Creates a new error structure with the error code and user info you provide.
### Error details
- [PKDisbursementError.Code](pkdisbursementerror/code.md)
  Values that describe errors that can occur while processing the disbursement.
- [var errorCode: Int](../Foundation/CustomNSError/errorCode-2opgi.md)
  The error code within the given domain.
- [var errorUserInfo: [String : Any]](../Foundation/CustomNSError/errorUserInfo-1aas5.md)
  The default user-info dictionary.
- [var hashValue: Int](../passkit_apple_pay_and_wallet/pkdisbursementerror/4156690-hashvalue.md)
  The hash value.
- [var userInfo: [String : Any]](../passkit_apple_pay_and_wallet/pkdisbursementerror/4156696-userinfo.md)
  A dictionary that contains additional details about the error.
### Type properties
- [static var recipientContactInvalidError: PKDisbursementError.Code](pkdisbursementerror/recipientcontactinvaliderror.md)
  A value that indicates the recipient’s contact information is invalid.
- [static var unknownError: PKDisbursementError.Code](pkdisbursementerror/unknownerror.md)
  A value that indicates an unknown error occurred.
- [static var unsupportedCardError: PKDisbursementError.Code](pkdisbursementerror/unsupportedcarderror.md)
  A value that indicates that the framework doesn’t support the card the individual presented for this disbursement.
### Utility methods
- [func hash(into: inout Hasher)](../passkit_apple_pay_and_wallet/pkdisbursementerror/4156689-hash.md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [static func == (PKDisbursementError, PKDisbursementError) -> Bool](../passkit_apple_pay_and_wallet/pkdisbursementerror/4156684.md)
  Returns a Boolean value that indicates whether two values are equal.
### Type Properties
- [static var errorDomain: String](pkdisbursementerror/errordomain.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct PKDisbursementErrorKey](pkdisbursementerrorkey.md)
  Values that describe errors that can occur when processing disbursements.
- [struct PKPaymentError](pkpaymenterror.md)
  An error type that you create to indicate problems with address or contact information on an Apple Pay sheet.
- [PKPaymentError.Code](pkpaymenterror/code.md)
  An error code that you provide to indicate problems with address or contact information on an Apple Pay sheet.
- [struct PKPaymentErrorKey](pkpaymenterrorkey.md)
  Additional details about an error on the Apple Pay sheet.
- [PKDisbursementError.Code](pkdisbursementerror/code.md)
  Values that describe errors that can occur while processing the disbursement.
- [let PKPaymentErrorDomain: String](pkpaymenterrordomain.md)
  The error domain for specific errors associated with Apple Pay in-app or web payments.
- [let PKDisbursementErrorDomain: String](pkdisbursementerrordomain.md)
  The error domain to use for errors with in-app disbursements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkdisbursementerror)*