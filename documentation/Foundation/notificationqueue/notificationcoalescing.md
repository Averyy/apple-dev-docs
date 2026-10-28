# NotificationQueue.NotificationCoalescing

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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

```c
enum NSNotificationCoalescing : NSUInteger;
```

## Overview

These constants are used by the [`enqueue(_:postingStyle:coalesceMask:forModes:)`](./enqueue%28_,postingstyle,coalescemask,formodes%29.md) method.

## Topics

### Constants
- [static var none: NotificationQueue.NotificationCoalescing](./notificationcoalescing/none.md)
  Do not coalesce notifications in the queue.
- [static var onName: NotificationQueue.NotificationCoalescing](./notificationcoalescing/onname.md)
  Coalesce notifications with the same name.
- [static var onSender: NotificationQueue.NotificationCoalescing](./notificationcoalescing/onsender.md)
  Coalesce notifications with the same object.
### Initializers
- [init(rawValue: UInt)](./notificationcoalescing/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Constants
- [NotificationQueue.PostingStyle](./postingstyle.md)
  The constants that specify when notifications are posted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationqueue/notificationcoalescing)*