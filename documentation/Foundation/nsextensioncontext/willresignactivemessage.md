# NSExtensionContext.WillResignActiveMessage

**Framework**: Foundation  
**Kind**: struct

A message the system sends when the extension’s host app moves from the active to the inactive state.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct WillResignActiveMessage
```

#### Overview

Your extension can use this message to adjust the extension’s activity when it becomes inactive. For example, you might use this message to save any unsaved data to prevent it from being lost.

Observe this message with the identifier [`willResignActive`](notificationcenter/messageidentifier/willresignactive-9z4xc.md), or specify its type directly to the `addObserver(of:for:using:)` method. The [`Subject`](notificationcenter/mainactormessage/subject.md) of this message type is [`NSExtensionContext`](nsextensioncontext.md).

This message interoperates with the notification [`NSExtensionHostWillResignActive`](nsnotification/name-swift.struct/nsextensionhostwillresignactive.md). The system notifies observers of the message when the [`NotificationCenter`](notificationcenter.md) posts the notification. Similarly, the system notifies observers of the notification when it posts the message.

## Topics

### Creating a message for a host app becoming inactive
- [init()](nsextensioncontext/willresignactivemessage/init.md)
  Creates a message for a host app becoming inactive.

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](notificationcenter/mainactormessage.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [NSExtensionContext.DidBecomeActiveMessage](nsextensioncontext/didbecomeactivemessage.md)
  A message the system sends when the extension’s host app moves from the inactive to the active state.
- [NSExtensionContext.DidEnterBackgroundMessage](nsextensioncontext/didenterbackgroundmessage.md)
  A message the system sends when the extension’s host app begins running in the background.
- [NSExtensionContext.WillEnterForegroundMessage](nsextensioncontext/willenterforegroundmessage.md)
  A message the system sends when the extension’s host app begins running in the foreground.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsextensioncontext/willresignactivemessage)*