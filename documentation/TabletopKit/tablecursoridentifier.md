# TableCursorIdentifier

**Framework**: TabletopKit  
**Kind**: struct

A unique identifier for cursors.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct TableCursorIdentifier
```

#### Overview

A cursor identifier is unique across all instances of the same tabletop game.

## Topics

### Creating cursor identifiers
- [init(Int)](tablecursoridentifier/init(_:).md)
### Getting identifier values
- [let rawValue: Int](tablecursoridentifier/rawvalue.md)

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Simulating dice rolls as a component for your game](simulating-dice-rolls-as-a-component-for-your-game.md)
  Create a physically realistic dice game by adding interactive rolling and scoring.
- [class TabletopInteraction](tabletopinteraction.md)
  A protocol for objects that manage the entire flow of players interacting with equipment.
- [struct TossableRepresentation](tossablerepresentation.md)
  An object that represents geometric shapes that the player can throw during gameplay, such as dice.
- [struct TableSnapshot](tablesnapshot.md)
  A snapshot of the current state of the table.
- [struct TableVisualState](tablevisualstate.md)
  A structure that represents the appearance of an object on the table.
- [struct TableCursor](tablecursor.md)
  A cursor conveys information about one equipment that is currently being controlled by an interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tablecursoridentifier)*