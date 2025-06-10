# PKDisbursementErrorKey

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: struct

Values that describe errors that can occur when processing disbursements.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct PKDisbursementErrorKey
```

## Topics

### Initializers
- [init(rawValue: String)](pkdisbursementerrorkey/init(rawvalue:).md)
  Create a new disbursement error key with the provided value.
### Type properties
- [static let contactFieldUserInfoKey: PKDisbursementErrorKey](pkdisbursementerrorkey/contactfielduserinfokey.md)
  The contact field the error relates to.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct PKDisbursementError](pkdisbursementerror.md)
  A structure that describes errors that can occur while processing the disbursement.
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

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkdisbursementerrorkey)*