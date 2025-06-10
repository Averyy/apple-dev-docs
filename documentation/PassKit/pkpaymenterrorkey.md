# PKPaymentErrorKey

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: struct

Additional details about an error on the Apple Pay sheet.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct PKPaymentErrorKey
```

#### Discussion

Use payment error keys if you are creating a payment error without using one of the convenience methods in [`PKPaymentRequest`](pkpaymentrequest.md) (such as [`paymentBillingAddressInvalidError(withKey:localizedDescription:)`](pkpaymentrequest/paymentbillingaddressinvaliderror(withkey:localizeddescription:).md) or others).

The payment error keys indicate a specific field that has an error, for example, the street field of an address.

## Topics

### Initializing a payment error key
- [init(rawValue: String)](pkpaymenterrorkey/init(rawvalue:).md)
  Create an error key given the raw value.
### Error keys
- [static let postalAddressUserInfoKey: PKPaymentErrorKey](pkpaymenterrorkey/postaladdressuserinfokey.md)
  Payment error key that indicates errors with the postal address.
- [static let contactFieldUserInfoKey: PKPaymentErrorKey](pkpaymenterrorkey/contactfielduserinfokey.md)
  Payment error key that indicates errors with the contact information.

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
- [struct PKDisbursementErrorKey](pkdisbursementerrorkey.md)
  Values that describe errors that can occur when processing disbursements.
- [struct PKPaymentError](pkpaymenterror.md)
  An error type that you create to indicate problems with address or contact information on an Apple Pay sheet.
- [PKPaymentError.Code](pkpaymenterror/code.md)
  An error code that you provide to indicate problems with address or contact information on an Apple Pay sheet.
- [PKDisbursementError.Code](pkdisbursementerror/code.md)
  Values that describe errors that can occur while processing the disbursement.
- [let PKPaymentErrorDomain: String](pkpaymenterrordomain.md)
  The error domain for specific errors associated with Apple Pay in-app or web payments.
- [let PKDisbursementErrorDomain: String](pkdisbursementerrordomain.md)
  The error domain to use for errors with in-app disbursements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymenterrorkey)*