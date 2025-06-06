# shippingAddressUnserviceableError

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

The error code for an unserviceable shipping address.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
static var shippingAddressUnserviceableError: PKPaymentError.Code { get }
```

#### Discussion

Use this error code for a shipping address that is otherwise valid, but is unserviceable. For example, the address is in a country or region you don’t ship to, or it’s a P.O. box and you can’t deliver to P.O. boxes.

## See Also

- [static var billingContactInvalidError: PKPaymentError.Code](pkpaymenterror/billingcontactinvaliderror.md)
  The error code to indicate an invalid billing address or billing name.
- [static var shippingContactInvalidError: PKPaymentError.Code](pkpaymenterror/shippingcontactinvaliderror.md)
  The error code to indicate an invalid shipping address, email, phone, or name.
- [static var couponCodeExpiredError: PKPaymentError.Code](pkpaymenterror/couponcodeexpirederror.md)
  The error code that indicates an expired coupon.
- [static var couponCodeInvalidError: PKPaymentError.Code](pkpaymenterror/couponcodeinvaliderror.md)
  The error code that indicates an invalid coupon.
- [static var unknownError: PKPaymentError.Code](pkpaymenterror/unknownerror.md)
  The error code for an unknown error.
- [PKPaymentError.Code](pkpaymenterror/code.md)
  An error code that you provide to indicate problems with address or contact information on an Apple Pay sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymenterror/shippingaddressunserviceableerror)*