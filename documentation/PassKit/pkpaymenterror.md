# PKPaymentError

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: struct

An error type that you create to indicate problems with address or contact information on an Apple Pay sheet.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
struct PKPaymentError
```

#### Overview

The user must resolve any errors that you report on the Apple Pay sheet before they’re able to authorize the transaction.  You return any errors in [`PKPaymentAuthorizationResult`](pkpaymentauthorizationresult.md) or [`PKPaymentRequestShippingContactUpdate`](pkpaymentrequestshippingcontactupdate.md).

You can build your own payment error ([`NSError`](https://developer.apple.com/documentation/foundation/nserror)), or use one of the following convenience methods from [`PKPaymentRequest`](pkpaymentrequest.md) to build it for you.

- For an error with contact information, use [`paymentContactInvalidError(withContactField:localizedDescription:)`](pkpaymentrequest/paymentcontactinvaliderror(withcontactfield:localizeddescription:).md).
- For a shipping address that is unserviceable, use [`paymentShippingAddressUnserviceableError(withLocalizedDescription:)`](pkpaymentrequest/paymentshippingaddressunserviceableerror(withlocalizeddescription:).md).
- For an error with the billing address, use [`paymentBillingAddressInvalidError(withKey:localizedDescription:)`](pkpaymentrequest/paymentbillingaddressinvaliderror(withkey:localizeddescription:).md).
- For an error with the shipping address, use [`paymentShippingAddressInvalidError(withKey:localizedDescription:)`](pkpaymentrequest/paymentshippingaddressinvaliderror(withkey:localizeddescription:).md).

The following code example shows:

- How to create an error directly.
- How to create an error using a convenience method.

Creating payment errors:

```swift
// A general billing address error created with NSError
let billingAddressError = NSError.init(domain: PKPaymentErrorDomain,
                          code: PKPaymentError.billingContactInvalidError.rawValue,
                          userInfo: [NSLocalizedDescriptionKey:"Address has an error",
                          PKPaymentErrorKey.contactFieldUserInfoKey: PKContactField.postalAddress])

// A specific billing address error created with a convenience method
let billingAddressInvalidStreet = PKPaymentRequest.paymentBillingAddressInvalidError(withKey:CNPostalAddressStreetKey,
                                                   localizedDescription: "Invalid street")
```

## Topics

### Describing the error
- [var errorCode: Int](../foundation/customnserror/errorcode-2opgi.md)
  The error code within the given domain.
- [var errorUserInfo: [String : Any]](../foundation/customnserror/erroruserinfo-1aas5.md)
  The default user-info dictionary.
### Identifying the error
- [static var billingContactInvalidError: PKPaymentError.Code](pkpaymenterror/billingcontactinvaliderror.md)
  The error code to indicate an invalid billing address or billing name.
- [static var shippingContactInvalidError: PKPaymentError.Code](pkpaymenterror/shippingcontactinvaliderror.md)
  The error code to indicate an invalid shipping address, email, phone, or name.
- [static var shippingAddressUnserviceableError: PKPaymentError.Code](pkpaymenterror/shippingaddressunserviceableerror.md)
  The error code for an unserviceable shipping address.
- [static var couponCodeExpiredError: PKPaymentError.Code](pkpaymenterror/couponcodeexpirederror.md)
  The error code that indicates an expired coupon.
- [static var couponCodeInvalidError: PKPaymentError.Code](pkpaymenterror/couponcodeinvaliderror.md)
  The error code that indicates an invalid coupon.
- [static var unknownError: PKPaymentError.Code](pkpaymenterror/unknownerror.md)
  The error code for an unknown error.
- [PKPaymentError.Code](pkpaymenterror/code.md)
  An error code that you provide to indicate problems with address or contact information on an Apple Pay sheet.
### Querying the error domain
- [static var errorDomain: String](pkpaymenterror/errordomain.md)
- [let PKPaymentErrorDomain: String](pkpaymenterrordomain.md)
  The error domain for specific errors associated with Apple Pay in-app or web payments.

## Relationships

### Conforms To
- [CustomNSError](../foundation/customnserror.md)
- [Equatable](../swift/equatable.md)
- [Error](../swift/error.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct PKDisbursementError](pkdisbursementerror.md)
  A structure that describes errors that can occur while processing the disbursement.
- [struct PKDisbursementErrorKey](pkdisbursementerrorkey.md)
  Values that describe errors that can occur when processing disbursements.
- [PKPaymentError.Code](pkpaymenterror/code.md)
  An error code that you provide to indicate problems with address or contact information on an Apple Pay sheet.
- [struct PKPaymentErrorKey](pkpaymenterrorkey.md)
  Additional details about an error on the Apple Pay sheet.
- [PKDisbursementError.Code](pkdisbursementerror/code.md)
  Values that describe errors that can occur while processing the disbursement.
- [let PKPaymentErrorDomain: String](pkpaymenterrordomain.md)
  The error domain for specific errors associated with Apple Pay in-app or web payments.
- [let PKDisbursementErrorDomain: String](pkdisbursementerrordomain.md)
  The error domain to use for errors with in-app disbursements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymenterror)*