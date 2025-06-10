# CFNotificationSuspensionBehavior

**Framework**: Core Foundation  
**Kind**: enum

Suspension flags that indicate how distributed notifications should be handled when the receiving application is in the background.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum CFNotificationSuspensionBehavior
```

#### Overview

An application selects the suspension behavior for a given notification when it registers an observer for that notification with [`CFNotificationCenterAddObserver(_:_:_:_:_:_:)`](cfnotificationcenteraddobserver(_:_:_:_:_:_:).md).

## Topics

### Constants
- [CFNotificationSuspensionBehavior.drop](cfnotificationsuspensionbehavior/drop.md)
  The server will not queue any notifications of the specified name and object while the receiving application is in the background.
- [CFNotificationSuspensionBehavior.coalesce](cfnotificationsuspensionbehavior/coalesce.md)
  The server will only queue the last notification of the specified name and object; earlier notifications are dropped.
- [CFNotificationSuspensionBehavior.hold](cfnotificationsuspensionbehavior/hold.md)
  The server will hold all matching notifications until the queue has been filled (queue size determined by the server) at which point the server may flush queued notifications.
- [CFNotificationSuspensionBehavior.deliverImmediately](cfnotificationsuspensionbehavior/deliverimmediately.md)
  The server will deliver notifications of the specified name and object whether or not the application is in the background. When a notification with this suspension behavior is matched, it has the effect of first flushing any queued notifications.
### Initializers
- [init?(rawValue: CFIndex)](cfnotificationsuspensionbehavior/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Notification Posting Options](1569610-notification-posting-options.md)
  Possible options when posting notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfnotificationsuspensionbehavior)*