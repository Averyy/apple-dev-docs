# paymentQueueDidChangeStorefront(_:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Instance Method

Tells the observer that the storefront for the payment queue has changed.

**Availability**:
- iOS 13.0+ - Deprecated in 18.0
- iPadOS 13.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.15+ - Deprecated in 15.0
- tvOS 13.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: Use Storefront.updates.

## Declaration

```swift
optional func paymentQueueDidChangeStorefront(_ queue: SKPaymentQueue)
```

```objc
- (void) paymentQueueDidChangeStorefront:(SKPaymentQueue *) queue;
```

#### Discussion

See [`SKStorefront`](../skstorefront.md) for more information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver/paymentqueuedidchangestorefront(_:))*