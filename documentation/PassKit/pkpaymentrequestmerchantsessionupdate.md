# PKPaymentRequestMerchantSessionUpdate

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class  
**Role**: Class

An object that updates a payment request with a merchant validation.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class PKPaymentRequestMerchantSessionUpdate
```

```objc
@interface PKPaymentRequestMerchantSessionUpdate : NSObject
```

#### Overview

This is the handler for [`paymentAuthorizationController(_:didRequestMerchantSessionUpdate:)`](./pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller%28_,didrequestmerchantsessionupdate%29.md) and [`paymentAuthorizationViewController(_:didRequestMerchantSessionUpdate:)`](./pkpaymentauthorizationviewcontrollerdelegate/paymentauthorizationviewcontroller%28_,didrequestmerchantsessionupdate%29.md).

## Topics

### Creating a merchant session update
- [init(status: PKPaymentAuthorizationStatus, merchantSession: PKPaymentMerchantSession?)](./pkpaymentrequestmerchantsessionupdate/init%28status,merchantsession%29.md)
  Creates a payment method update with the specified status and merchant session.
### Getting information for the merchant session update
- [var status: PKPaymentAuthorizationStatus](./pkpaymentrequestmerchantsessionupdate/status.md)
  The current authorization status for the payment.
- [var session: PKPaymentMerchantSession?](./pkpaymentrequestmerchantsessionupdate/session.md)
  An object that validates the identity of a merchant for the payment request.
- [class PKPaymentMerchantSession](./pkpaymentmerchantsession.md)
  An object that validates the identity of a merchant for a payment request.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Payment sheet updates
- [class PKPaymentRequestPaymentMethodUpdate](./pkpaymentrequestpaymentmethodupdate.md)
  An object that updates the payment request after the payment method changes.
- [class PKPaymentRequestShippingContactUpdate](./pkpaymentrequestshippingcontactupdate.md)
  An object that updates the payment request after the shipping contact information changes.
- [class PKPaymentRequestShippingMethodUpdate](./pkpaymentrequestshippingmethodupdate.md)
  An object that updates the payment request after the shipping method changed.
- [class PKPaymentRequestCouponCodeUpdate](./pkpaymentrequestcouponcodeupdate.md)
  An object that updates the payment request after the coupon code changes.
- [class PKPaymentRequestUpdate](./pkpaymentrequestupdate.md)
  The base class for updating the payment request after the user makes changes on the payment sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentrequestmerchantsessionupdate)*