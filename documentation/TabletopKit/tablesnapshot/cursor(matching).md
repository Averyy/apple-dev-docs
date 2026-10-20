# cursor(matching:)

**Framework**: TabletopKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func cursor(matching id: TableCursorIdentifier) -> TableCursor?
```

## See Also

### Getting cursors
- [var cursors: [TableCursor]](./cursors.md)
- [func cursor(controlling: EquipmentIdentifier) -> TableCursor?](./cursor%28controlling%29.md)
  Returns the cursor corresponding to an interaction controlling the given equipment ID, or `nil` if no such cursors could be found.
- [func cursors(forPlayer: Player) -> [TableCursor]](./cursors%28forplayer%29.md)
- [func cursors(hovering: EquipmentIdentifier) -> [TableCursor]](./cursors%28hovering%29.md)
- [func cursors(controlling: some Sequence<EquipmentIdentifier>) -> [TableCursor]](./cursors%28controlling%29.md)
  Finds and returns all the cursors corresponding to an interactions controlling any of the given equipment IDs. Duplicate equipment IDs are ignored.
- [func cursors(for: Player) -> [TableCursor]](./cursors%28for%29.md)
  Finds and returns all the cursors corresponding to an interactions owned by the given player.
- [func cursors(matching: TabletopInteraction.Identifier) -> [TableCursor]](./cursors%28matching%29.md)
  Finds and returns all the cursors corresponding to a given interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tablesnapshot/cursor(matching:))*