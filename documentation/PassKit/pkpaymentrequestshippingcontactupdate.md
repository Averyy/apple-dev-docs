# PKPaymentRequestShippingContactUpdate

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

An object that updates the payment request after the shipping contact information changes.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class PKPaymentRequestShippingContactUpdate
```

#### Overview

This is the handler for [`paymentAuthorizationController(_:didSelectShippingContact:handler:)`](pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller(_:didselectshippingcontact:handler:).md) and [`paymentAuthorizationViewController(_:didSelectShippingContact:handler:)`](pkpaymentauthorizationviewcontrollerdelegate/paymentauthorizationviewcontroller(_:didselectshippingcontact:handler:).md).

Use this object to update the available shipping methods and, if the user has selected a shipping method, the current shipping cost.

## Topics

### Creating a shipping contact update
- [init(errors: [any Error]?, paymentSummaryItems: [PKPaymentSummaryItem], shippingMethods: [PKShippingMethod])](pkpaymentrequestshippingcontactupdate/init(errors:paymentsummaryitems:shippingmethods:).md)
  Creates a shipping contact update with your specified payment summary items and shipping methods.
### Updating user errors and shipping methods
- [var errors: [any Error]!](pkpaymentrequestshippingcontactupdate/errors.md)
  An array of shipping contact information errors that the user must resolve.
- [var shippingMethods: [PKShippingMethod]](pkpaymentrequestshippingcontactupdate/shippingmethods.md)
  An array of shipping methods.

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
- [class PKPaymentRequestShippingMethodUpdate](pkpaymentrequestshippingmethodupdate.md)
  An object that updates the payment request after the shipping method changed.
- [class PKPaymentRequestCouponCodeUpdate](pkpaymentrequestcouponcodeupdate.md)
  An object that updates the payment request after the coupon code changes.
- [class PKPaymentRequestUpdate](pkpaymentrequestupdate.md)
  The base class for updating the payment request after the user makes changes on the payment sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentrequestshippingcontactupdate)*