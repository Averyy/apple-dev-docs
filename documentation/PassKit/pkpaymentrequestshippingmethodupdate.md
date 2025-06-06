# PKPaymentRequestShippingMethodUpdate

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

An object that updates the payment request after the shipping method changed.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class PKPaymentRequestShippingMethodUpdate
```

#### Overview

This is the handler for [`paymentAuthorizationController(_:didSelectShippingMethod:handler:)`](pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller(_:didselectshippingmethod:handler:).md) and [`paymentAuthorizationViewController(_:didSelect:handler:)`](pkpaymentauthorizationviewcontrollerdelegate/paymentauthorizationviewcontroller(_:didselect:handler:)-5r0i7.md).

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
- [class PKPaymentRequestCouponCodeUpdate](pkpaymentrequestcouponcodeupdate.md)
  An object that updates the payment request after the coupon code changes.
- [class PKPaymentRequestUpdate](pkpaymentrequestupdate.md)
  The base class for updating the payment request after the user makes changes on the payment sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentrequestshippingmethodupdate)*