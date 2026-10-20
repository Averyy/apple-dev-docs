# CKSubscription.SubscriptionType

**Framework**: CloudKit  
**Kind**: enum  
**Role**: Enumeration

Constants that identify a subscription’s behavior.

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
enum SubscriptionType
```

```c
enum CKSubscriptionType : NSInteger;
```

## Topics

### Subscription Types
- [CKSubscription.SubscriptionType.query](./subscriptiontype-swift.enum/query.md)
  A constant that indicates the subscription is query-based.
- [CKSubscription.SubscriptionType.database](./subscriptiontype-swift.enum/database.md)
  A constant that indicates the subscription is database-based.
- [CKSubscription.SubscriptionType.recordZone](./subscriptiontype-swift.enum/recordzone.md)
  A constant that indicates the subscription is zone-based.
### Initializers
- [init?(rawValue: Int)](./subscriptiontype-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing the Subscription Metadata
- [var subscriptionID: CKSubscription.ID](./subscriptionid-6fp3j.md)
  The subscription’s unique identifier.
- [CKSubscription.ID](./id.md)
  A type that represents a subscription’s identifier.
- [var subscriptionType: CKSubscription.SubscriptionType](./subscriptiontype-swift.property.md)
  The behavior that a subscription provides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksubscription/subscriptiontype-swift.enum)*