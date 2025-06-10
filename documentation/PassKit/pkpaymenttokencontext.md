# PKPaymentTokenContext

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

A class that defines the context for a single payment token in a payment request for multimerchant payments.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class PKPaymentTokenContext
```

#### Overview

> ❗ **Important**:  You must set the [`multiTokenContexts`](pkpaymentrequest/multitokencontexts.md) property on the [`PKPaymentRequest`](pkpaymentrequest.md) object to use this class to request multimerchant payments.

Use [`PKPaymentTokenContext`](pkpaymenttokencontext.md) to authorize a payment amount for each payment token in a multimerchant payment request. To enable multiple merchants for a transaction, use one [`PKPaymentTokenContext`](pkpaymenttokencontext.md) object for each merchant.

You can optionally associate each payment token with the merchant’s top-level domain.

## Topics

### Creating a payment token context
- [init(merchantIdentifier: String, externalIdentifier: String, merchantName: String, merchantDomain: String?, amount: NSDecimalNumber)](pkpaymenttokencontext/init(merchantidentifier:externalidentifier:merchantname:merchantdomain:amount:).md)
  Create a payment token context for a single merchant.
### Specifying the merchant
- [var merchantIdentifier: String](pkpaymenttokencontext/merchantidentifier.md)
  The Apply Pay merchant identifier.
- [var merchantDomain: String?](pkpaymenttokencontext/merchantdomain.md)
  The merchant’s top-level domain that the Apple Pay server associates with the payment token.
- [var merchantName: String](pkpaymenttokencontext/merchantname.md)
  The merchant’s display name that the Apple Pay server associates with the payment token.
- [var externalIdentifier: String](pkpaymenttokencontext/externalidentifier.md)
  An external identifier for the merchant.
### Indicating a payment amount
- [var amount: NSDecimalNumber](pkpaymenttokencontext/amount.md)
  The amount to authorize for the payment token.

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

- [class PKPaymentRequest](pkpaymentrequest.md)
  An object that represents a request for payment, including details about payment-processing capabilities, the payment amount, and shipping information.
- [class PKRecurringPaymentRequest](pkrecurringpaymentrequest.md)
  A class that represents a request to set up a recurring payment, typically a subscription.
- [class PKAutomaticReloadPaymentRequest](pkautomaticreloadpaymentrequest.md)
  A class that represents a request to set up an automatic reload payment, such as a store card top-up or a prepaid account.
- [class PKDeferredPaymentRequest](pkdeferredpaymentrequest.md)
  An object that represents a request to set up a deferred payment, such as a hotel booking or a pre-order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymenttokencontext)*