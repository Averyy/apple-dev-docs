# claimSeat(_:)

**Framework**: TabletopKit  
**Kind**: method

Claims the given seat. If provided Seat is not part of the table, it has no effect

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func claimSeat(_ seat: some TableSeat)
```

## See Also

- [func claimAnySeat()](tabletopgame/claimanyseat.md)
  Claims any free seat. If there are no free seats, it has no effect
- [func claimSeat(matching: TableSeatIdentifier)](tabletopgame/claimseat(matching:).md)
  Claims the given seat. If provided ID does not exist, it has no effect
- [func releaseSeat()](tabletopgame/releaseseat.md)
  Releases the seat for this player. If the player is not seated it has no effect


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopgame/claimseat(_:))*