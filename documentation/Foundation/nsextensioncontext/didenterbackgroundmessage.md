# NSExtensionContext.DidEnterBackgroundMessage

**Framework**: Foundation  
**Kind**: struct

A message the system sends when the extension’s host app begins running in the background.

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
struct DidEnterBackgroundMessage
```

#### Overview

You can use this message in your extension to stop tasks and prepare for the system to suspend the extension.

Extensions receive only a short amount of time to perform any background work. If you need more time to complete critical tasks, use the methods of the [`ProcessInfo`](processinfo.md) class to request that time.

Observe this message with the identifier [`didEnterBackground`](notificationcenter/messageidentifier/didenterbackground-5gdtk.md), or specify its type directly to the `addObserver(of:for:using:)` method. The [`Subject`](notificationcenter/mainactormessage/subject.md) of this message type is [`NSExtensionContext`](nsextensioncontext.md).

This message interoperates with the notification [`NSExtensionHostDidEnterBackground`](nsnotification/name-swift.struct/nsextensionhostdidenterbackground.md). The system notifies observers of the message when the [`NotificationCenter`](notificationcenter.md) posts the notification. Similarly, the system notifies observers of the notification when it posts the message.

## Topics

### Creating a message for a host app entering the background
- [init()](nsextensioncontext/didenterbackgroundmessage/init.md)
  Creates a message for a host app entering the background.

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](notificationcenter/mainactormessage.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [NSExtensionContext.DidBecomeActiveMessage](nsextensioncontext/didbecomeactivemessage.md)
  A message the system sends when the extension’s host app moves from the inactive to the active state.
- [NSExtensionContext.WillResignActiveMessage](nsextensioncontext/willresignactivemessage.md)
  A message the system sends when the extension’s host app moves from the active to the inactive state.
- [NSExtensionContext.WillEnterForegroundMessage](nsextensioncontext/willenterforegroundmessage.md)
  A message the system sends when the extension’s host app begins running in the foreground.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsextensioncontext/didenterbackgroundmessage)*