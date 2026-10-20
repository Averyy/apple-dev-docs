# addObserver(of:for:using:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Adds an observer to a center for messages delivered on the main actor with a given subject and message type.

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
func addObserver<Message>(of subject: Message.Subject? = nil, for messageType: Message.Type, using observer: @escaping @MainActor (Message) -> Void) -> NotificationCenter.ObservationToken where Message : NotificationCenter.MainActorMessage, Message.Subject : AnyObject
```

#### Return Value

A token representing the observation registration with the given notification center.

## Parameters

- `subject`: The subject to be observed. Specify a metatype to observe all values for a given type.
- `messageType`: The message type to be observed.
- `observer`: A closure to execute when receving a message.

## See Also

### Observing concurrency-safe notifications
- [func addObserver<Identifier, Message>(of: Message.Subject, for: Identifier, using: (Message) -> Void) -> NotificationCenter.ObservationToken](./addobserver%28of,for,using%29-4d19x.md)
  Adds an observer to a center for messages delivered on the main actor with a given subject and identifier.
- [func addObserver<Identifier, Message>(of: Message.Subject.Type, for: Identifier, using: (Message) -> Void) -> NotificationCenter.ObservationToken](./addobserver%28of,for,using%29-90os.md)
  Adds an observer to a center for messages delivered on the main actor with a given subject and identifier.
- [func addObserver<Identifier, Message>(of: Message.Subject, for: Identifier, using: (Message) async -> Void) -> NotificationCenter.ObservationToken](./addobserver%28of,for,using%29-twm3.md)
  Adds an observer to a center for messages delivered asynchronously with a given subject and identifier.
- [func addObserver<Identifier, Message>(of: Message.Subject.Type, for: Identifier, using: (Message) async -> Void) -> NotificationCenter.ObservationToken](./addobserver%28of,for,using%29-t1wr.md)
  Adds an observer to a center for messages delivered asynchronously with a given subject and message type.
- [func addObserver<Message>(of: Message.Subject?, for: Message.Type, using: (Message) async -> Void) -> NotificationCenter.ObservationToken](./addobserver%28of,for,using%29-64uw3.md)
  Adds an observer to a center for messages delivered asynchronously with a given subject and message type.
- [func removeObserver(NotificationCenter.ObservationToken)](./removeobserver%28_%29-2gmm0.md)
  Stops the observation represented by the given observation token.
- [NotificationCenter.ObservationToken](./observationtoken.md)
  A unique token representing a single observer registration in a notification center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/addobserver(of:for:using:)-56bn4)*