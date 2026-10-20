# claimSeat(matching:)

**Framework**: TabletopKit  
**Kind**: method  
**Role**: Instance Method

Claims the given seat. If provided ID does not exist, it has no effect

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func claimSeat(matching seatID: TableSeatIdentifier)
```

## See Also

### Managing seats
- [func claimAnySeat()](./claimanyseat%28%29.md)
  Claims any free seat. Has no effect if the player is already seated or if there are no free seats.
- [func claimSeat(some TableSeat)](./claimseat%28_%29.md)
  Claims the given seat. If provided Seat is not part of the table, it has no effect
- [func releaseSeat()](./releaseseat%28%29.md)
  Releases the seat for this player. If the player is not seated it has no effect


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopgame/claimseat(matching:))*