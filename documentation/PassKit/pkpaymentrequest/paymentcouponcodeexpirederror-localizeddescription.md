# paymentCouponCodeExpiredError(localizedDescription:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

Returns an error object that indicates an expired coupon.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
static func paymentCouponCodeExpiredError(localizedDescription: String? = nil) -> any Error
```

#### Return Value

A new expired coupon error.

#### Discussion

Use this convenience method to create a payment error object instead of creating an [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) object yourself. This method indicates that the coupon code received from the Apple Pay sheet has expired.

The error you provide and its optional message appear on the Apple Pay sheet. There’s limited available space to display messages, so keep your messages concise.

## Parameters

- `localizedDescription`: A user-readable error as a localized string.

## See Also

- [class func paymentBillingAddressInvalidError(withKey: String, localizedDescription: String?) -> any Error](pkpaymentrequest/paymentbillingaddressinvaliderror(withkey:localizeddescription:).md)
  Creates a billing address error with the supplied key and user-facing error message.
- [class func paymentContactInvalidError(withContactField: PKContactField, localizedDescription: String?) -> any Error](pkpaymentrequest/paymentcontactinvaliderror(withcontactfield:localizeddescription:).md)
  Creates a contact error with the supplied field and user-facing error message.
- [class func paymentShippingAddressInvalidError(withKey: String, localizedDescription: String?) -> any Error](pkpaymentrequest/paymentshippingaddressinvaliderror(withkey:localizeddescription:).md)
  Creates a shipping address error with the supplied key and user-facing error message.
- [class func paymentShippingAddressUnserviceableError(withLocalizedDescription: String?) -> any Error](pkpaymentrequest/paymentshippingaddressunserviceableerror(withlocalizeddescription:).md)
  Creates an error for an unserviceable address, with the supplied user-facing error message.
- [static func paymentCouponCodeInvalidError(localizedDescription: String?) -> any Error](pkpaymentrequest/paymentcouponcodeinvaliderror(localizeddescription:).md)
  Returns an error object that indicates an invalid coupon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentrequest/paymentcouponcodeexpirederror(localizeddescription:))*