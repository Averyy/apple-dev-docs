# Bundle.DidLoadMessage

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

A message a bundle sends when it dynamically loads a class.

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
struct DidLoadMessage
```

#### Overview

When a bundle handles a request to load a class with [`classNamed(_:)`](./classnamed%28_%29.md) or  [`principalClass`](./principalclass.md), the bundle dynamically loads the executable code file that contains the class implementation and all other class definitions contained in the file. After module loading completes, the bundle posts this message.

Observe this message with the identifier [`didLoad`](../notificationcenter/messageidentifier/didload.md), or specify its type directly to the `addObserver(of:for:using:)` method. The [`Subject`](../notificationcenter/mainactormessage/subject.md) of this message type is [`Bundle`](../bundle.md).

This message interoperates with the notification [`didLoadNotification`](./didloadnotification.md). The system notifies observers of the message when the [`NotificationCenter`](../notificationcenter.md) posts the notification. Similarly, the system notifies observers of the notification when it posts the message.

## Topics

### Creating a message
- [init()](./didloadmessage/init%28%29.md)
  Creates a message that indicates a bundle dynamically loaded a class.

## Relationships

### Conforms To
- [NotificationCenter.AsyncMessage](../notificationcenter/asyncmessage.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting classes from a bundle
- [func classNamed(String) -> AnyClass?](./classnamed%28_%29.md)
  Returns the `Class` object for the specified name.
- [var principalClass: AnyClass?](./principalclass.md)
  The bundle’s principal class.
- [class let didLoadNotification: NSNotification.Name](./didloadnotification.md)
  A notification that lets observers know when classes are dynamically loaded.
- [let NSLoadedClasses: String](../nsloadedclasses.md)
  A constant used as a key for the `userInfo` dictionary of a [`didLoadNotification`](./didloadnotification.md) notification that corresponds to an array of names of each class that was loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bundle/didloadmessage)*