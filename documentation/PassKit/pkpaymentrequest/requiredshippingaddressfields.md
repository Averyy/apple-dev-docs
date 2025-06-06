# requiredShippingAddressFields

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

A bit field of shipping address fields that you need in order to process the transaction.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var requiredShippingAddressFields: PKAddressField { get set }
```

#### Discussion

The default value is [`PKPaymentRequest`](pkpaymentrequest.md). For possible values, see [`PKPaymentRequest`](pkpaymentrequest.md).

## See Also

- [static var enabled: PKShippingContactEditingMode](pkshippingcontacteditingmode/enabled.md)
  All fields of the shipping contact on the payment sheet are editable by the user.
- [var requiredBillingAddressFields: PKAddressField](pkpaymentrequest/requiredbillingaddressfields.md)
  A bit field of billing address fields that you need in order to process the transaction.
- [struct PKAddressField](pkaddressfield.md)
  Billing or shipping address fields.
- [var billingAddress: ABRecord?](pkpaymentrequest/billingaddress.md)
  A prepopulated billing address.
- [var shippingAddress: ABRecord?](pkpaymentrequest/shippingaddress.md)
  A prepopulated shipping address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentrequest/requiredshippingaddressfields)*