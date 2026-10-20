# ControllingSeats.restrictedCurrent(_:)

**Framework**: TabletopKit  
**Kind**: case  
**Role**: Case

Lets players in specific seats interact with the equipment if they are currently in turn.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
case restrictedCurrent([TableSeatIdentifier])
```

## See Also

### Seats
- [ControllingSeats.any](./any.md)
  Lets players in all seats interact with the equipment.
- [case restricted([TableSeatIdentifier])](./restricted%28_%29.md)
  Lets players in specific seats interact with the equipment.
- [ControllingSeats.inherited](./inherited.md)
  The value is inherited from the parent. The table implicit value is considered to be `.any`.
- [ControllingSeats.current](./current.md)
  Lets only seats currently in turn interact with the equipment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/controllingseats/restrictedcurrent(_:))*