# simulatesAskToBuyInSandbox(_:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Type Method

Simulates an Ask to Buy scenario when testing your app in the sandbox environment.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static func simulatesAskToBuyInSandbox(_ simulateAskToBuy: Bool) -> Product.PurchaseOption
```

## Mentions

- [Testing Ask to Buy in the sandbox environment](../../testing-ask-to-buy-in-the-sandbox-environment.md)

## Return Value

An instance of [`Product.PurchaseOption`](../purchaseoption.md) to use in [`purchase(options:)`](../purchase%28options%29.md).

## Discussion

This option puts a single purchase into the pending state. If you’re signed in to a Sandbox Apple Account, you can approve or decline the request on the Ask to Buy page in Account Settings. While Enable Ask to Buy is on, every purchase already requires approval, so this option has no effect. For more information on testing the approval flow, see [Testing Ask to Buy in the sandbox environment](../../testing-ask-to-buy-in-the-sandbox-environment.md).

For information about testing Ask to Buy scenarios, see [Testing at all stages of development with Xcode and the sandbox](../../testing-at-all-stages-of-development-with-xcode-and-the-sandbox.md). For information about testing Ask to Buy in Xcode, see [Testing Ask to Buy in Xcode](../../testing-ask-to-buy-in-xcode.md).

For information about purchases that use Ask to Buy, see [Approve what kids buy with Ask to Buy](https://support.apple.com/105055).

## Parameters

- `simulateAskToBuy`: Set to `true` to simulate a child’s account asking permission to make a purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/purchaseoption/simulatesasktobuyinsandbox(_:))*