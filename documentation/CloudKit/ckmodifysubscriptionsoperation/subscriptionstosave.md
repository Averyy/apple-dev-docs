# subscriptionsToSave

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The subscriptions to save to the database.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var subscriptionsToSave: [CKSubscription]? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSArray<CKSubscription *> * subscriptionsToSave;
```

#### Discussion

This property contains the subscriptions that you want to save. Its initial value is the array that you pass to the [`init(subscriptionsToSave:subscriptionIDsToDelete:)`](./init%28subscriptionstosave,subscriptionidstodelete%29.md) method. Modify this property as necessary before you execute the operation or submit it to a queue. After CloudKit saves the subscriptions, it begins generating push notifications according to their criteria.

## See Also

### Configuring the Modify Subscriptions Operation
- [var subscriptionIDsToDelete: [CKSubscription.ID]?](./subscriptionidstodelete-3534e.md)
  The IDs of the subscriptions that you want to delete.
- [subscriptionIDsToDelete](./subscriptionidstodelete-14x82.md)
  The IDs of the subscriptions that you want to delete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckmodifysubscriptionsoperation/subscriptionstosave)*