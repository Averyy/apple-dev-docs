# Locale.CurrentLocaleDidChangeMessage

**Framework**: Foundation  
**Kind**: struct

A message the system sends when the current locale changes.

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
struct CurrentLocaleDidChangeMessage
```

#### Overview

Register an observer for this message if your app displays content that’s affected by the current locale, such as dates, times, numbers, and so on. Use the message to trigger updates to your app’s interface.

Observe this message with the identifier [`currentLocaleDidChange`](notificationcenter/messageidentifier/currentlocaledidchange.md), or specify its type directly to the `addObserver(of:for:using:)` method. The [`Subject`](notificationcenter/mainactormessage/subject.md) of this message type is [`Locale`](locale.md).

This message interoperates with the notification [`currentLocaleDidChangeNotification`](nslocale/currentlocaledidchangenotification.md). The system notifies observers of the message when the [`NotificationCenter`](notificationcenter.md) posts the notification. Similarly, the system notifies observers of the notification when it posts the message.

## Topics

### Creating a message for a change in locale
- [init()](locale/currentlocaledidchangemessage/init.md)
  Creates a message for the change in current locale.

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](notificationcenter/mainactormessage.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/currentlocaledidchangemessage)*