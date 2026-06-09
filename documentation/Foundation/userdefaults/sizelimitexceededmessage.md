# UserDefaults.SizeLimitExceededMessage

**Framework**: Foundation  
**Kind**: struct

A message the system sends when the size of the data in the defaults database exceeds the maximum.

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
struct SizeLimitExceededMessage
```

#### Overview

In tvOS, the system posts this message as a warning when the size of your app’s defaults database reaches 512 kilobytes. If your app continues to write to the defaults database, the system terminates your app when the database reaches or exceeds 1 megabyte in size.

The system doesn’t post size exceeded messages for platforms other than tvOS. The system posts this message on your app’s main thread.

Observe this message with the identifier [`sizeLimitExceeded`](notificationcenter/messageidentifier/sizelimitexceeded.md), or specify its type directly to the `addObserver(of:for:using:)` method. The [`Subject`](notificationcenter/mainactormessage/subject.md) of this message type is [`UserDefaults`](userdefaults.md).

This message interoperates with the notification [`sizeLimitExceededNotification`](userdefaults/sizelimitexceedednotification.md). The system notifies observers of the message when the [`NotificationCenter`](notificationcenter.md) posts the notification. Similarly, the system notifies observers of the notification when it posts the message.

## Topics

### Creating a message
- [init()](userdefaults/sizelimitexceededmessage/init.md)
  Creates a message when the user defaults database of a tvOS app exceeds its maximum size.

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](notificationcenter/mainactormessage.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [UserDefaults.DidChangeMessage](userdefaults/didchangemessage.md)
  A message the system sends when a user-defaults setting changes.
- [class let didChangeNotification: NSNotification.Name](userdefaults/didchangenotification.md)
  Posted when the current process changes the value of a setting.
- [class let sizeLimitExceededNotification: NSNotification.Name](userdefaults/sizelimitexceedednotification.md)
  Posted when the amount of data in the defaults database exceeds the allowed maximum.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/sizelimitexceededmessage)*