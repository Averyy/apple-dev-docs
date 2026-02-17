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

### Error details
- [PKDisbursementError.Code](pkdisbursementerror/code.md)
  Values that describe errors that can occur while processing the disbursement.
- [var errorCode: Int](../Foundation/CustomNSError/errorCode-2opgi.md)
  The error code within the given domain.
- [var errorUserInfo: [String : Any]](../Foundation/CustomNSError/errorUserInfo-1aas5.md)
  The default user-info dictionary.
### Type properties
- [static var errorDomain: String](pkdisbursementerror/errordomain.md)
- [static var recipientContactInvalidError: PKDisbursementError.Code](pkdisbursementerror/recipientcontactinvaliderror.md)
  A value that indicates the recipient’s contact information is invalid.
- [static var unknownError: PKDisbursementError.Code](pkdisbursementerror/unknownerror.md)
  A value that indicates an unknown error occurred.
- [static var unsupportedCardError: PKDisbursementError.Code](pkdisbursementerror/unsupportedcarderror.md)
  A value that indicates that the framework doesn’t support the card the individual presented for this disbursement.

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