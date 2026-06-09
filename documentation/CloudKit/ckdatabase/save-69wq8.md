# save(_:)

**Framework**: CloudKit  
**Kind**: method

Saves a specific subscription.

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
func save(_ subscription: CKSubscription) async throws -> CKSubscription
```

#### Return Value

The saved subscription (as it appears on the server).

#### Discussion

This method throws an error if the request fails, such as when the network is unavailable or the device doesn’t have an active iCloud account.

For information on a more convenient way to save subscriptions, see [`modifySubscriptions(saving:deleting:)`](ckdatabase/modifysubscriptions(saving:deleting:).md).

## Parameters

- `subscription`: The subscription to save.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/save(_:)-69wq8)*