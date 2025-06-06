# subscriptionIDsToDelete

**Framework**: CloudKit  
**Kind**: property

The IDs of the subscriptions that you want to delete.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS ?+
- watchOS 6.0+
- Swift 4.2+

## Declaration

```swift
var subscriptionIDsToDelete: [CKSubscription.ID]? { get set }
```

#### Discussion

This property contains the IDs of the subscriptions that you want to delete. Its initial value is the array that you pass to the [`init(subscriptionsToSave:subscriptionIDsToDelete:)`](ckmodifysubscriptionsoperation/init(subscriptionstosave:subscriptionidstodelete:).md) method. Modify this property as necessary before you execute the operation or submit it to a queue.

## See Also

- [var subscriptionsToSave: [CKSubscription]?](ckmodifysubscriptionsoperation/subscriptionstosave.md)
  The subscriptions to save to the database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckmodifysubscriptionsoperation/subscriptionidstodelete-3534e)*