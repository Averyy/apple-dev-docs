# allSubscriptions()

**Framework**: CloudKit  
**Kind**: method

Fetches all subscriptions from the current database.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
func allSubscriptions() async throws -> [CKSubscription]
```

#### Return Value

The database’s subscriptions.

#### Discussion

This method throws an error if the request fails, such as when the network is unavailable or the device doesn’t have an active iCloud account.

For information on a more configurable way to fetch all subscriptions from a specific database, see [`fetchAllSubscriptionsOperation()`](ckfetchsubscriptionsoperation/fetchallsubscriptionsoperation().md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/allsubscriptions())*