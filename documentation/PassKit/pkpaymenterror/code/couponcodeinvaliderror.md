# PKPaymentError.Code.couponCodeInvalidError

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: case

The error code that indicates an invalid coupon.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
case couponCodeInvalidError
```

#### Discussion

Use this error code if the coupon code entered in the payment sheet is invalid. You can use [`paymentCouponCodeInvalidError(localizedDescription:)`](pkpaymentrequest/paymentcouponcodeinvaliderror(localizeddescription:).md) to create an expired coupon error object.

## See Also

- [PKPaymentError.Code.couponCodeExpiredError](pkpaymenterror/code/couponcodeexpirederror.md)
  The error code that indicates an expired coupon.
- [PKPaymentError.Code.billingContactInvalidError](pkpaymenterror/code/billingcontactinvaliderror.md)
  The error code that indicates an invalid billing address or billing name.
- [PKPaymentError.Code.shippingContactInvalidError](pkpaymenterror/code/shippingcontactinvaliderror.md)
  The error code that indicates an invalid shipping address, email, phone, or name.
- [PKPaymentError.Code.shippingAddressUnserviceableError](pkpaymenterror/code/shippingaddressunserviceableerror.md)
  The error code that indicates an unserviceable shipping address.
- [PKPaymentError.Code.unknownError](pkpaymenterror/code/unknownerror.md)
  The error code that indicates an unknown error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymenterror/code/couponcodeinvaliderror)*