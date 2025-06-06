# paymentContactInvalidError(withContactField:localizedDescription:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

Creates a contact error with the supplied field and user-facing error message.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class func paymentContactInvalidError(withContactField field: PKContactField, localizedDescription: String?) -> any Error
```

#### Discussion

You can use this convenience method to create a payment error object instead of creating an [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) object yourself.  This method indicates an error in the contact information that is received from an Apple Pay sheet.

The error you provide and its optional message appear on the Apple Pay sheet. The available space to display messages is limited, so you should keep your messages concise.

## Parameters

- `field`: A value from   that indicates which part of the contact information has an error.
- `localizedDescription`: Optional. Provide a localized, user-facing error message string to help the user resolve the error.

## See Also

- [class func paymentBillingAddressInvalidError(withKey: String, localizedDescription: String?) -> any Error](pkpaymentrequest/paymentbillingaddressinvaliderror(withkey:localizeddescription:).md)
  Creates a billing address error with the supplied key and user-facing error message.
- [class func paymentShippingAddressInvalidError(withKey: String, localizedDescription: String?) -> any Error](pkpaymentrequest/paymentshippingaddressinvaliderror(withkey:localizeddescription:).md)
  Creates a shipping address error with the supplied key and user-facing error message.
- [class func paymentShippingAddressUnserviceableError(withLocalizedDescription: String?) -> any Error](pkpaymentrequest/paymentshippingaddressunserviceableerror(withlocalizeddescription:).md)
  Creates an error for an unserviceable address, with the supplied user-facing error message.
- [static func paymentCouponCodeInvalidError(localizedDescription: String?) -> any Error](pkpaymentrequest/paymentcouponcodeinvaliderror(localizeddescription:).md)
  Returns an error object that indicates an invalid coupon.
- [static func paymentCouponCodeExpiredError(localizedDescription: String?) -> any Error](pkpaymentrequest/paymentcouponcodeexpirederror(localizeddescription:).md)
  Returns an error object that indicates an expired coupon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentrequest/paymentcontactinvaliderror(withcontactfield:localizeddescription:))*