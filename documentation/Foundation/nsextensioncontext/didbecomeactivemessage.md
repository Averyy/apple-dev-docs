# NSExtensionContext.DidBecomeActiveMessage

**Framework**: Foundation  
**Kind**: struct

A message the system sends when the extension’s host app moves from the inactive to the active state.

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
struct DidBecomeActiveMessage
```

#### Overview

You can use this message to adjust your extension’s activity when the host app becomes active.

Observe this message with the identifier [`didBecomeActive`](notificationcenter/messageidentifier/didbecomeactive-79dvm.md), or specify its type directly to the `addObserver(of:for:using:)` method. The [`Subject`](notificationcenter/mainactormessage/subject.md) of this message type is [`NSExtensionContext`](nsextensioncontext.md).

This message interoperates with the notification [`NSExtensionHostDidBecomeActive`](nsnotification/name-swift.struct/nsextensionhostdidbecomeactive.md). The system notifies observers of the message when the [`NotificationCenter`](notificationcenter.md) posts the notification. Similarly, the system notifies observers of the notification when it posts the message.

## Topics

### Creating a message for a host app becoming active
- [init()](nsextensioncontext/didbecomeactivemessage/init.md)
  Creates a message for a host app becoming active.

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](notificationcenter/mainactormessage.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [NSExtensionContext.WillResignActiveMessage](nsextensioncontext/willresignactivemessage.md)
  A message the system sends when the extension’s host app moves from the active to the inactive state.
- [NSExtensionContext.DidEnterBackgroundMessage](nsextensioncontext/didenterbackgroundmessage.md)
  A message the system sends when the extension’s host app begins running in the background.
- [NSExtensionContext.WillEnterForegroundMessage](nsextensioncontext/willenterforegroundmessage.md)
  A message the system sends when the extension’s host app begins running in the foreground.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsextensioncontext/didbecomeactivemessage)*