# NotificationCenter.MainActorMessage

**Framework**: Foundation  
**Kind**: protocol  
**Role**: Protocol

A protocol for creating types that you can post to a notification center and bind to the main actor.

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
protocol MainActorMessage : SendableMetatype
```

## Overview

You post types conforming to  `MainActorMessage` to a notification center using `post(_:subject:)` and observe them with `addObserver(of:for:using:)`. The notification center delivers `MainActorMessage` types synchronously when posted.

For types that post on an arbitrary isolation, use [`NotificationCenter.AsyncMessage`](./asyncmessage.md).

Each `MainActorMessage` is associated with a specific `Subject` type.

For example, a `MainActorMessage` associated with the type `Event` could use the following declaration:

```swift
struct EventDidStart: NotificationCenter.MainActorMessage {
    typealias Subject = Event
}
```

`MainActorMessage` can use an optional [`NotificationCenter.MessageIdentifier`](./messageidentifier.md) type for context-aware observer registration:

```swift
extension NotificationCenter.MessageIdentifier where Self == NotificationCenter.BaseMessageIdentifier<EventDidStart> {
    static var didStart: Self { .init() }
}
```

With this identifier, observers can receive information about a specific instance by registering for this message with a [`NotificationCenter`](../notificationcenter.md):

```swift
let observerToken = NotificationCenter.default.addObserver(of: importantEvent, for: .didStart)
```

Or an observer can receive information about any instance with:

```swift
let observerToken = NotificationCenter.default.addObserver(of: Event.self, for: .didStart)
```

The notification center ties observation the lifetime of the returned [`NotificationCenter.ObservationToken`](./observationtoken.md) and automatically de-registers the observer if the token goes out of scope. You can also remove observation explicitly:

```swift
NotificationCenter.default.removeObserver(observerToken)
```

## Topics

### Declaring the message name and subject
- [static var name: Notification.Name](./mainactormessage/name.md)
  A optional name corresponding to this type, used to interoperate with notification posters and observers.
- [associatedtype Subject](./mainactormessage/subject.md)
  A type which you can optionally post and observe along with this `MainActorMessage`.
### Converting between messages and notifications
- [static func makeMessage(Notification) -> Self?](./mainactormessage/makemessage%28_%29.md)
  Converts a posted notification into this main actor message type for any observers.
- [static func makeNotification(Self) -> Notification](./mainactormessage/makenotification%28_%29.md)
  Converts a posted main actor message into a notification for any observers.

## Relationships

### Inherits From
- [SendableMetatype](../../Swift/sendablemetatype.md)
### Conforming Types
- [Date.SystemClockDidChangeMessage](../date/systemclockdidchangemessage.md)
- [FileManager.UbiquityIdentityDidChangeMessage](../filemanager/ubiquityidentitydidchangemessage.md)
- [Locale.CurrentLocaleDidChangeMessage](../locale/currentlocaledidchangemessage.md)
- [NSExtensionContext.DidBecomeActiveMessage](../nsextensioncontext/didbecomeactivemessage.md)
- [NSExtensionContext.DidEnterBackgroundMessage](../nsextensioncontext/didenterbackgroundmessage.md)
- [NSExtensionContext.WillEnterForegroundMessage](../nsextensioncontext/willenterforegroundmessage.md)
- [NSExtensionContext.WillResignActiveMessage](../nsextensioncontext/willresignactivemessage.md)
- [TimeZone.SystemTimeZoneDidChangeMessage](../timezone/systemtimezonedidchangemessage.md)
- [UndoManager.CheckpointMessage](../undomanager/checkpointmessage.md)
- [UndoManager.DidCloseUndoGroupMessage](../undomanager/didcloseundogroupmessage.md)
- [UndoManager.DidOpenUndoGroupMessage](../undomanager/didopenundogroupmessage.md)
- [UndoManager.DidRedoChangeMessage](../undomanager/didredochangemessage.md)
- [UndoManager.DidUndoChangeMessage](../undomanager/didundochangemessage.md)
- [UndoManager.WillCloseUndoGroupMessage](../undomanager/willcloseundogroupmessage.md)
- [UndoManager.WillRedoChangeMessage](../undomanager/willredochangemessage.md)
- [UndoManager.WillUndoChangeMessage](../undomanager/willundochangemessage.md)
- [UserDefaults.SizeLimitExceededMessage](../userdefaults/sizelimitexceededmessage.md)

## See Also

### Declaring a message
- [NotificationCenter.AsyncMessage](./asyncmessage.md)
  A protocol for creating types that you can post to a notification center, which posts them to an arbitrary isolation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/mainactormessage)*