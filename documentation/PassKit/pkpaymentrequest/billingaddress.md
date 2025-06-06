# billingAddress

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

A prepopulated billing address.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+

## Declaration

```swift
unowned(unsafe) var billingAddress: ABRecord? { get set }
```

#### Discussion

If you already have a billing address on file, set it here. The user can either use the address you specify or select a different address.

## See Also

- [static var enabled: PKShippingContactEditingMode](pkshippingcontacteditingmode/enabled.md)
  All fields of the shipping contact on the payment sheet are editable by the user.
- [var requiredBillingAddressFields: PKAddressField](pkpaymentrequest/requiredbillingaddressfields.md)
  A bit field of billing address fields that you need in order to process the transaction.
- [var requiredShippingAddressFields: PKAddressField](pkpaymentrequest/requiredshippingaddressfields.md)
  A bit field of shipping address fields that you need in order to process the transaction.
- [struct PKAddressField](pkaddressfield.md)
  Billing or shipping address fields.
- [var shippingAddress: ABRecord?](pkpaymentrequest/shippingaddress.md)
  A prepopulated shipping address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentrequest/billingaddress)*