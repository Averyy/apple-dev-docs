# SKRequest

**Framework**: StoreKit  
**Kind**: class

An abstract class that represents a request to the App Store.

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
class SKRequest
```

#### Overview

To make a request, initialize a subclass of [`SKRequest`](skrequest.md)—such as [`SKProductsRequest`](skproductsrequest.md) or [`SKReceiptRefreshRequest`](skreceiptrefreshrequest.md)—set the [`delegate`](skrequest/delegate.md) property, and call the [`start()`](skrequest/start().md) method.

## Topics

### Controlling the Request
- [func start()](skrequest/start.md)
  Sends the request to the Apple App Store.
- [func cancel()](skrequest/cancel.md)
  Cancels a previously started request.
### Accessing the Delegate
- [var delegate: (any SKRequestDelegate)?](skrequest/delegate.md)
  The delegate of the request object.
- [protocol SKRequestDelegate](skrequestdelegate.md)
  Common methods that are implemented by delegates for any subclass of the `SKRequest` abstract class.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [SKProductsRequest](skproductsrequest.md)
- [SKReceiptRefreshRequest](skreceiptrefreshrequest.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Setting up the transaction observer for the payment queue](setting-up-the-transaction-observer-for-the-payment-queue.md)
  Enable your app to receive and handle transactions by adding an observer.
- [Offering, completing, and restoring in-app purchases](offering-completing-and-restoring-in-app-purchases.md)
  Fetch, display, purchase, validate, and finish transactions in your app.
- [class SKPaymentQueue](skpaymentqueue.md)
  A queue of payment transactions for the App Store to process.
- [protocol SKPaymentTransactionObserver](skpaymenttransactionobserver.md)
  A set of methods that process transactions, unlock purchased functionality, and continue promoted In-App Purchases.
- [protocol SKPaymentQueueDelegate](skpaymentqueuedelegate.md)
  The protocol that provides information needed to complete transactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skrequest)*