# addObserver(of:for:using:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Adds an observer to a center for messages delivered asynchronously with a given subject and message type.

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
func addObserver<Identifier, Message>(of subject: Message.Subject.Type, for identifier: Identifier, using observer: @escaping @Sendable (Message) async -> Void) -> NotificationCenter.ObservationToken where Identifier : NotificationCenter.MessageIdentifier, Message : NotificationCenter.AsyncMessage, Message == Identifier.MessageType
```

## Return Value

A token representing the observation registration with the given notification center. Retain this token for as long as you need to receive messages.

## Parameters

- `subject`: The metatype to observe all values for a given type.
- `identifier`: An identifier representing a specific message type.
- `observer`: A closure to execute when receving a message.

## See Also

### Observing concurrency-safe notifications
- [func addObserver<Identifier, Message>(of: Message.Subject, for: Identifier, using: (Message) -> Void) -> NotificationCenter.ObservationToken](./addobserver%28of,for,using%29-4d19x.md)
  Adds an observer to a center for messages delivered on the main actor with a given subject and identifier.
- [func addObserver<Identifier, Message>(of: Message.Subject.Type, for: Identifier, using: (Message) -> Void) -> NotificationCenter.ObservationToken](./addobserver%28of,for,using%29-90os.md)
  Adds an observer to a center for messages delivered on the main actor with a given subject and identifier.
- [func addObserver<Message>(of: Message.Subject?, for: Message.Type, using: (Message) -> Void) -> NotificationCenter.ObservationToken](./addobserver%28of,for,using%29-56bn4.md)
  Adds an observer to a center for messages delivered on the main actor with a given subject and message type.
- [func addObserver<Identifier, Message>(of: Message.Subject, for: Identifier, using: (Message) async -> Void) -> NotificationCenter.ObservationToken](./addobserver%28of,for,using%29-twm3.md)
  Adds an observer to a center for messages delivered asynchronously with a given subject and identifier.
- [func addObserver<Message>(of: Message.Subject?, for: Message.Type, using: (Message) async -> Void) -> NotificationCenter.ObservationToken](./addobserver%28of,for,using%29-64uw3.md)
  Adds an observer to a center for messages delivered asynchronously with a given subject and message type.
- [func removeObserver(NotificationCenter.ObservationToken)](./removeobserver%28_%29-2gmm0.md)
  Stops the observation represented by the given observation token.
- [NotificationCenter.ObservationToken](./observationtoken.md)
  A unique token representing a single observer registration in a notification center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/addobserver(of:for:using:)-t1wr)*