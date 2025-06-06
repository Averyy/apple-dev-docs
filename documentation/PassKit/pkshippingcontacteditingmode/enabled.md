# enabled

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

All fields of the shipping contact on the payment sheet are editable by the user.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 8.0+
- Unknown ?+ - Deprecated

## Declaration

```swift
static var enabled: PKShippingContactEditingMode { get }
```

## See Also

- [var requiredBillingAddressFields: PKAddressField](pkpaymentrequest/requiredbillingaddressfields.md)
  A bit field of billing address fields that you need in order to process the transaction.
- [var requiredShippingAddressFields: PKAddressField](pkpaymentrequest/requiredshippingaddressfields.md)
  A bit field of shipping address fields that you need in order to process the transaction.
- [struct PKAddressField](pkaddressfield.md)
  Billing or shipping address fields.
- [var billingAddress: ABRecord?](pkpaymentrequest/billingaddress.md)
  A prepopulated billing address.
- [var shippingAddress: ABRecord?](pkpaymentrequest/shippingaddress.md)
  A prepopulated shipping address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkshippingcontacteditingmode/enabled)*