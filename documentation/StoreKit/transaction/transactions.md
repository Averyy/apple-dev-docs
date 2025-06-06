# Transaction.Transactions

**Framework**: StoreKit  
**Kind**: struct

An asynchronous sequence of transactions.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct Transactions
```

#### Overview

You don’t create a [`Transaction.Transactions`](transaction/transactions.md) sequence directly. Use methods such as [`all`](transaction/all.md), [`updates`](transaction/updates.md), or [`currentEntitlements`](transaction/currententitlements.md) to get transactions.

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [static var updates: Transaction.Transactions](transaction/updates.md)
  The asynchronous sequence that emits a transaction when the system creates or updates transactions that occur outside the app or on other devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/transactions)*