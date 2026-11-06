# NotificationCenter.AsyncMessage

**Framework**: Foundation  
**Kind**: protocol  
**Role**: Protocol

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

## Overview

You post types conforming to `AsyncMessage` to a notification center using `post(_:subject:)` and observe them with `addObserver(of:for:using:)`.

The notification center delivers `AsyncMessage` types asynchronously when posted. Asynchronous delivery isn’t suitable for messages with time-critical deliveries, such as a message that must have its observers called before a certain action takes place.

For types that post on the main actor, use [`NotificationCenter.MainActorMessage`](./mainactormessage.md).

Each `AsyncMessage` is associated with a specific `Subject` type.

For example, an `AsyncMessage` associated with the type `Event` could use the following declaration:

```swift
struct EventDidStart: NotificationCenter.AsyncMessage {
    typealias Subject = Event
}
```

`AsyncMessage` can use an optional [`NotificationCenter.MessageIdentifier`](./messageidentifier.md) type for context-aware observer registration:

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
- [static var name: Notification.Name](./asyncmessage/name.md)
  A optional name corresponding to this type, used to interoperate with notification posters and observers.
- [associatedtype Subject](./asyncmessage/subject.md)
  A type which you can optionally post and observe along with this `AsyncMessage`.
### Converting between messages and notifications
- [static func makeMessage(Notification) -> Self?](./asyncmessage/makemessage%28_%29.md)
  Converts a posted notification into this asynchronous message type for any observers.
- [static func makeNotification(Self) -> Notification](./asyncmessage/makenotification%28_%29.md)
  Converts a posted asynchronous message into a notification for any observers.

## Relationships

### Inherits From
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
### Conforming Types
- [Bundle.DidLoadMessage](../bundle/didloadmessage.md)
- [Calendar.CalendarDayChangedMessage](../calendar/calendardaychangedmessage.md)
- [FileHandle.ConnectionAcceptedMessage](../filehandle/connectionacceptedmessage.md)
- [FileHandle.DataAvailableMessage](../filehandle/dataavailablemessage.md)
- [FileHandle.ReadCompletionMessage](../filehandle/readcompletionmessage.md)
- [FileHandle.ReadToEndOfFileCompletionMessage](../filehandle/readtoendoffilecompletionmessage.md)
- [HTTPCookieStorage.CookiesChangedMessage](../httpcookiestorage/cookieschangedmessage.md)
- [NSBundleResourceRequest.LowDiskSpaceMessage](../nsbundleresourcerequest/lowdiskspacemessage.md)
- [NSMetadataQuery.DidFinishGatheringMessage](../nsmetadataquery/didfinishgatheringmessage.md)
- [NSMetadataQuery.DidStartGatheringMessage](../nsmetadataquery/didstartgatheringmessage.md)
- [Port.DidBecomeInvalidMessage](../port/didbecomeinvalidmessage.md)
- [Process.DidTerminateMessage](../process/didterminatemessage.md)
- [ProcessInfo.PowerStateDidChangeMessage](../processinfo/powerstatedidchangemessage.md)
- [ProcessInfo.ThermalStateDidChangeMessage](../processinfo/thermalstatedidchangemessage.md)
- [UserDefaults.DidChangeMessage](../userdefaults/didchangemessage.md)

## See Also

### Declaring a message
- [NotificationCenter.MainActorMessage](./mainactormessage.md)
  A protocol for creating types that you can post to a notification center and bind to the main actor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/asyncmessage)*