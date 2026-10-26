# paymentShippingAddressInvalidError(withKey:localizedDescription:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Type Method

Creates a shipping address error with the supplied key and user-facing error message.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class func paymentShippingAddressInvalidError(withKey postalAddressKey: String, localizedDescription: String?) -> any Error
```

```objc
+ (NSError *) paymentShippingAddressInvalidErrorWithKey:(NSString *) postalAddressKey localizedDescription:(NSString *) localizedDescription;
```

#### Discussion

You can use this convenience method to create a payment error object instead of creating an [`NSError`](../../Foundation/nserror.md) object yourself.  This convenience method indicates an error in the shipping address received from an Apple Pay sheet.

The error you provide and its optional message appear on the Apple Pay sheet. The available space to display messages is limited, so you should keep your messages concise.

For example, the following example shows how to create errors for indicating problems with the zip code and street, using the keys [`CNPostalAddressPostalCodeKey`](../../Contacts/cnpostaladdresspostalcodekey.md) and [`CNPostalAddressStreetKey`](../../Contacts/cnpostaladdressstreetkey.md).

Creating custom errors:

**Swift**:

```swift
// Create errors for the zip code and street address
let shippingInvalidZip = PKPaymentRequest.paymentShippingAddressInvalidError(withKey: CNPostalAddressPostalCodeKey,localizedDescription: "Invalid ZIP code")
        let shippingInvalidStreet = PKPaymentRequest.paymentShippingAddressInvalidError(withKey: CNPostalAddressStreetKey,localizedDescription: "Missing street name")
// The result contains both errors       let result = PKPaymentAuthorizationResult(status: .failure, errors: [shippingInvalidZip, shippingInvalidStreet])
```

**Objective-C**:

```objc
// Create errors for the zip code and street address
NSError *shippingInvalidZip = [PKPaymentRequest 
    paymentShippingAddressInvalidErrorWithKey:CNPostalAddressPostalCodeKey 
    localizedDescription:@"Invalid ZIP code"];
 
NSError *shippingInvalidStreet = [PKPaymentRequest    paymentShippingAddressInvalidErrorWithKey:CNPostalAddressStreetKey 
    localizedDescription:@"Missing street name"];

// The result contains both errors
PKPaymentAuthorizationResult *result = [[PKPaymentAuthorizationResult alloc]
    initWithStatus:PKPaymentAuthorizationStatusFailure 
    errors:@[shippingInvalidZip, shippingInvalidStreet]];
```

## Parameters

- `postalAddressKey`: A key value from [`CNPostalAddress`](../../Contacts/cnpostaladdress.md) that indicates which part of the address has an error.
- `localizedDescription`: Optional. Provide a localized, user-facing error message string to help the user resolve the error.

## See Also

### Providing error information
- [class func paymentBillingAddressInvalidError(withKey: String, localizedDescription: String?) -> any Error](./paymentbillingaddressinvaliderror%28withkey,localizeddescription%29.md)
  Creates a billing address error with the supplied key and user-facing error message.
- [class func paymentContactInvalidError(withContactField: PKContactField, localizedDescription: String?) -> any Error](./paymentcontactinvaliderror%28withcontactfield,localizeddescription%29.md)
  Creates a contact error with the supplied field and user-facing error message.
- [class func paymentShippingAddressUnserviceableError(withLocalizedDescription: String?) -> any Error](./paymentshippingaddressunserviceableerror%28withlocalizeddescription%29.md)
  Creates an error for an unserviceable address, with the supplied user-facing error message.
- [static func paymentCouponCodeInvalidError(localizedDescription: String?) -> any Error](./paymentcouponcodeinvaliderror%28localizeddescription%29.md)
  Returns an error object that indicates an invalid coupon.
- [static func paymentCouponCodeExpiredError(localizedDescription: String?) -> any Error](./paymentcouponcodeexpirederror%28localizeddescription%29.md)
  Returns an error object that indicates an expired coupon.
- [+ paymentCouponCodeInvalidErrorWithLocalizedDescription:](./paymentcouponcodeinvaliderrorwithlocalizeddescription_.md)
  Returns an error object that indicates an invalid coupon.
- [+ paymentCouponCodeExpiredErrorWithLocalizedDescription:](./paymentcouponcodeexpirederrorwithlocalizeddescription_.md)
  Returns an error object that indicates an expired coupon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentrequest/paymentshippingaddressinvaliderror(withkey:localizeddescription:))*