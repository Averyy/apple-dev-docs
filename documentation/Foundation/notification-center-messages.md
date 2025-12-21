# Notification center messages

**Framework**: Foundation

Use Foundation’s notification center with Swift concurrency.

#### Overview

In Swift, the [`Notification`](notification.md) type is `nonisolated`, even in cases where it’s posted on a known isolation. To provide specific isolation information and better support Swift concurrency, `NotificationCenter` defines two message types. A [`NotificationCenter.MainActorMessage`](notificationcenter/mainactormessage.md) binds to the main actor, whereas a [`NotificationCenter.AsyncMessage`](notificationcenter/asyncmessage.md) uses an arbitrary isolation. Frameworks extend these types to define distinct messages, typically corresponding to an existing [`Notification.Name`](notification/name-swift.typealias.md), that declare instance properties for their values instead of using a `userInfo` dictionary. As a result, messages can conform to [`Sendable`](https://developer.apple.com/documentation/Swift/Sendable) when they either don’t use properties or contain only sendable properties.

If your project only needs to support Swift, you can just use the `Message` types. For projects with both Objective-C and Swift code, define a [`Notification`](notification.md) as well as a corresponding `Message` type.

##### Posting and Observing Messages

You can post a message with the `post(_:subject:)` method, passing a message instance and optionally providing a subject. To receive messages, add an observer with the `addObserver(of:for:using:)` method. The overloads of this method allow you to observe either messages from a single object or from any object of a given type. Observation ends when you discard the token returned from `addObserver(of:for:using:)` or after an explicit call to [`removeObserver(_:)`](notificationcenter/removeobserver(_:)-2gmm0.md).

You can also receive messages as an [`AsyncSequence`](https://developer.apple.com/documentation/Swift/AsyncSequence) with the `messages(of:for:bufferSize:)` methods.

Several flavors of `addObserver(of:for:using:)` and `messages(of:for:bufferSize:)` take a [`NotificationCenter.MessageIdentifier`](notificationcenter/messageidentifier.md), which frameworks may implement to provide a typed, ergonomic experience at the call point for convenience, as described in [`SE-0299`](https://developer.apple.comhttps://github.com/swiftlang/swift-evolution/blob/main/proposals/0299-extend-generic-static-member-lookup.md).

##### Using Messages with the Sdk

Many system frameworks — including Foundation, UIKit, and AppKit — adopt the [`NotificationCenter.MainActorMessage`](notificationcenter/mainactormessage.md) and [`NotificationCenter.AsyncMessage`](notificationcenter/asyncmessage.md) types to facilitate using their notifications in concurrency-safe Swift code. The following example shows how to observe Foundation’s [`TimeZone`](timezone.md) type for the [`systemTimeZoneDidChange`](notificationcenter/messageidentifier/systemtimezonedidchange.md) message, which contains the property [`previousTimeZone`](timezone/systemtimezonedidchangemessage/previoustimezone.md).

```None
/// Note: Store `token` in a property for as long as you intend to observe.
token = NotificationCenter.default.addObserver(of: TimeZone.self,
                                               for: .systemTimeZoneDidChange)
{ message in
    let identifier = message.previousTimeZone?.identifier ?? "(unknown)"
    print("Time zone changed from \(identifier).")
}
```

For use with existing notification code, [`NotificationCenter.MainActorMessage`](notificationcenter/mainactormessage.md) and [`NotificationCenter.AsyncMessage`](notificationcenter/asyncmessage.md) define helper methods that conforming types implement to convert a message to a corresponding notification and vice versa.

## Topics

### Declaring a message
- [NotificationCenter.MainActorMessage](notificationcenter/mainactormessage.md)
  A protocol for creating types that you can post to a notification center and bind to the main actor.
- [NotificationCenter.AsyncMessage](notificationcenter/asyncmessage.md)
  A protocol for creating types that you can post to a notification center, which posts them to an arbitrary isolation.
### Using message identifiers
- [NotificationCenter.MessageIdentifier](notificationcenter/messageidentifier.md)
  An optional identifier to associate a given message with a given type.
- [NotificationCenter.BaseMessageIdentifier](notificationcenter/basemessageidentifier.md)
  A type for use when defining optional Message identifiers.
### Observing concurrency-safe notifications
- [func addObserver<Identifier, Message>(of: Message.Subject, for: Identifier, using: (Message) -> Void) -> NotificationCenter.ObservationToken](notificationcenter/addobserver(of:for:using:)-4d19x.md)
  Adds an observer to a center for messages delivered on the main actor with a given subject and identifier.
- [func addObserver<Identifier, Message>(of: Message.Subject.Type, for: Identifier, using: (Message) -> Void) -> NotificationCenter.ObservationToken](notificationcenter/addobserver(of:for:using:)-90os.md)
  Adds an observer to a center for messages delivered on the main actor with a given subject and identifier.
- [func addObserver<Message>(of: Message.Subject?, for: Message.Type, using: (Message) -> Void) -> NotificationCenter.ObservationToken](notificationcenter/addobserver(of:for:using:)-56bn4.md)
  Adds an observer to a center for messages delivered on the main actor with a given subject and message type.
- [func addObserver<Identifier, Message>(of: Message.Subject, for: Identifier, using: (Message) async -> Void) -> NotificationCenter.ObservationToken](notificationcenter/addobserver(of:for:using:)-twm3.md)
  Adds an observer to a center for messages delivered asynchronously with a given subject and identifier.
- [func addObserver<Identifier, Message>(of: Message.Subject.Type, for: Identifier, using: (Message) async -> Void) -> NotificationCenter.ObservationToken](notificationcenter/addobserver(of:for:using:)-t1wr.md)
  Adds an observer to a center for messages delivered asynchronously with a given subject and message type.
- [func addObserver<Message>(of: Message.Subject?, for: Message.Type, using: (Message) async -> Void) -> NotificationCenter.ObservationToken](notificationcenter/addobserver(of:for:using:)-64uw3.md)
  Adds an observer to a center for messages delivered asynchronously with a given subject and message type.
- [func removeObserver(NotificationCenter.ObservationToken)](notificationcenter/removeobserver(_:)-2gmm0.md)
  Stops the observation represented by the given observation token.
- [NotificationCenter.ObservationToken](notificationcenter/observationtoken.md)
  A unique token representing a single observer registration in a notification center.
### Receiving notifications as asynchronous sequences
- [func messages<Identifier, Message>(of: Message.Subject, for: Identifier, bufferSize: Int) -> some Sendable & AsyncSequence<Message, Never>
](notificationcenter/messages(of:for:buffersize:)-4tof0.md)
  Returns an asynchronous sequence of messages produced by this center for a given subject and identifier.
- [func messages<Identifier, Message>(of: Message.Subject.Type, for: Identifier, bufferSize: Int) -> some Sendable & AsyncSequence<Message, Never>
](notificationcenter/messages(of:for:buffersize:)-1ub69.md)
  Returns an asynchronous sequence of messages produced by this center for a given subject type and identifier.
- [func messages<Message>(of: Message.Subject?, for: Message.Type, bufferSize: Int) -> some Sendable & AsyncSequence<Message, Never>
](notificationcenter/messages(of:for:buffersize:)-623kg.md)
  Returns an asynchronous sequence of messages produced by this center for a given subject and message type.
### Posting notification messages
- [func post<Message>(Message, subject: Message.Subject)](notificationcenter/post(_:subject:)-87dbk.md)
  Posts a given main actor message to the notification center.
- [func post<Message>(Message)](notificationcenter/post(_:)-19s7b.md)
  Posts a given main actor message to the notification center.
- [func post<Message>(Message, subject: Message.Subject)](notificationcenter/post(_:subject:)-5271w.md)
  Posts a given asynchronous message to the notification center.
- [func post<Message>(Message)](notificationcenter/post(_:)-7ia4j.md)
  Posts a given asynchronous message to the notification center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notification-center-messages)*