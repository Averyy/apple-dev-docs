# NotificationQueue.PostingStyle

**Framework**: Foundation  
**Kind**: enum

The constants that specify when notifications are posted.

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
enum PostingStyle
```

#### Overview

These constants are used by the [`enqueue(_:postingStyle:)`](notificationqueue/enqueue(_:postingstyle:).md) and [`enqueue(_:postingStyle:coalesceMask:forModes:)`](notificationqueue/enqueue(_:postingstyle:coalescemask:formodes:).md) methods.

## Topics

### Constants
- [NotificationQueue.PostingStyle.asap](notificationqueue/postingstyle/asap.md)
  The notification is posted at the end of the current notification callout or timer.
- [NotificationQueue.PostingStyle.whenIdle](notificationqueue/postingstyle/whenidle.md)
  The notification is posted when the run loop is idle.
- [NotificationQueue.PostingStyle.now](notificationqueue/postingstyle/now.md)
  The notification is posted immediately after coalescing.
### Initializers
- [init?(rawValue: UInt)](notificationqueue/postingstyle/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [NotificationQueue.NotificationCoalescing](notificationqueue/notificationcoalescing.md)
  The constants that specify how notifications are coalesced.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationqueue/postingstyle)*