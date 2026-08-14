# PlayerIdentifier

**Framework**: TabletopKit  
**Kind**: struct

A unique identifier for players.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct PlayerIdentifier
```

#### Overview

A player identifier is unique across all instances of the same tabletop game.

## Topics

### Creating player identifiers
- [init(uuid: UUID)](playeridentifier/init(uuid:).md)
  Creates a player identifier.
### Getting identifier values
- [var uuid: UUID](playeridentifier/uuid.md)
  A universally unique value to identify a player.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Copyable](../swift/copyable.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct Player](player.md)
  A player in a tabletop game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/playeridentifier)*