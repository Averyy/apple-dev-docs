# NotificationQueue.NotificationCoalescing

**Framework**: Foundation  
**Kind**: struct

The constants that specify how notifications are coalesced.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct NotificationCoalescing
```

#### Overview

These constants are used by the [`enqueue(_:postingStyle:coalesceMask:forModes:)`](notificationqueue/enqueue(_:postingstyle:coalescemask:formodes:).md) method.

## Topics

### Constants
- [static var none: NotificationQueue.NotificationCoalescing](notificationqueue/notificationcoalescing/none.md)
  Do not coalesce notifications in the queue.
- [static var onName: NotificationQueue.NotificationCoalescing](notificationqueue/notificationcoalescing/onname.md)
  Coalesce notifications with the same name.
- [static var onSender: NotificationQueue.NotificationCoalescing](notificationqueue/notificationcoalescing/onsender.md)
  Coalesce notifications with the same object.
- [static var none: NotificationQueue.NotificationCoalescing](notificationqueue/notificationcoalescing/none.md)
  Do not coalesce notifications in the queue.
- [static var onName: NotificationQueue.NotificationCoalescing](notificationqueue/notificationcoalescing/onname.md)
  Coalesce notifications with the same name.
- [static var onSender: NotificationQueue.NotificationCoalescing](notificationqueue/notificationcoalescing/onsender.md)
  Coalesce notifications with the same object.
### Initializers
- [init(rawValue: UInt)](notificationqueue/notificationcoalescing/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [NotificationQueue.PostingStyle](notificationqueue/postingstyle.md)
  The constants that specify when notifications are posted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationqueue/notificationcoalescing)*