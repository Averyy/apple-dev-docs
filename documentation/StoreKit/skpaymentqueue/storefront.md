# storefront

**Framework**: StoreKit  
**Kind**: property

The App Store storefront of the device.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
var storefront: SKStorefront? { get }
```

#### Discussion

The storefront information tells you the device’s App Store region. You can use this information to display products that your app makes available in specific regions. You maintain your own list of product identifiers and the storefronts in which you make them available.

If the storefront changes during a transaction, StoreKit notifies your app by calling the [`paymentQueueDidChangeStorefront(_:)`](skpaymenttransactionobserver/paymentqueuedidchangestorefront(_:).md) method of the [`SKPaymentTransactionObserver`](skpaymenttransactionobserver.md) protocol. Implement [`paymentQueue(_:shouldContinue:in:)`](skpaymentqueuedelegate/paymentqueue(_:shouldcontinue:in:).md) to indicate whether the transaction should continue with the new storefront.

> ❗ **Important**:  [`storefront`](skpaymentqueue/storefront.md) is a synchronous API that may take significant time to return. Don’t use [`storefront`](skpaymentqueue/storefront.md) in a time-sensitive thread, such as during app launch. To get asynchronous behavior, dispatch it to a separate queue, or use the asynchronous [`current`](storefront/current.md) property of [`Storefront`](storefront.md) instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymentqueue/storefront)*