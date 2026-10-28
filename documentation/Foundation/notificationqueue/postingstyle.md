# NotificationQueue.PostingStyle

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum NSPostingStyle : NSUInteger;
```

## Overview

These constants are used by the [`enqueue(_:postingStyle:)`](./enqueue%28_,postingstyle%29.md) and [`enqueue(_:postingStyle:coalesceMask:forModes:)`](./enqueue%28_,postingstyle,coalescemask,formodes%29.md) methods.

## Topics

### Constants
- [NotificationQueue.PostingStyle.asap](./postingstyle/asap.md)
  The notification is posted at the end of the current notification callout or timer.
- [NotificationQueue.PostingStyle.whenIdle](./postingstyle/whenidle.md)
  The notification is posted when the run loop is idle.
- [NotificationQueue.PostingStyle.now](./postingstyle/now.md)
  The notification is posted immediately after coalescing.
### Initializers
- [init?(rawValue: UInt)](./postingstyle/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Constants
- [NotificationQueue.NotificationCoalescing](./notificationcoalescing.md)
  The constants that specify how notifications are coalesced.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationqueue/postingstyle)*