# PKPaymentError.Code.couponCodeExpiredError

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: case  
**Role**: Case

The error code that indicates an expired coupon.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
case couponCodeExpiredError
```

```c
PKPaymentCouponCodeExpiredError
```

#### Discussion

Use this error code if the coupon code entered in the payment sheet has expired. You can use [`paymentCouponCodeExpiredError(localizedDescription:)`](../../pkpaymentrequest/paymentcouponcodeexpirederror%28localizeddescription%29.md) to create an expired coupon error object.

## See Also

### Error codes
- [PKPaymentError.Code.couponCodeInvalidError](./couponcodeinvaliderror.md)
  The error code that indicates an invalid coupon.
- [PKPaymentError.Code.billingContactInvalidError](./billingcontactinvaliderror.md)
  The error code that indicates an invalid billing address or billing name.
- [PKPaymentError.Code.shippingContactInvalidError](./shippingcontactinvaliderror.md)
  The error code that indicates an invalid shipping address, email, phone, or name.
- [PKPaymentError.Code.shippingAddressUnserviceableError](./shippingaddressunserviceableerror.md)
  The error code that indicates an unserviceable shipping address.
- [PKPaymentError.Code.unknownError](./unknownerror.md)
  The error code that indicates an unknown error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymenterror/code/couponcodeexpirederror)*