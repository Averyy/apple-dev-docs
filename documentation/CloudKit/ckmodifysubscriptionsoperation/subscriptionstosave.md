# subscriptionsToSave

**Framework**: CloudKit  
**Kind**: property

The subscriptions to save to the database.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var subscriptionsToSave: [CKSubscription]? { get set }
```

#### Discussion

This property contains the subscriptions that you want to save. Its initial value is the array that you pass to the [`init(subscriptionsToSave:subscriptionIDsToDelete:)`](ckmodifysubscriptionsoperation/init(subscriptionstosave:subscriptionidstodelete:).md) method. Modify this property as necessary before you execute the operation or submit it to a queue. After CloudKit saves the subscriptions, it begins generating push notifications according to their criteria.

## See Also

- [var subscriptionIDsToDelete: [CKSubscription.ID]?](ckmodifysubscriptionsoperation/subscriptionidstodelete-3534e.md)
  The IDs of the subscriptions that you want to delete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckmodifysubscriptionsoperation/subscriptionstosave)*