# fetchAllSubscriptionsOperation()

**Framework**: CloudKit  
**Kind**: method  
**Role**: Type Method

Returns an operation that fetches all of the user’s subscriptions.

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
class func fetchAllSubscriptionsOperation() -> Self
```

```objc
+ (instancetype) fetchAllSubscriptionsOperation;
```

#### Discussion

After creating the operation, set the [`fetchSubscriptionCompletionBlock`](./fetchsubscriptioncompletionblock-207ep.md) property to process the results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchsubscriptionsoperation/fetchallsubscriptionsoperation())*