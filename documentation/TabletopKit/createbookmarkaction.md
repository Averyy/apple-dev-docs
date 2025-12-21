# CreateBookmarkAction

**Framework**: TabletopKit  
**Kind**: struct

An action that takes a snapshot of the game.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
struct CreateBookmarkAction
```

#### Overview

To create a bookmark action, use the [`createBookmark(_:context:)`](tabletopaction/createbookmark(_:context:).md) or the [`createBookmark(id:context:)`](tabletopaction/createbookmark(id:context:).md) static method.

## Topics

### Getting the bookmark
- [var bookmark: StateBookmark](createbookmarkaction/bookmark.md)
### Getting game-specific information
- [var context: UInt64](createbookmarkaction/context.md)
  An integer value that your game uses.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TabletopAction](tabletopaction.md)

## See Also

- [protocol TabletopAction](tabletopaction.md)
  A protocol for objects that describe an action in a tabletop game.
- [struct MoveEquipmentAction](moveequipmentaction.md)
  An action that moves a piece of equipment on the table or changes the grouping.
- [struct UpdateEquipmentAction](updateequipmentaction.md)
  An action that updates properties of equipment on the table.
- [struct SetTurnAction](setturnaction.md)
  An action that sets the current seats participating in the current turn.
- [struct UpdateCounterAction](updatecounteraction.md)
  An action that updates the game counter.
- [protocol CustomAction](customaction.md)
  A protocol that represents an action whose behavior is implemented outside of TabletopKit. A custom action that can be applied to a `TableState`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/createbookmarkaction)*