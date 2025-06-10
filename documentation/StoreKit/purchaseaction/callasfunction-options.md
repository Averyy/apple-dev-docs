# callAsFunction(_:options:)

**Framework**: StoreKit  
**Kind**: method

Starts an in-app purchase for the indicated product and purchase options.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@MainActor
@preconcurrency func callAsFunction(_ product: Product, options: Set<Product.PurchaseOption> = []) async throws -> Product.PurchaseResult
```

#### Return Value

The result of the purchase, [`Product.PurchaseResult`](product/purchaseresult.md).

#### Discussion

Don’t call this method directly. SwiftUI calls it when you call the [`PurchaseAction`](purchaseaction.md) structure with the `product` and `options` as arguments.

This method may throw a [`Product.PurchaseError`](product/purchaseerror.md) or [`StoreKitError`](storekiterror.md).

For information about how Swift uses the [`callAsFunction(_:options:)`](purchaseaction/callasfunction(_:options:).md) method to simplify call site syntax, see [`Methods with Special Names`](https://developer.apple.comhttps://docs.swift.org/swift-book/documentation/the-swift-programming-language/declarations/#Methods-with-Special-Names) in .

## Parameters

- `product`: The in-app purchase   the customer is purchasing.
- `options`: A set of options you may associate with the purchase ( ).


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/purchaseaction/callasfunction(_:options:))*