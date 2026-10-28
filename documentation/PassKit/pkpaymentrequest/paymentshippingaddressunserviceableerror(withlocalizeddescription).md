# paymentShippingAddressUnserviceableError(withLocalizedDescription:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Type Method

Creates an error for an unserviceable address, with the supplied user-facing error message.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class func paymentShippingAddressUnserviceableError(withLocalizedDescription localizedDescription: String?) -> any Error
```

```objc
+ (NSError *) paymentShippingAddressUnserviceableErrorWithLocalizedDescription:(NSString *) localizedDescription;
```

## Discussion

You can use this convenience method to create a payment error object instead of creating an [`NSError`](../../Foundation/nserror.md) object yourself.  This method indicates that the address received from the Apple Pay sheet is unserviceable.

The error you provide and its optional message appear on the Apple Pay sheet. The available space to display messages is limited, so you should keep your messages concise.

## Parameters

- `localizedDescription`: Optional. Provide a localized, user-facing error message string to help the user resolve the error.

## See Also

### Providing error information
- [class func paymentBillingAddressInvalidError(withKey: String, localizedDescription: String?) -> any Error](./paymentbillingaddressinvaliderror%28withkey,localizeddescription%29.md)
  Creates a billing address error with the supplied key and user-facing error message.
- [class func paymentContactInvalidError(withContactField: PKContactField, localizedDescription: String?) -> any Error](./paymentcontactinvaliderror%28withcontactfield,localizeddescription%29.md)
  Creates a contact error with the supplied field and user-facing error message.
- [class func paymentShippingAddressInvalidError(withKey: String, localizedDescription: String?) -> any Error](./paymentshippingaddressinvaliderror%28withkey,localizeddescription%29.md)
  Creates a shipping address error with the supplied key and user-facing error message.
- [static func paymentCouponCodeInvalidError(localizedDescription: String?) -> any Error](./paymentcouponcodeinvaliderror%28localizeddescription%29.md)
  Returns an error object that indicates an invalid coupon.
- [static func paymentCouponCodeExpiredError(localizedDescription: String?) -> any Error](./paymentcouponcodeexpirederror%28localizeddescription%29.md)
  Returns an error object that indicates an expired coupon.
- [+ paymentCouponCodeInvalidErrorWithLocalizedDescription:](./paymentcouponcodeinvaliderrorwithlocalizeddescription_.md)
  Returns an error object that indicates an invalid coupon.
- [+ paymentCouponCodeExpiredErrorWithLocalizedDescription:](./paymentcouponcodeexpirederrorwithlocalizeddescription_.md)
  Returns an error object that indicates an expired coupon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentrequest/paymentshippingaddressunserviceableerror(withlocalizeddescription:))*