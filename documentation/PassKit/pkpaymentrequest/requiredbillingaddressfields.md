# requiredBillingAddressFields

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

A bit field of billing address fields that you need in order to process the transaction.

**Availability**:
- iOS 8.0+ - Deprecated in 11.0
- iPadOS 8.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 11.0+
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 4.0

> **Deprecated**: This property is deprecated. Use [`requiredBillingContactFields`](./requiredbillingcontactfields.md) instead.

## Declaration

```swift
var requiredBillingAddressFields: PKAddressField { get set }
```

```objc
@property (nonatomic, assign) PKAddressField requiredBillingAddressFields;
```

## Discussion

The default value is [`PKPaymentRequest`](../pkpaymentrequest.md). For possible values, see [`PKPaymentRequest`](../pkpaymentrequest.md).

## See Also

### Deprecated
- [var applePayLaterAvailability: PKPaymentRequest.ApplePayLaterAvailability](./applepaylateravailability-3dxrt.md)
  A value that indicates whether Apple Pay Later is available for a transaction.
- [static var enabled: PKShippingContactEditingMode](../pkshippingcontacteditingmode/enabled.md)
  All fields of the shipping contact on the payment sheet are editable by the user.
- [var requiredShippingAddressFields: PKAddressField](./requiredshippingaddressfields.md)
  A bit field of shipping address fields that you need in order to process the transaction.
- [struct PKAddressField](../pkaddressfield.md)
  Billing or shipping address fields.
- [var billingAddress: ABRecord?](./billingaddress.md)
  A prepopulated billing address.
- [var shippingAddress: ABRecord?](./shippingaddress.md)
  A prepopulated shipping address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentrequest/requiredbillingaddressfields)*