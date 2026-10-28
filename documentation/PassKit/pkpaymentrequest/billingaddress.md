# billingAddress

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

A prepopulated billing address.

**Availability**:
- iOS 8.0+ - Deprecated in 9.0
- iPadOS 8.0+ - Deprecated in 9.0

> **Deprecated**: This property is deprecated. Use the [`billingContact`](./billingcontact.md) property instead.

## Declaration

```swift
unowned(unsafe) var billingAddress: ABRecord? { get set }
```

```objc
@property (nonatomic, assign, nullable) ABRecordRef billingAddress;
```

## Discussion

If you already have a billing address on file, set it here. The user can either use the address you specify or select a different address.

## See Also

### Deprecated
- [var applePayLaterAvailability: PKPaymentRequest.ApplePayLaterAvailability](./applepaylateravailability-3dxrt.md)
  A value that indicates whether Apple Pay Later is available for a transaction.
- [static var enabled: PKShippingContactEditingMode](../pkshippingcontacteditingmode/enabled.md)
  All fields of the shipping contact on the payment sheet are editable by the user.
- [var requiredBillingAddressFields: PKAddressField](./requiredbillingaddressfields.md)
  A bit field of billing address fields that you need in order to process the transaction.
- [var requiredShippingAddressFields: PKAddressField](./requiredshippingaddressfields.md)
  A bit field of shipping address fields that you need in order to process the transaction.
- [struct PKAddressField](../pkaddressfield.md)
  Billing or shipping address fields.
- [var shippingAddress: ABRecord?](./shippingaddress.md)
  A prepopulated shipping address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentrequest/billingaddress)*