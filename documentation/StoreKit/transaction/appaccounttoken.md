# appAccountToken

**Framework**: StoreKit  
**Kind**: property

A UUID that associates the transaction with a user on your own service.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
let appAccountToken: UUID?
```

## Mentions

- [Generating a signature for promotional offers](generating-a-signature-for-promotional-offers.md)

#### Discussion

You create an [`appAccountToken(_:)`](product/purchaseoption/appaccounttoken(_:).md) and send it to the App Store when a customer initiates an in-app purchase. The App Store returns the same value in [`appAccountToken`](transaction/appaccounttoken.md) in the transaction information after the customer completes the purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/appaccounttoken)*