# PKDisbursementError.Code

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: enum

Values that describe errors that can occur while processing the disbursement.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
enum Code
```

## Topics

### Error codes
- [PKDisbursementError.Code.recipientContactInvalidError](pkdisbursementerror/code/recipientcontactinvaliderror.md)
  The recipient’s contact information wasn’t valid.
- [PKDisbursementError.Code.unsupportedCardError](pkdisbursementerror/code/unsupportedcarderror.md)
  The framework doesn’t support the card the individual presented.
- [PKDisbursementError.Code.unknownError](pkdisbursementerror/code/unknownerror.md)
  An unknown error occurred.
### Initializers
- [init?(rawValue: Int)](pkdisbursementerror/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct PKDisbursementError](pkdisbursementerror.md)
  A structure that describes errors that can occur while processing the disbursement.
- [struct PKDisbursementErrorKey](pkdisbursementerrorkey.md)
  Values that describe errors that can occur when processing disbursements.
- [struct PKPaymentError](pkpaymenterror.md)
  An error type that you create to indicate problems with address or contact information on an Apple Pay sheet.
- [PKPaymentError.Code](pkpaymenterror/code.md)
  An error code that you provide to indicate problems with address or contact information on an Apple Pay sheet.
- [struct PKPaymentErrorKey](pkpaymenterrorkey.md)
  Additional details about an error on the Apple Pay sheet.
- [let PKPaymentErrorDomain: String](pkpaymenterrordomain.md)
  The error domain for specific errors associated with Apple Pay in-app or web payments.
- [let PKDisbursementErrorDomain: String](pkdisbursementerrordomain.md)
  The error domain to use for errors with in-app disbursements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkdisbursementerror/code)*