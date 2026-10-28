# subscriptionIDsToDelete

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The IDs of the subscriptions that you want to delete.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```objc
@property (nonatomic, copy, nullable) NSArray<NSString *> * subscriptionIDsToDelete;
```

## Discussion

This property contains the IDs of the subscriptions that you want to delete. Its initial value is the array that you pass to the [`init(subscriptionsToSave:subscriptionIDsToDelete:)`](./init%28subscriptionstosave,subscriptionidstodelete%29.md) method. Modify this property as necessary before you execute the operation or submit it to a queue.

## See Also

### Configuring the Modify Subscriptions Operation
- [var subscriptionsToSave: [CKSubscription]?](./subscriptionstosave.md)
  The subscriptions to save to the database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckmodifysubscriptionsoperation/subscriptionidstodelete-14x82)*