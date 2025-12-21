# removeObserver(_:)

**Framework**: Foundation  
**Kind**: method

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

- `token`: A unique token representing a specific observer in a specific notification center. You receive this type from prior calls to  .

## See Also

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
- [NotificationCenter.ObservationToken](notificationcenter/observationtoken.md)
  A unique token representing a single observer registration in a notification center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/removeobserver(_:)-2gmm0)*