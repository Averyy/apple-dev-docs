# PKPaymentError.Code.shippingAddressUnserviceableError

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: case

The error code that indicates an unserviceable shipping address.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
case shippingAddressUnserviceableError
```

#### Discussion

Use this error code for a shipping address that is otherwise valid, but is unserviceable. For example, the address is in a country or region you don’t ship to, or it’s a P.O. box and you can’t deliver to P.O. boxes.

## See Also

- [PKPaymentError.Code.couponCodeExpiredError](pkpaymenterror/code/couponcodeexpirederror.md)
  The error code that indicates an expired coupon.
- [PKPaymentError.Code.couponCodeInvalidError](pkpaymenterror/code/couponcodeinvaliderror.md)
  The error code that indicates an invalid coupon.
- [PKPaymentError.Code.billingContactInvalidError](pkpaymenterror/code/billingcontactinvaliderror.md)
  The error code that indicates an invalid billing address or billing name.
- [PKPaymentError.Code.shippingContactInvalidError](pkpaymenterror/code/shippingcontactinvaliderror.md)
  The error code that indicates an invalid shipping address, email, phone, or name.
- [PKPaymentError.Code.unknownError](pkpaymenterror/code/unknownerror.md)
  The error code that indicates an unknown error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymenterror/code/shippingaddressunserviceableerror)*