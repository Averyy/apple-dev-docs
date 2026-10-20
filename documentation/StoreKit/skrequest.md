# SKRequest

**Framework**: StoreKit  
**Kind**: class  
**Role**: Class

An abstract class that represents a request to the App Store.

**Availability**:
- iOS 3.0+ - Deprecated in 18.0
- iPadOS 3.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.7+ - Deprecated in 15.0
- tvOS - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: No longer supported.

## Declaration

```swift
class SKRequest
```

```objc
@interface SKRequest : NSObject
```

#### Overview

To make a request, initialize a subclass of [`SKRequest`](./skrequest.md)—such as [`SKProductsRequest`](./skproductsrequest.md) or [`SKReceiptRefreshRequest`](./skreceiptrefreshrequest.md)—set the [`delegate`](./skrequest/delegate.md) property, and call the [`start()`](./skrequest/start%28%29.md) method.

## Topics

### Controlling the Request
- [func start()](./skrequest/start%28%29.md)
  Sends the request to the Apple App Store.
- [func cancel()](./skrequest/cancel%28%29.md)
  Cancels a previously started request.
### Accessing the Delegate
- [var delegate: (any SKRequestDelegate)?](./skrequest/delegate.md)
  The delegate of the request object.
- [protocol SKRequestDelegate](./skrequestdelegate.md)
  Common methods that are implemented by delegates for any subclass of the `SKRequest` abstract class.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [SKProductsRequest](./skproductsrequest.md)
- [SKReceiptRefreshRequest](./skreceiptrefreshrequest.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Essentials
- [Setting up the transaction observer for the payment queue](./setting-up-the-transaction-observer-for-the-payment-queue.md)
  Enable your app to receive and handle transactions by adding an observer.
- [Offering, completing, and restoring Apple In-App Purchases](./offering-completing-and-restoring-in-app-purchases.md)
  Fetch, display, purchase, validate, and finish transactions in your app.
- [class SKPaymentQueue](./skpaymentqueue.md)
  A queue of payment transactions for the App Store to process.
- [protocol SKPaymentTransactionObserver](./skpaymenttransactionobserver.md)
  A set of methods that process transactions, unlock purchased functionality, and continue promoted Apple In-App Purchases.
- [protocol SKPaymentQueueDelegate](./skpaymentqueuedelegate.md)
  The protocol that provides information needed to complete transactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skrequest)*