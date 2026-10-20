# removeObserver(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Stops the observation represented by the given observation token.

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
func removeObserver(_ token: NotificationCenter.ObservationToken)
```

## Parameters

- `token`: A unique token representing a specific observer in a specific notification center. You receive this type from prior calls to `addObserver(of:for:using:)`.

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
- [func addObserver<Identifier, Message>(of: Message.Subject.Type, for: Identifier, using: (Message) async -> Void) -> NotificationCenter.ObservationToken](./addobserver%28of,for,using%29-t1wr.md)
  Adds an observer to a center for messages delivered asynchronously with a given subject and message type.
- [func addObserver<Message>(of: Message.Subject?, for: Message.Type, using: (Message) async -> Void) -> NotificationCenter.ObservationToken](./addobserver%28of,for,using%29-64uw3.md)
  Adds an observer to a center for messages delivered asynchronously with a given subject and message type.
- [NotificationCenter.ObservationToken](./observationtoken.md)
  A unique token representing a single observer registration in a notification center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/removeobserver(_:)-2gmm0)*