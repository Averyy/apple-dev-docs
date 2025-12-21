# NotificationCenter.MainActorMessage

**Framework**: Foundation  
**Kind**: protocol

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

#### Overview

You post types conforming to  `MainActorMessage` to a notification center using `post(_:subject:)` and observe them with `addObserver(of:for:using:)`. The notification center delivers `MainActorMessage` types synchronously when posted.

For types that post on an arbitrary isolation, use [`NotificationCenter.AsyncMessage`](notificationcenter/asyncmessage.md).

Each `MainActorMessage` is associated with a specific `Subject` type.

For example, a `MainActorMessage` associated with the type `Event` could use the following declaration:

```swift
struct EventDidStart: NotificationCenter.MainActorMessage {
    typealias Subject = Event
}
```

`MainActorMessage` can use an optional [`NotificationCenter.MessageIdentifier`](notificationcenter/messageidentifier.md) type for context-aware observer registration:

```swift
extension NotificationCenter.MessageIdentifier where Self == NotificationCenter.BaseMessageIdentifier<EventDidStart> {
    static var didStart: Self { .init() }
}
```

With this identifier, observers can receive information about a specific instance by registering for this message with a [`NotificationCenter`](notificationcenter.md):

```swift
let observerToken = NotificationCenter.default.addObserver(of: importantEvent, for: .didStart)
```

Or an observer can receive information about any instance with:

```swift
let observerToken = NotificationCenter.default.addObserver(of: Event.self, for: .didStart)
```

The notification center ties observation the lifetime of the returned [`NotificationCenter.ObservationToken`](notificationcenter/observationtoken.md) and automatically de-registers the observer if the token goes out of scope. You can also remove observation explicitly:

```swift
NotificationCenter.default.removeObserver(observerToken)
```

##### Notification Interoperability

`MainActorMessage` includes optional interoperability with [`Notification`](notification.md), enabling posters and observers of both types to pass information.

It does this by offering a [`makeMessage(_:)`](notificationcenter/mainactormessage/makemessage(_:).md) method that collects values from a [`Notification`](notification.md)‘s [`userInfo`](notification/userinfo.md) and populates properties on a new message. In the other direction, a [`makeNotification(_:)`](notificationcenter/mainactormessage/makenotification(_:).md) method collects the message’s defined properties and loads them into a new notification’s [`userInfo`](notification/userinfo.md) dictionary.

For example, if there exists a [`Notification`](notification.md) posted on `MainActor` identified by the [`Notification.Name`](notification/name-swift.typealias.md) `"eventDidFinish"` with a [`userInfo`](notification/userinfo.md) dictionary containing the key `"duration"` as an [`NSNumber`](nsnumber.md), an app could post and observe the notification with the following [`NotificationCenter.MainActorMessage`](notificationcenter/mainactormessage.md):

```swift
struct EventDidFinish: NotificationCenter.MainActorMessage {
    typealias Subject = Event
    static var name: Notification.Name { Notification.Name("eventDidFinish") }

    var duration: Int

    static func makeNotification(_ message: Self) -> Notification {
        return Notification(name: Self.name, userInfo: ["duration": NSNumber(message.duration)])
    }

    static func makeMessage(_ notification: Notification) -> Self? {
        guard let userInfo = notification.userInfo,
              let duration = userInfo["duration"] as? Int
        else {
            return nil
        }

        return Self(duration: duration)
    }
}
```

With this definition, an observer for this `MainActorMessage` type receives information even if the poster used the [`Notification`](notification.md) equivalent, and vice versa.

## Topics

### Declaring the message name and subject
- [static var name: Notification.Name](notificationcenter/mainactormessage/name.md)
  A optional name corresponding to this type, used to interoperate with notification posters and observers.
- [associatedtype Subject](notificationcenter/mainactormessage/subject.md)
  A type which you can optionally post and observe along with this `MainActorMessage`.
### Converting between messages and notifications
- [static func makeMessage(Notification) -> Self?](notificationcenter/mainactormessage/makemessage(_:).md)
  Converts a posted notification into this main actor message type for any observers.
- [static func makeNotification(Self) -> Notification](notificationcenter/mainactormessage/makenotification(_:).md)
  Converts a posted main actor message into a notification for any observers.

## Relationships

### Inherits From
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [Date.SystemClockDidChangeMessage](date/systemclockdidchangemessage.md)
- [FileManager.UbiquityIdentityDidChangeMessage](filemanager/ubiquityidentitydidchangemessage.md)
- [Locale.CurrentLocaleDidChangeMessage](locale/currentlocaledidchangemessage.md)
- [NSExtensionContext.DidBecomeActiveMessage](nsextensioncontext/didbecomeactivemessage.md)
- [NSExtensionContext.DidEnterBackgroundMessage](nsextensioncontext/didenterbackgroundmessage.md)
- [NSExtensionContext.WillEnterForegroundMessage](nsextensioncontext/willenterforegroundmessage.md)
- [NSExtensionContext.WillResignActiveMessage](nsextensioncontext/willresignactivemessage.md)
- [TimeZone.SystemTimeZoneDidChangeMessage](timezone/systemtimezonedidchangemessage.md)
- [UndoManager.CheckpointMessage](undomanager/checkpointmessage.md)
- [UndoManager.DidCloseUndoGroupMessage](undomanager/didcloseundogroupmessage.md)
- [UndoManager.DidOpenUndoGroupMessage](undomanager/didopenundogroupmessage.md)
- [UndoManager.DidRedoChangeMessage](undomanager/didredochangemessage.md)
- [UndoManager.DidUndoChangeMessage](undomanager/didundochangemessage.md)
- [UndoManager.WillCloseUndoGroupMessage](undomanager/willcloseundogroupmessage.md)
- [UndoManager.WillRedoChangeMessage](undomanager/willredochangemessage.md)
- [UndoManager.WillUndoChangeMessage](undomanager/willundochangemessage.md)
- [UserDefaults.SizeLimitExceededMessage](userdefaults/sizelimitexceededmessage.md)

## See Also

- [NotificationCenter.AsyncMessage](notificationcenter/asyncmessage.md)
  A protocol for creating types that you can post to a notification center, which posts them to an arbitrary isolation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/mainactormessage)*