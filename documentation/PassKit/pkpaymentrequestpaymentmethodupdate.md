# PKPaymentRequestPaymentMethodUpdate

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class  
**Role**: Class

An object that updates the payment request after the payment method changes.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class PKPaymentRequestPaymentMethodUpdate
```

```objc
@interface PKPaymentRequestPaymentMethodUpdate : PKPaymentRequestUpdate
```

## Overview

This is the handler for [`paymentAuthorizationController(_:didSelectPaymentMethod:handler:)`](./pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller%28_,didselectpaymentmethod,handler%29.md) and [`paymentAuthorizationViewController(_:didSelect:handler:)`](./pkpaymentauthorizationviewcontrollerdelegate/paymentauthorizationviewcontroller%28_,didselect,handler%29-3bex6.md). Update the summary items to reflect the change in payment method.

## Topics

### Creating a payment request update
- [init(errors: [any Error]?, paymentSummaryItems: [PKPaymentSummaryItem])](./pkpaymentrequestpaymentmethodupdate/init%28errors,paymentsummaryitems%29.md)
  Creates a payment-method update with your specified payment summary items.
### Getting user errors
- [var errors: [any Error]!](./pkpaymentrequestpaymentmethodupdate/errors.md)
  An array of payment-method errors that the user must resolve.

## Relationships

### Inherits From
- [PKPaymentRequestUpdate](./pkpaymentrequestupdate.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Payment sheet updates
- [class PKPaymentRequestMerchantSessionUpdate](./pkpaymentrequestmerchantsessionupdate.md)
  An object that updates a payment request with a merchant validation.
- [class PKPaymentRequestShippingContactUpdate](./pkpaymentrequestshippingcontactupdate.md)
  An object that updates the payment request after the shipping contact information changes.
- [class PKPaymentRequestShippingMethodUpdate](./pkpaymentrequestshippingmethodupdate.md)
  An object that updates the payment request after the shipping method changed.
- [class PKPaymentRequestCouponCodeUpdate](./pkpaymentrequestcouponcodeupdate.md)
  An object that updates the payment request after the coupon code changes.
- [class PKPaymentRequestUpdate](./pkpaymentrequestupdate.md)
  The base class for updating the payment request after the user makes changes on the payment sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentrequestpaymentmethodupdate)*