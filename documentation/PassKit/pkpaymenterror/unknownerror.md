# unknownError

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Type Property

The error code for an unknown error.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
static var unknownError: PKPaymentError.Code { get }
```

## Discussion

Use this error code if an unknown but non-fatal error occurred during payment processing.  The user can attempt authorization again.

## See Also

### Identifying the error
- [static var billingContactInvalidError: PKPaymentError.Code](./billingcontactinvaliderror.md)
  The error code to indicate an invalid billing address or billing name.
- [static var shippingContactInvalidError: PKPaymentError.Code](./shippingcontactinvaliderror.md)
  The error code to indicate an invalid shipping address, email, phone, or name.
- [static var shippingAddressUnserviceableError: PKPaymentError.Code](./shippingaddressunserviceableerror.md)
  The error code for an unserviceable shipping address.
- [static var couponCodeExpiredError: PKPaymentError.Code](./couponcodeexpirederror.md)
  The error code that indicates an expired coupon.
- [static var couponCodeInvalidError: PKPaymentError.Code](./couponcodeinvaliderror.md)
  The error code that indicates an invalid coupon.
- [PKPaymentError.Code](./code.md)
  An error code that you provide to indicate problems with address or contact information on an Apple Pay sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymenterror/unknownerror)*