# PKPaymentError.Code.unknownError

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: case

The error code that indicates an unknown error.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
case unknownError
```

#### Discussion

User this error code if an unknown but non-fatal error occurred during payment processing.  The user can attempt to authorize the transaction again.

## See Also

- [PKPaymentError.Code.couponCodeExpiredError](pkpaymenterror/code/couponcodeexpirederror.md)
  The error code that indicates an expired coupon.
- [PKPaymentError.Code.couponCodeInvalidError](pkpaymenterror/code/couponcodeinvaliderror.md)
  The error code that indicates an invalid coupon.
- [PKPaymentError.Code.billingContactInvalidError](pkpaymenterror/code/billingcontactinvaliderror.md)
  The error code that indicates an invalid billing address or billing name.
- [PKPaymentError.Code.shippingContactInvalidError](pkpaymenterror/code/shippingcontactinvaliderror.md)
  The error code that indicates an invalid shipping address, email, phone, or name.
- [PKPaymentError.Code.shippingAddressUnserviceableError](pkpaymenterror/code/shippingaddressunserviceableerror.md)
  The error code that indicates an unserviceable shipping address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymenterror/code/unknownerror)*