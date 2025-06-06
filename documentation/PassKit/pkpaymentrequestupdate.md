# PKPaymentRequestUpdate

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

The base class for updating the payment request after the user makes changes on the payment sheet.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class PKPaymentRequestUpdate
```

## Topics

### Creating a payment request update
- [init(paymentSummaryItems: [PKPaymentSummaryItem])](pkpaymentrequestupdate/init(paymentsummaryitems:).md)
  Creates a payment request update with the specified payment summary items.
### Updating authorization status
- [var status: PKPaymentAuthorizationStatus](pkpaymentrequestupdate/status.md)
  The status of the payment request that indicates whether authorization succeeds or fails.
- [enum PKPaymentAuthorizationStatus](pkpaymentauthorizationstatus.md)
  General success and failure status for payment authorization.
### Updating summary items
- [var paymentSummaryItems: [PKPaymentSummaryItem]](pkpaymentrequestupdate/paymentsummaryitems.md)
  The list of payment summary items for the instance.
- [class PKPaymentSummaryItem](pkpaymentsummaryitem.md)
  An object that defines a summary item in a payment request, taxes, discounts, shipping, a grand total, and the like.
### Updating shipping methods
- [var shippingMethods: [PKShippingMethod]](pkpaymentrequestupdate/shippingmethods.md)
  The list of shipping methods available for a payment request.
### Updating automatic reload payments
- [var automaticReloadPaymentRequest: PKAutomaticReloadPaymentRequest?](pkpaymentrequestupdate/automaticreloadpaymentrequest.md)
  The automatic reload payment request to update the payment request with.
### Updating multitoken or multimerchant payments
- [var multiTokenContexts: [PKPaymentTokenContext]?](pkpaymentrequestupdate/multitokencontexts.md)
  An optional array of payment token contexts to request multiple payment tokens with one payment token per context.
### Updating recurring payments
- [var recurringPaymentRequest: PKRecurringPaymentRequest?](pkpaymentrequestupdate/recurringpaymentrequest.md)
  The recurring payment request to update the payment request with.
### Setting up a deferred payment request
- [var deferredPaymentRequest: PKDeferredPaymentRequest?](pkpaymentrequestupdate/deferredpaymentrequest.md)
  The deferred payment request to update the payment request with.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [PKPaymentRequestCouponCodeUpdate](pkpaymentrequestcouponcodeupdate.md)
- [PKPaymentRequestPaymentMethodUpdate](pkpaymentrequestpaymentmethodupdate.md)
- [PKPaymentRequestShippingContactUpdate](pkpaymentrequestshippingcontactupdate.md)
- [PKPaymentRequestShippingMethodUpdate](pkpaymentrequestshippingmethodupdate.md)
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
- [class PKPaymentRequestCouponCodeUpdate](pkpaymentrequestcouponcodeupdate.md)
  An object that updates the payment request after the coupon code changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentrequestupdate)*