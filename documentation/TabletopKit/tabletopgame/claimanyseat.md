# claimAnySeat()

**Framework**: TabletopKit  
**Kind**: method

Claims any free seat. Has no effect if the player is already seated or if there are no free seats.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func claimAnySeat()
```

## See Also

- [func claimSeat(some TableSeat)](tabletopgame/claimseat(_:).md)
  Claims the given seat. If provided Seat is not part of the table, it has no effect
- [func claimSeat(matching: TableSeatIdentifier)](tabletopgame/claimseat(matching:).md)
  Claims the given seat. If provided ID does not exist, it has no effect
- [func releaseSeat()](tabletopgame/releaseseat.md)
  Releases the seat for this player. If the player is not seated it has no effect


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopgame/claimanyseat())*