# simulatesAskToBuyInSandbox(_:)

**Framework**: StoreKit  
**Kind**: method

Simulates an Ask to Buy scenario when testing your app in the sandbox environment.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static func simulatesAskToBuyInSandbox(_ simulateAskToBuy: Bool) -> Product.PurchaseOption
```

#### Return Value

An instance of [`Product.PurchaseOption`](product/purchaseoption.md) to use in [`purchase(options:)`](product/purchase(options:).md).

#### Discussion

For information about testing Ask to Buy scenarios, see [`Testing at all stages of development with Xcode and the sandbox`](testing-at-all-stages-of-development-with-xcode-and-the-sandbox.md).

For information about purchases made using Ask to Buy, see [`Approve what kids buy with Ask to Buy`](https://developer.apple.comhttps://support.apple.com/en-us/HT201089).

## Parameters

- `simulateAskToBuy`: Set to   to simulate a child’s account asking permission to make a purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/purchaseoption/simulatesasktobuyinsandbox(_:))*