# CKSubscription.SubscriptionType

**Framework**: CloudKit  
**Kind**: enum

Constants that identify a subscription’s behavior.

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
enum SubscriptionType
```

## Topics

### Subscription Types
- [CKSubscription.SubscriptionType.query](cksubscription/subscriptiontype-swift.enum/query.md)
  A constant that indicates the subscription is query-based.
- [CKSubscription.SubscriptionType.database](cksubscription/subscriptiontype-swift.enum/database.md)
  A constant that indicates the subscription is database-based.
- [CKSubscription.SubscriptionType.recordZone](cksubscription/subscriptiontype-swift.enum/recordzone.md)
  A constant that indicates the subscription is zone-based.
### Initializers
- [init?(rawValue: Int)](cksubscription/subscriptiontype-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var subscriptionID: CKSubscription.ID](cksubscription/subscriptionid-6fp3j.md)
  The subscription’s unique identifier.
- [CKSubscription.ID](cksubscription/id.md)
  A type that represents a subscription’s identifier.
- [var subscriptionType: CKSubscription.SubscriptionType](cksubscription/subscriptiontype-swift.property.md)
  The behavior that a subscription provides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksubscription/subscriptiontype-swift.enum)*