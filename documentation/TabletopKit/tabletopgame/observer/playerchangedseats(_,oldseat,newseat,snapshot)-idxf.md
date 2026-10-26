# playerChangedSeats(_:oldSeat:newSeat:snapshot:)

**Framework**: TabletopKit  
**Kind**: method  
**Role**: Instance Method

Called whenever the Seat for any player has changed in the shared network table state. `playerChandedSeats` callbacks are also reliably ordered with `actionWasConfirmed` and `actionWasRolledBack` callbacks, and are also network delayed behind any changes to the speculative visible table state.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func playerChangedSeats(_ player: Player, oldSeat: (any TableSeat)?, newSeat: (any TableSeat)?, snapshot: TableSnapshot)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopgame/observer/playerchangedseats(_:oldseat:newseat:snapshot:)-idxf)*