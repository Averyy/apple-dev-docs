# ControllingSeats.current

**Framework**: TabletopKit  
**Kind**: case  
**Role**: Case

Lets only seats currently in turn interact with the equipment.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
case current
```

## See Also

### Seats
- [ControllingSeats.any](./any.md)
  Lets players in all seats interact with the equipment.
- [case restricted([TableSeatIdentifier])](./restricted%28_%29.md)
  Lets players in specific seats interact with the equipment.
- [case restrictedCurrent([TableSeatIdentifier])](./restrictedcurrent%28_%29.md)
  Lets players in specific seats interact with the equipment if they are currently in turn.
- [ControllingSeats.inherited](./inherited.md)
  The value is inherited from the parent. The table implicit value is considered to be `.any`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/controllingseats/current)*