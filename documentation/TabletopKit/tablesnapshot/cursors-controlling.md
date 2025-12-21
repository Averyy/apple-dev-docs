# cursors(controlling:)

**Framework**: TabletopKit  
**Kind**: method

Finds and returns all the cursors corresponding to an interactions controlling any of the given equipment IDs. Duplicate equipment IDs are ignored.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
func cursors(controlling equipmentIDs: some Sequence<EquipmentIdentifier>) -> [TableCursor]
```

## See Also

- [var cursors: [TableCursor]](tablesnapshot/cursors.md)
- [func cursor(matching: TableCursorIdentifier) -> TableCursor?](tablesnapshot/cursor(matching:).md)
- [func cursor(controlling: EquipmentIdentifier) -> TableCursor?](tablesnapshot/cursor(controlling:).md)
  Returns the cursor corresponding to an interaction controlling the given equipment ID, or `nil` if no such cursors could be found.
- [func cursors(forPlayer: Player) -> [TableCursor]](tablesnapshot/cursors(forplayer:).md)
- [func cursors(hovering: EquipmentIdentifier) -> [TableCursor]](tablesnapshot/cursors(hovering:).md)
- [func cursors(for: Player) -> [TableCursor]](tablesnapshot/cursors(for:).md)
  Finds and returns all the cursors corresponding to an interactions owned by the given player.
- [func cursors(matching: TabletopInteraction.Identifier) -> [TableCursor]](tablesnapshot/cursors(matching:).md)
  Finds and returns all the cursors corresponding to a given interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tablesnapshot/cursors(controlling:))*