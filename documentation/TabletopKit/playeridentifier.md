# PlayerIdentifier

**Framework**: TabletopKit  
**Kind**: struct  
**Role**: Structure

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
- [init(uuid: UUID)](./playeridentifier/init%28uuid%29.md)
  Creates a player identifier.
### Getting identifier values
- [var uuid: UUID](./playeridentifier/uuid.md)
  A universally unique value to identify a player.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Copyable](../Swift/copyable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Players
- [struct Player](./player.md)
  A player in a tabletop game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/playeridentifier)*