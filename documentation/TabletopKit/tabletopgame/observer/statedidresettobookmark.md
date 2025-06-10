# stateDidResetToBookmark(_:)

**Framework**: TabletopKit  
**Kind**: method  
**Required**: Yes

Called whenever a `jumpToBookmark` is applied to the shared network table state. `stateDidResetToBookmark` callbacks are also reliably ordered with `actionWasConfirmed` and `actionWasRolledBack` callbacks, and are also network delayed behind any changes to the speculative visible table state.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func stateDidResetToBookmark(_ bookmarkID: StateBookmarkIdentifier)
```

## See Also

- [func playerChangedSeats(Player, oldSeat: (any TableSeat)?, newSeat: (any TableSeat)?, snapshot: TableSnapshot)](tabletopgame/observer/playerchangedseats(_:oldseat:newseat:snapshot:).md)
  Called whenever the Seat for any player has changed in the shared network table state. `playerChandedSeats` callbacks are also reliably ordered with `actionWasConfirmed` and `actionWasRolledBack` callbacks, and are also network delayed behind any changes to the speculative visible table state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopgame/observer/statedidresettobookmark(_:))*