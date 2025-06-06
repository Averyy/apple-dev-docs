# SKPayment

**Framework**: StoreKit  
**Kind**: class

A request to the App Store to process payment for additional functionality that your app offers.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS ?+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
class SKPayment
```

## Mentions

- [Promoting In-App Purchases](promoting-in-app-purchases.md)
- [Testing a payment request](testing-a-payment-request.md)

#### Overview

A payment object identifies a product and the quantity of those items the user would like to purchase.

## Topics

### Creating Payments
- [convenience init(product: SKProduct)](skpayment/init(product:).md)
  Returns a new payment for the specified product.
### Getting Payment Details
- [var productIdentifier: String](skpayment/productidentifier.md)
  A string used to identify a product that can be purchased from within your app.
- [var quantity: Int](skpayment/quantity.md)
  The number of items the user wants to purchase.
- [var requestData: Data?](skpayment/requestdata.md)
  Reserved for future use.
- [var applicationUsername: String?](skpayment/applicationusername.md)
  A string that associates the transaction with a user account on your service.
### Simulating Purchases for Testing
- [var simulatesAskToBuyInSandbox: Bool](skpayment/simulatesasktobuyinsandbox.md)
  A Boolean value that produces an “ask to buy” flow for this payment in the sandbox.
### Getting Discount Details
- [var paymentDiscount: SKPaymentDiscount?](skpayment/paymentdiscount.md)
  The details of the discount offer to apply to the payment.
- [class SKPaymentDiscount](skpaymentdiscount.md)
  The signed discount to apply to a payment.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [SKMutablePayment](skmutablepayment.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSMutableCopying](../Foundation/NSMutableCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Requesting a payment from the App Store](requesting-a-payment-from-the-app-store.md)
  Submit a payment request to the App Store when a customer selects a product to buy.
- [Processing a transaction](processing-a-transaction.md)
  Register a transaction queue observer to get and handle transaction updates from the App Store.
- [class SKMutablePayment](skmutablepayment.md)
  A mutable request to the App Store to process payment for additional functionality that your app offers.
- [class SKPaymentTransaction](skpaymenttransaction.md)
  An object in the payment queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpayment)*