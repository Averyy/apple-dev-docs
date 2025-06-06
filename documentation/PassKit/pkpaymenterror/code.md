# PKPaymentError.Code

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: enum

An error code that you provide to indicate problems with address or contact information on an Apple Pay sheet.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
enum Code
```

#### Overview

The user must resolve any errors that you report on the Apple Pay sheet before they’re able to authorize the transaction.  You return any errors in [`PKPaymentAuthorizationResult`](pkpaymentauthorizationresult.md) or [`PKPaymentRequestShippingContactUpdate`](pkpaymentrequestshippingcontactupdate.md).

You can build your own payment error ([`NSError`](https://developer.apple.com/documentation/Foundation/NSError)), or use one of the following convenience methods from [`PKPaymentRequest`](pkpaymentrequest.md) to build it for you.

For an error with contact information: [`paymentContactInvalidError(withContactField:localizedDescription:)`](pkpaymentrequest/paymentcontactinvaliderror(withcontactfield:localizeddescription:).md).

For a shipping address that is unserviceable: [`paymentShippingAddressUnserviceableError(withLocalizedDescription:)`](pkpaymentrequest/paymentshippingaddressunserviceableerror(withlocalizeddescription:).md).

For an error with the billing address: [`paymentBillingAddressInvalidError(withKey:localizedDescription:)`](pkpaymentrequest/paymentbillingaddressinvaliderror(withkey:localizeddescription:).md).

For an error with the shipping address: [`paymentShippingAddressInvalidError(withKey:localizedDescription:)`](pkpaymentrequest/paymentshippingaddressinvaliderror(withkey:localizeddescription:).md).

The following code example shows:

- How to create a payment error directly.
- How to create a payment error using a convenience method.

Creating payment errors:

```objc
// Creating a general shipping address error with NSError
NSError *addressError = [[NSError alloc] initWithDomain:PKPaymentErrorDomain
                        code:PKPaymentShippingContactInvalidError
                        userInfo:@{NSLocalizedDescriptionKey: @"Address is invalid",
                        PKPaymentErrorContactFieldUserInfoKey: PKContactFieldPostalAddress}];

// Creating a shipping address error specific to the zip code:
NSError *zipCodeError = [[NSError alloc] initWithDomain:PKPaymentErrorDomain
                        code:PKPaymentShippingContactInvalidError
                        userInfo:@{NSLocalizedDescriptionKey: @"Zip code is invalid", 
                        PKPaymentErrorContactFieldUserInfoKey: PKContactFieldPostalAddress,                      
                        PKPaymentErrorPostalAddressUserInfoKey:CNPostalAddressPostalCodeKey}];

// Creating a billing address error specific to the street with a convenience method
NSError *billingAddressInvalidStreet = [PKPaymentRequest
                             paymentBillingAddressInvalidErrorWithKey:CNPostalAddressStreetKey 
                             localizedDescription:@"Invalid Street"];
```

## Topics

### Error codes
- [PKPaymentError.Code.couponCodeExpiredError](pkpaymenterror/code/couponcodeexpirederror.md)
  The error code that indicates an expired coupon.
- [PKPaymentError.Code.couponCodeInvalidError](pkpaymenterror/code/couponcodeinvaliderror.md)
  The error code that indicates an invalid coupon.
- [PKPaymentError.Code.billingContactInvalidError](pkpaymenterror/code/billingcontactinvaliderror.md)
  The error code that indicates an invalid billing address or billing name.
- [PKPaymentError.Code.shippingContactInvalidError](pkpaymenterror/code/shippingcontactinvaliderror.md)
  The error code that indicates an invalid shipping address, email, phone, or name.
- [PKPaymentError.Code.shippingAddressUnserviceableError](pkpaymenterror/code/shippingaddressunserviceableerror.md)
  The error code that indicates an unserviceable shipping address.
- [PKPaymentError.Code.unknownError](pkpaymenterror/code/unknownerror.md)
  The error code that indicates an unknown error.
### Initializers
- [init?(rawValue: Int)](pkpaymenterror/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct PKDisbursementError](pkdisbursementerror.md)
  A structure that describes errors that can occur while processing the disbursement.
- [struct PKDisbursementErrorKey](pkdisbursementerrorkey.md)
  Values that describe errors that can occur when processing disbursements.
- [struct PKPaymentError](pkpaymenterror.md)
  An error type that you create to indicate problems with address or contact information on an Apple Pay sheet.
- [struct PKPaymentErrorKey](pkpaymenterrorkey.md)
  Additional details about an error on the Apple Pay sheet.
- [PKDisbursementError.Code](pkdisbursementerror/code.md)
  Values that describe errors that can occur while processing the disbursement.
- [let PKPaymentErrorDomain: String](pkpaymenterrordomain.md)
  The error domain for specific errors associated with Apple Pay in-app or web payments.
- [let PKDisbursementErrorDomain: String](pkdisbursementerrordomain.md)
  The error domain to use for errors with in-app disbursements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymenterror/code)*