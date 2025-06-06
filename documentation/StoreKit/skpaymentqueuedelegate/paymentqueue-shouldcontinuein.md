# paymentQueue(_:shouldContinue:in:)

**Framework**: StoreKit  
**Kind**: method

Asks the delegate whether to continue the transaction if the device’s App Store storefront changes during a transaction.

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
optional func paymentQueue(_ paymentQueue: SKPaymentQueue, shouldContinue transaction: SKPaymentTransaction, in newStorefront: SKStorefront) -> Bool
```

#### Discussion

StoreKit calls this delegate method if the storefront changes while processing a transaction.

- Return `true` if you wish to continue the transaction within the updated storefront.
- Return `false` to stop the transaction. The transaction will fail with the error [`SKError.Code.storeProductNotAvailable`](skerror/code/storeproductnotavailable.md). In this case, consider displaying a message to the user indicating that the product isn’t available in the current storefront.

If the delegate isn’t implemented, [`paymentQueue(_:shouldContinue:in:)`](skpaymentqueuedelegate/paymentqueue(_:shouldcontinue:in:).md) defaults to `true`.

This call times out after approximately one second, defaulting to `false` and causing the transaction to fail. The delegate should return as quickly as possible. Don’t perform any networking calls in this method. Your app should cache product availability information locally before starting a transaction.

See [`SKStorefront`](skstorefront.md) for more information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymentqueuedelegate/paymentqueue(_:shouldcontinue:in:))*