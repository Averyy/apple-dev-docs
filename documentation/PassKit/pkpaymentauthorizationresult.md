# PKPaymentAuthorizationResult

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

An object that reports the status code and errors for a payment authorization request.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class PKPaymentAuthorizationResult
```

#### Overview

If the Apple Pay sheet contains errors, you provide a [`PKPaymentAuthorizationStatus.failure`](pkpaymentauthorizationstatus/failure.md) status to [`PKPaymentAuthorizationResult`](pkpaymentauthorizationresult.md), and include the errors in the errors array. If there are no errors, you provide a [`PKPaymentAuthorizationStatus.success`](pkpaymentauthorizationstatus/success.md) status and leave the error array empty.

The following code example shows a failure result with two errors in the postal code and street fields.

A result that reports two errors:

```swift
// Error in postal code field.
let shippingInvalidZip =
PKPaymentRequest.paymentShippingAddressInvalidError(withKey:CNPostalAddressPostalCodeKey,
                                                    localizedDescription: "Invalid ZIP code")
// Error in street address field.
let shippingInvalidStreet = PKPaymentRequest.paymentShippingAddressInvalidError(withKey:CNPostalAddressStreetKey,
                                                    localizedDescription: "Missing street name")
// Result with failure status and errors.
let result = PKPaymentAuthorizationResult(status: .failure, 
                                          errors: [shippingInvalidZip, shippingInvalidStreet])
```

## Topics

### Initializing a payment authorization result
- [init(status: PKPaymentAuthorizationStatus, errors: [any Error]?)](pkpaymentauthorizationresult/init(status:errors:).md)
  Initializes the result with the status code and list of errors.
### Setting order details
- [var orderDetails: PKPaymentOrderDetails?](pkpaymentauthorizationresult/orderdetails.md)
  Optional metadata with order details for the placed order.
- [class PKPaymentOrderDetails](pkpaymentorderdetails.md)
  Optional metadata with payment order details for the placed order.
### Setting payment authorization status and errors
- [var errors: [any Error]!](pkpaymentauthorizationresult/errors.md)
  List of errors in the Apple Pay sheet.
- [var status: PKPaymentAuthorizationStatus](pkpaymentauthorizationresult/status.md)
  Payment authorization general status.
- [enum PKPaymentAuthorizationStatus](pkpaymentauthorizationstatus.md)
  General success and failure status for payment authorization.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class PKPaymentOrderDetails](pkpaymentorderdetails.md)
  Optional metadata with payment order details for the placed order.
- [class PKPaymentAuthorizationController](pkpaymentauthorizationcontroller.md)
  An object that presents a sheet that prompts the user to authorize a payment request.
- [class PKPaymentAuthorizationViewController](pkpaymentauthorizationviewcontroller.md)
  An object that presents a sheet that prompts the user to authorize a payment request.
- [class PKPayment](pkpayment.md)
  Represents the result of authorizing a payment request and contains payment information, encrypted in the payment token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationresult)*