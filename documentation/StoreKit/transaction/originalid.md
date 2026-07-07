# originalID

**Framework**: StoreKit  
**Kind**: property

The original transaction identifier of a purchase.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
let originalID: UInt64
```

#### Discussion

The original transaction identifier, [`originalID`](transaction/originalid.md), is identical to [`id`](transaction/id.md) except when the user restores a purchase or renews a transaction. You can use this value to:

- Identify one or more renewals for the same subscription.
- Differentiate a purchase transaction from a restore or a renewal transaction. For restore and renewal transactions, the original transaction identifier, [`originalID`](transaction/originalid.md), and transaction identifier, [`id`](transaction/id.md), differ.
- Match a transaction in the app with a transaction you receive on your server in an [`App Store Server Notifications`](https://developer.apple.com/documentation/AppStoreServerNotifications) event.

## See Also

- [let originalPurchaseDate: Date](transaction/originalpurchasedate.md)
  The date of purchase for the original transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/originalid)*