# playerChangedSeats(_:oldSeat:newSeat:snapshot:)

**Framework**: TabletopKit  
**Kind**: method  
**Required**: Yes

Called every time the Seat for any player has changed

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func playerChangedSeats(_ player: Player, oldSeat: (any TableSeat)?, newSeat: (any TableSeat)?, snapshot: TableSnapshot)
```

## See Also

- [func stateDidResetToBookmark(StateBookmarkIdentifier)](tabletopgame/observer/statedidresettobookmark(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopgame/observer/playerchangedseats(_:oldseat:newseat:snapshot:))*