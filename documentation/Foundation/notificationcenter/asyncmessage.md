# NotificationCenter.AsyncMessage

**Framework**: Foundation  
**Kind**: protocol

A protocol for creating types that you can post to a notification center, which posts them to an arbitrary isolation.

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
protocol AsyncMessage : Sendable
```

#### Overview

You post types conforming to `AsyncMessage` to a notification center using `post(_:subject:)` and observe them with `addObserver(of:for:using:)`.

The notification center delivers `AsyncMessage` types asynchronously when posted. Asynchronous delivery isn’t suitable for messages with time-critical deliveries, such as a message that must have its observers called before a certain action takes place.

For types that post on the main actor, use [`NotificationCenter.MainActorMessage`](notificationcenter/mainactormessage.md).

Each `AsyncMessage` is associated with a specific `Subject` type.

For example, an `AsyncMessage` associated with the type `Event` could use the following declaration:

```swift
struct EventDidStart: NotificationCenter.AsyncMessage {
    typealias Subject = Event
}
```

`AsyncMessage` can use an optional [`NotificationCenter.MessageIdentifier`](notificationcenter/messageidentifier.md) type for context-aware observer registration:

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

`AsyncMessage` includes optional interoperability with [`Notification`](notification.md), enabling posters and observers of both types to pass information.

It does this by offering a [`makeMessage(_:)`](notificationcenter/asyncmessage/makemessage(_:).md) method that collects values from a [`Notification`](notification.md)‘s [`userInfo`](notification/userinfo.md) and populates properties on a new message. In the other direction, a [`makeNotification(_:)`](notificationcenter/asyncmessage/makenotification(_:).md) method collects the message’s defined properties and loads them into a new notification’s [`userInfo`](notification/userinfo.md) dictionary.

For example, if there exists a [`Notification`](notification.md) posted on an arbitrary isolation identified by the [`Notification.Name`](notification/name-swift.typealias.md) `"eventDidFinish"` with a [`userInfo`](notification/userinfo.md) dictionary containing the key `"duration"` as an [`NSNumber`](nsnumber.md), an app could post and observe the notification with the following [`NotificationCenter.AsyncMessage`](notificationcenter/asyncmessage.md):

```swift
struct EventDidFinish: NotificationCenter.AsyncMessage {
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

With this definition, an observer for this `AsyncMessage` type receives information even if the poster used the [`Notification`](notification.md) equivalent, and vice versa.

## Topics

### Declaring the message name and subject
- [static var name: Notification.Name](notificationcenter/asyncmessage/name.md)
  A optional name corresponding to this type, used to interoperate with notification posters and observers.
- [associatedtype Subject](notificationcenter/asyncmessage/subject.md)
  A type which you can optionally post and observe along with this `AsyncMessage`.
### Converting between messages and notifications
- [static func makeMessage(Notification) -> Self?](notificationcenter/asyncmessage/makemessage(_:).md)
  Converts a posted notification into this asynchronous message type for any observers.
- [static func makeNotification(Self) -> Notification](notificationcenter/asyncmessage/makenotification(_:).md)
  Converts a posted asynchronous message into a notification for any observers.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [Bundle.DidLoadMessage](bundle/didloadmessage.md)
- [Calendar.CalendarDayChangedMessage](calendar/calendardaychangedmessage.md)
- [FileHandle.ConnectionAcceptedMessage](filehandle/connectionacceptedmessage.md)
- [FileHandle.DataAvailableMessage](filehandle/dataavailablemessage.md)
- [FileHandle.ReadCompletionMessage](filehandle/readcompletionmessage.md)
- [FileHandle.ReadToEndOfFileCompletionMessage](filehandle/readtoendoffilecompletionmessage.md)
- [HTTPCookieStorage.CookiesChangedMessage](httpcookiestorage/cookieschangedmessage.md)
- [NSBundleResourceRequest.LowDiskSpaceMessage](nsbundleresourcerequest/lowdiskspacemessage.md)
- [NSMetadataQuery.DidFinishGatheringMessage](nsmetadataquery/didfinishgatheringmessage.md)
- [NSMetadataQuery.DidStartGatheringMessage](nsmetadataquery/didstartgatheringmessage.md)
- [Port.DidBecomeInvalidMessage](port/didbecomeinvalidmessage.md)
- [Process.DidTerminateMessage](process/didterminatemessage.md)
- [ProcessInfo.PowerStateDidChangeMessage](processinfo/powerstatedidchangemessage.md)
- [ProcessInfo.ThermalStateDidChangeMessage](processinfo/thermalstatedidchangemessage.md)
- [UserDefaults.DidChangeMessage](userdefaults/didchangemessage.md)

## See Also

- [NotificationCenter.MainActorMessage](notificationcenter/mainactormessage.md)
  A protocol for creating types that you can post to a notification center and bind to the main actor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/asyncmessage)*