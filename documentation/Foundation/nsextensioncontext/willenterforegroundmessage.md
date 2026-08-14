# NSExtensionContext.WillEnterForegroundMessage

**Framework**: Foundation  
**Kind**: struct

A message the system sends when the extension’s host app begins running in the foreground.

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
struct WillEnterForegroundMessage
```

#### Overview

Your extension can use this message to restart tasks that it stopped when the app moved to the background.

Observe this message with the identifier [`willEnterForeground`](notificationcenter/messageidentifier/willenterforeground-p1og.md), or specify its type directly to the `addObserver(of:for:using:)` method. The [`Subject`](notificationcenter/mainactormessage/subject.md) of this message type is [`NSExtensionContext`](nsextensioncontext.md).

This message interoperates with the notification [`NSExtensionHostWillEnterForeground`](nsnotification/name-swift.struct/nsextensionhostwillenterforeground.md). The system notifies observers of the message when the [`NotificationCenter`](notificationcenter.md) posts the notification. Similarly, the system notifies observers of the notification when it posts the message.

## Topics

### Creating a message for a host app entering the foreground
- [init()](nsextensioncontext/willenterforegroundmessage/init.md)
  Creates a message for a host app entering the foreground.

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](notificationcenter/mainactormessage.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [NSExtensionContext.DidBecomeActiveMessage](nsextensioncontext/didbecomeactivemessage.md)
  A message the system sends when the extension’s host app moves from the inactive to the active state.
- [NSExtensionContext.WillResignActiveMessage](nsextensioncontext/willresignactivemessage.md)
  A message the system sends when the extension’s host app moves from the active to the inactive state.
- [NSExtensionContext.DidEnterBackgroundMessage](nsextensioncontext/didenterbackgroundmessage.md)
  A message the system sends when the extension’s host app begins running in the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsextensioncontext/willenterforegroundmessage)*