# shippingAddress

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

A prepopulated shipping address.

**Availability**:
- iOS 8.0+ - Deprecated in 9.0
- iPadOS 8.0+ - Deprecated in 9.0

> **Deprecated**: This property is deprecated. Use the [`shippingContact`](./shippingcontact.md) property instead.

## Declaration

```swift
unowned(unsafe) var shippingAddress: ABRecord? { get set }
```

```objc
@property (nonatomic, assign, nullable) ABRecordRef shippingAddress;
```

## Discussion

If you already have a shipping address on file, set this property to that address. When the [`PKPaymentAuthorizationViewController`](../pkpaymentauthorizationviewcontroller.md) class is presented, the user can either keep the address you specified or enter a different address.

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
- [var billingAddress: ABRecord?](./billingaddress.md)
  A prepopulated billing address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentrequest/shippingaddress)*