# NotificationCenter.ObservationToken

**Framework**: Foundation  
**Kind**: struct

A unique token representing a single observer registration in a notification center.

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
struct ObservationToken
```

#### Overview

You receive the `ObservationToken` type as a return value from `addObserver(of:for:using:)` and related methods.

Retain the `ObservationToken` for as long as you need to continue observation, since observation ends when the token goes out of scope. You can also explicitly stop observing by passing the token to `removeObserver(_:)-(ObservationToken)`.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [func removeObserver(NotificationCenter.ObservationToken)](notificationcenter/removeobserver(_:)-2gmm0.md)
  Stops the observation represented by the given observation token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/observationtoken)*