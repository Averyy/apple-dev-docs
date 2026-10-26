# init()

**Framework**: CloudKit  
**Kind**: init  
**Role**: Initializer

Creates an empty fetch subscriptions operation.

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
init()
```

```objc
- (instancetype) init;
```

#### Discussion

You must set the [`subscriptionIDs`](./subscriptionids-714ct.md) property before you execute the operation.

## See Also

### Creating a Fetch Subscriptions Operation
- [convenience init(subscriptionIDs: [CKSubscription.ID])](./init%28subscriptionids%29.md)
  Creates an operation for fetching the specified subscriptions.
- [- initWithSubscriptionIDs:](./initwithsubscriptionids_.md)
  Creates an operation for fetching the specified subscriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchsubscriptionsoperation/init())*