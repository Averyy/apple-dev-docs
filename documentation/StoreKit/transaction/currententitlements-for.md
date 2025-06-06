# currentEntitlements(for:)

**Framework**: StoreKit  
**Kind**: method

Gets the transactions that entitle the user to items purchased under a product ID.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
static func currentEntitlements(for productID: String) -> Transaction.Transactions
```

#### Return Value

A sequence containing all transactions that entitle the user to the product.

#### Discussion

If a generic SKU is provided, the returned sequence will yield all transactions that entitle the user to Advanced Commerce Items purchased using the generic product’s ID.

If an ID for a regular IAP is provided, the returned sequence will contain no more than one transaction.

## Parameters

- `productID`: Identifies the product to check entitlements for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/currententitlements(for:))*