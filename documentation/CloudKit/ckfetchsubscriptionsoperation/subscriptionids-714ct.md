# subscriptionIDs

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The IDs of the subscriptions to fetch.

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
@property (nonatomic, copy, nullable) NSArray<NSString *> * subscriptionIDs;
```

## Discussion

Use this property to view or change the IDs of the subscriptions to fetch. Each element of the array is a string that represents the ID of a subscription. If you intend to modify this property’s value, do so before you execute the operation or submit it to a queue.

If you use the [`fetchAllSubscriptionsOperation()`](./fetchallsubscriptionsoperation%28%29.md) method to create the operation, CloudKit ignores this property’s value and sets it to `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchsubscriptionsoperation/subscriptionids-714ct)*