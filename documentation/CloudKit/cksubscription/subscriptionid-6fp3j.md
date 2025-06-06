# subscriptionID

**Framework**: CloudKit  
**Kind**: property

The subscription’s unique identifier.

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
var subscriptionID: CKSubscription.ID { get }
```

#### Discussion

This property’s value is the subscription ID that you provide to the `init(recordType:predicate:subscriptionID:options:)` or `init(zoneID:subscriptionID:options:)` methods when you create the subscription. If you use a different method to create the subscription, CloudKit automatically assigns a UUID as the subscription ID.

## See Also

- [CKSubscription.ID](cksubscription/id.md)
  A type that represents a subscription’s identifier.
- [var subscriptionType: CKSubscription.SubscriptionType](cksubscription/subscriptiontype-swift.property.md)
  The behavior that a subscription provides.
- [CKSubscription.SubscriptionType](cksubscription/subscriptiontype-swift.enum.md)
  Constants that identify a subscription’s behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksubscription/subscriptionid-6fp3j)*