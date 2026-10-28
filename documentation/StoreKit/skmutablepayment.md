# SKMutablePayment

**Framework**: StoreKit  
**Kind**: class  
**Role**: Class

A mutable request to the App Store to process payment for additional functionality that your app offers.

**Availability**:
- iOS 3.0+ - Deprecated in 18.0
- iPadOS 3.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.7+ - Deprecated in 15.0
- tvOS - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: Use Product.purchase(confirmIn:options:).

## Declaration

```swift
class SKMutablePayment
```

```objc
@interface SKMutablePayment : SKPayment
```

## Mentions

- [Implementing promotional offers in your app](./implementing-promotional-offers-in-your-app.md)

## Overview

A mutable payment object identifies a product and the quantity of that item the user would like to purchase.

When a mutable payment is added to the payment queue, the payment queue copies the contents into an immutable request before queueing the request. Your app can safely change the contents of the mutable payment object.

## Topics

### Getting and Setting Attributes
- [var productIdentifier: String](./skmutablepayment/productidentifier.md)
  A string that identifies a product that can be purchased from within your app.
- [var quantity: Int](./skmutablepayment/quantity.md)
  The number of items the user wants to purchase.
- [var requestData: Data?](./skmutablepayment/requestdata.md)
  Reserved for future use.
- [var applicationUsername: String?](./skmutablepayment/applicationusername.md)
  A string that associates the transaction with a user account on your service.
### Simulating Buy for Testing
- [var simulatesAskToBuyInSandbox: Bool](./skmutablepayment/simulatesasktobuyinsandbox.md)
  A Boolean value that produces an “ask to buy” flow for this payment in the sandbox.
### Getting and Setting Discount Details
- [var paymentDiscount: SKPaymentDiscount?](./skmutablepayment/paymentdiscount.md)
  The details of the discount offer to apply to the payment.

## Relationships

### Inherits From
- [SKPayment](./skpayment.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSMutableCopying](../Foundation/nsmutablecopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Purchases
- [Requesting a payment from the App Store](./requesting-a-payment-from-the-app-store.md)
  Submit a payment request to the App Store when a customer selects a product to buy.
- [Processing a transaction](./processing-a-transaction.md)
  Register a transaction queue observer to get and handle transaction updates from the App Store.
- [class SKPayment](./skpayment.md)
  A request to the App Store to process payment for additional functionality that your app offers.
- [class SKPaymentTransaction](./skpaymenttransaction.md)
  An object in the payment queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skmutablepayment)*