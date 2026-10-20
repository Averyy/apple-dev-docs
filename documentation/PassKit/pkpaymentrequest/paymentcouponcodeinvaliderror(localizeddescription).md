# paymentCouponCodeInvalidError(localizedDescription:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Type Method

Returns an error object that indicates an invalid coupon.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS

## Declaration

```swift
static func paymentCouponCodeInvalidError(localizedDescription: String? = nil) -> any Error
```

#### Return Value

A new invalid coupon error.

#### Discussion

Use this convenience method to create a payment error object instead of creating an [`NSError`](../../Foundation/nserror.md) object yourself. This method indicates that the coupon code received from the Apple Pay sheet is invalid.

The error you provide and its optional message appear on the Apple Pay sheet. There’s limited available space to display messages, so keep your messages concise.

## Parameters

- `localizedDescription`: A user-readable error as a localized string.

## See Also

### Providing error information
- [class func paymentBillingAddressInvalidError(withKey: String, localizedDescription: String?) -> any Error](./paymentbillingaddressinvaliderror%28withkey,localizeddescription%29.md)
  Creates a billing address error with the supplied key and user-facing error message.
- [class func paymentContactInvalidError(withContactField: PKContactField, localizedDescription: String?) -> any Error](./paymentcontactinvaliderror%28withcontactfield,localizeddescription%29.md)
  Creates a contact error with the supplied field and user-facing error message.
- [class func paymentShippingAddressInvalidError(withKey: String, localizedDescription: String?) -> any Error](./paymentshippingaddressinvaliderror%28withkey,localizeddescription%29.md)
  Creates a shipping address error with the supplied key and user-facing error message.
- [class func paymentShippingAddressUnserviceableError(withLocalizedDescription: String?) -> any Error](./paymentshippingaddressunserviceableerror%28withlocalizeddescription%29.md)
  Creates an error for an unserviceable address, with the supplied user-facing error message.
- [static func paymentCouponCodeExpiredError(localizedDescription: String?) -> any Error](./paymentcouponcodeexpirederror%28localizeddescription%29.md)
  Returns an error object that indicates an expired coupon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentrequest/paymentcouponcodeinvaliderror(localizeddescription:))*