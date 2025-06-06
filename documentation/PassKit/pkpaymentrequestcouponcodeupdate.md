# PKPaymentRequestCouponCodeUpdate

**Framework**: Passkit  
**Kind**: class

An object that updates the payment request after the coupon code changes.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class PKPaymentRequestCouponCodeUpdate
```

#### Overview

This is the handler for [`paymentAuthorizationController(_:didChangeCouponCode:handler:)`](pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller(_:didchangecouponcode:handler:).md) and [`paymentAuthorizationViewController(_:didChangeCouponCode:handler:)`](pkpaymentauthorizationviewcontrollerdelegate/paymentauthorizationviewcontroller(_:didchangecouponcode:handler:).md).

Use this object to update the summary items to reflect the change in the coupon code.

> **Note**:  A coupon code error doesn’t block payment authorization.

## Topics

### Creating a payment coupon update object
- [init(errors: [any Error]?, paymentSummaryItems: [PKPaymentSummaryItem], shippingMethods: [PKShippingMethod])](pkpaymentrequestcouponcodeupdate/init(errors:paymentsummaryitems:shippingmethods:).md)
  Creates a payment coupon update with your specified payment summary items, errors, and shipping methods.
### Reading errors
- [var errors: [any Error]!](pkpaymentrequestcouponcodeupdate/errors.md)
  An array of errors for the coupon code that the user must resolve.

## Relationships

### Inherits From
- [PKPaymentRequestUpdate](pkpaymentrequestupdate.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class PKPaymentRequestMerchantSessionUpdate](pkpaymentrequestmerchantsessionupdate.md)
  An object that updates a payment request with a merchant validation.
- [class PKPaymentRequestPaymentMethodUpdate](pkpaymentrequestpaymentmethodupdate.md)
  An object that updates the payment request after the payment method changes.
- [class PKPaymentRequestShippingContactUpdate](pkpaymentrequestshippingcontactupdate.md)
  An object that updates the payment request after the shipping contact information changes.
- [class PKPaymentRequestShippingMethodUpdate](pkpaymentrequestshippingmethodupdate.md)
  An object that updates the payment request after the shipping method changed.
- [class PKPaymentRequestUpdate](pkpaymentrequestupdate.md)
  The base class for updating the payment request after the user makes changes on the payment sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/PassKit/pkpaymentrequestcouponcodeupdate)*