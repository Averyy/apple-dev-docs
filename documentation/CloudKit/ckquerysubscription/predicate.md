# predicate

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The matching criteria to apply to records.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@NSCopying
var predicate: NSPredicate { get }
```

```objc
@property (copy, readonly) NSPredicate * predicate;
```

#### Discussion

A query-based subscription uses its search predicate to identify potential matches for records. It combines the predicate information with the value in the [`querySubscriptionOptions`](./querysubscriptionoptions.md) property to determine when to send a push notification to the app.

The search predicate defines the records that the subscription object monitors for changes. The system only uses the property’s value when the [`subscriptionType`](../cksubscription/subscriptiontype-swift.property.md) property is [`CKSubscription.SubscriptionType.query`](../cksubscription/subscriptiontype-swift.enum/query.md). Otherwise, the system ignores it.

## See Also

### Accessing the Subscription Search Parameters
- [var querySubscriptionOptions: CKQuerySubscription.Options](./querysubscriptionoptions.md)
  Options that define the behavior of the subscription.
- [CKQuerySubscription.Options](./options.md)
  Configuration options for a query subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckquerysubscription/predicate)*