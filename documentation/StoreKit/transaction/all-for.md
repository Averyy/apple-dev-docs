# all(for:)

**Framework**: StoreKit  
**Kind**: method

Gets all the transactions associated with this product ID.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
static func all(for productID: String) -> Transaction.Transactions
```

#### Return Value

A sequence containing all transactions for the given product.

## Parameters

- `productID`: Identifies the product to filter the transaction cache against.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/all(for:))*