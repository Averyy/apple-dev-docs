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

## See Also

- [static func currentEntitlements(for: String) -> Transaction.Transactions](transaction/currententitlements(for:).md)
  Gets the transactions that entitle the user to items purchased under a product ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/all(for:))*