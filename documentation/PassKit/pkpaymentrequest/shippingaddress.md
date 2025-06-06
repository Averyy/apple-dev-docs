# shippingAddress

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

A prepopulated shipping address.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+

## Declaration

```swift
unowned(unsafe) var shippingAddress: ABRecord? { get set }
```

#### Discussion

If you already have a shipping address on file, set this property to that address. When the [`PKPaymentAuthorizationViewController`](pkpaymentauthorizationviewcontroller.md) class is presented, the user can either keep the address you specified or enter a different address.

## See Also

- [static var enabled: PKShippingContactEditingMode](pkshippingcontacteditingmode/enabled.md)
  All fields of the shipping contact on the payment sheet are editable by the user.
- [var requiredBillingAddressFields: PKAddressField](pkpaymentrequest/requiredbillingaddressfields.md)
  A bit field of billing address fields that you need in order to process the transaction.
- [var requiredShippingAddressFields: PKAddressField](pkpaymentrequest/requiredshippingaddressfields.md)
  A bit field of shipping address fields that you need in order to process the transaction.
- [struct PKAddressField](pkaddressfield.md)
  Billing or shipping address fields.
- [var billingAddress: ABRecord?](pkpaymentrequest/billingaddress.md)
  A prepopulated billing address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentrequest/shippingaddress)*