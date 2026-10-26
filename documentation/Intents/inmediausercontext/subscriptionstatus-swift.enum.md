# INMediaUserContext.SubscriptionStatus

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants that describe the current description status.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
enum SubscriptionStatus
```

```c
enum INMediaUserContextSubscriptionStatus : NSInteger;
```

## Topics

### Constants
- [INMediaUserContext.SubscriptionStatus.unknown](./subscriptionstatus-swift.enum/unknown.md)
  A code that indicates the app doesn’t offer subscriptions or the subscription status is unavailable.
- [INMediaUserContext.SubscriptionStatus.notSubscribed](./subscriptionstatus-swift.enum/notsubscribed.md)
  A code that indicates the user isn’t a subscriber, but subscriptions are available.
- [INMediaUserContext.SubscriptionStatus.subscribed](./subscriptionstatus-swift.enum/subscribed.md)
  A code that indicates the user currently has a subscription.
### Initializers
- [init?(rawValue: Int)](./subscriptionstatus-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing the Media Context Information
- [var numberOfLibraryItems: Int?](./numberoflibraryitems-8rnf0.md)
  An approximate number of relevant items available in the users library.
- [var subscriptionStatus: INMediaUserContext.SubscriptionStatus](./subscriptionstatus-swift.property.md)
  The user’s current subscription status.
- [numberOfLibraryItems](./numberoflibraryitems-881cf.md)
  An approximate number of relevant items available in the users library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmediausercontext/subscriptionstatus-swift.enum)*