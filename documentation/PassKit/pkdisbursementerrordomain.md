# PKDisbursementErrorDomain

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: var

The error domain to use for errors with in-app disbursements.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
let PKDisbursementErrorDomain: String
```

#### Discussion

Use the [`PKDisbursementErrorDomain`](pkdisbursementerrordomain.md) to create your own [`PKDisbursementError`](pkdisbursementerror.md) objects, and return them to indicate problems with a transfer.

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
- [PKDisbursementError.Code](pkdisbursementerror/code.md)
  Values that describe errors that can occur while processing the disbursement.
- [let PKPaymentErrorDomain: String](pkpaymenterrordomain.md)
  The error domain for specific errors associated with Apple Pay in-app or web payments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkdisbursementerrordomain)*