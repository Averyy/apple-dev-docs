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

You can build your own payment error ([`NSError`](https://developer.apple.com/documentation/Foundation/NSError)), or use one of the following convenience methods from [`PKPaymentRequest`](pkpaymentrequest.md) to build it for you.

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

### Creating a payment error object
- [init(Code, userInfo: [String : Any])](../passkit_apple_pay_and_wallet/pkpaymenterror/3727675-init.md)
  Creates a payment error object of the specified type with the specified user information.
### Describing the error
- [var errorCode: Int](../Foundation/CustomNSError/errorCode-2opgi.md)
  The error code within the given domain.
- [var userInfo: [String : Any]](../passkit_apple_pay_and_wallet/pkpaymenterror/3727676-userinfo.md)
  Additional details about the error.
- [var errorUserInfo: [String : Any]](../Foundation/CustomNSError/errorUserInfo-1aas5.md)
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
- [let PKPaymentErrorDomain: String](pkpaymenterrordomain.md)
  The error domain for specific errors associated with Apple Pay in-app or web payments.
### Comparing errors
- [static func == (PKPaymentError, PKPaymentError) -> Bool](../passkit_apple_pay_and_wallet/pkpaymenterror/3727671.md)
  Returns a Boolean value indicating whether two payment error objects are equal.
### Hashing
- [func hash(into: inout Hasher)](../passkit_apple_pay_and_wallet/pkpaymenterror/3727673-hash.md)
  Hashes the payment error object by feeding the item into the given hasher.
- [var hashValue: Int](../passkit_apple_pay_and_wallet/pkpaymenterror/3727674-hashvalue.md)
  The hash value for the payment error.
### Type Properties
- [static var errorDomain: String](pkpaymenterror/errordomain.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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