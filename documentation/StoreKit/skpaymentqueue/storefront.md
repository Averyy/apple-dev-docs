# storefront

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The App Store storefront of the device.

**Availability**:
- iOS 13.0+ - Deprecated in 18.0
- iPadOS 13.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.15+ - Deprecated in 15.0
- tvOS 13.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: Use Storefront.current.

## Declaration

```swift
var storefront: SKStorefront? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly, nullable) SKStorefront * storefront;
```

*macOS*

```objc
@property (atomic, readonly, nullable) SKStorefront * storefront;
```

## Discussion

The storefront information tells you the device’s App Store region. You can use this information to display products that your app makes available in specific regions. You maintain your own list of product identifiers and the storefronts in which you make them available.

If the storefront changes during a transaction, StoreKit notifies your app by calling the [`paymentQueueDidChangeStorefront(_:)`](../skpaymenttransactionobserver/paymentqueuedidchangestorefront%28_%29.md) method of the [`SKPaymentTransactionObserver`](../skpaymenttransactionobserver.md) protocol. Implement [`paymentQueue(_:shouldContinue:in:)`](../skpaymentqueuedelegate/paymentqueue%28_,shouldcontinue,in%29.md) to indicate whether the transaction should continue with the new storefront.

> ❗ **Important**:  [`storefront`](./storefront.md) is a synchronous API that may take significant time to return. Don’t use [`storefront`](./storefront.md) in a time-sensitive thread, such as during app launch. To get asynchronous behavior, dispatch it to a separate queue, or use the asynchronous [`current`](../storefront/current.md) property of [`Storefront`](../storefront.md) instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymentqueue/storefront)*