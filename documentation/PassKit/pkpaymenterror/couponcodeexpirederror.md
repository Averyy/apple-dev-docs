# couponCodeExpiredError

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

The error code that indicates an expired coupon.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
static var couponCodeExpiredError: PKPaymentError.Code { get }
```

#### Discussion

Use this error code if the user entered an expired coupon code in the payment sheet. You can use [`paymentCouponCodeExpiredError(localizedDescription:)`](pkpaymentrequest/paymentcouponcodeexpirederror(localizeddescription:).md) to create an expired coupon error object.

> **Note**:  A coupon code error doesn’t prevent the user from authorizing the payment.

## See Also

- [static var billingContactInvalidError: PKPaymentError.Code](pkpaymenterror/billingcontactinvaliderror.md)
  The error code to indicate an invalid billing address or billing name.
- [static var shippingContactInvalidError: PKPaymentError.Code](pkpaymenterror/shippingcontactinvaliderror.md)
  The error code to indicate an invalid shipping address, email, phone, or name.
- [static var shippingAddressUnserviceableError: PKPaymentError.Code](pkpaymenterror/shippingaddressunserviceableerror.md)
  The error code for an unserviceable shipping address.
- [static var couponCodeInvalidError: PKPaymentError.Code](pkpaymenterror/couponcodeinvaliderror.md)
  The error code that indicates an invalid coupon.
- [static var unknownError: PKPaymentError.Code](pkpaymenterror/unknownerror.md)
  The error code for an unknown error.
- [PKPaymentError.Code](pkpaymenterror/code.md)
  An error code that you provide to indicate problems with address or contact information on an Apple Pay sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymenterror/couponcodeexpirederror)*