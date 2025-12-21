# ControllingSeats.restrictedCurrent(_:)

**Framework**: TabletopKit  
**Kind**: case

Lets players in specific seats interact with the equipment if they are currently in turn.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
case restrictedCurrent([TableSeatIdentifier])
```

## See Also

- [ControllingSeats.any](controllingseats/any.md)
  Lets players in all seats interact with the equipment.
- [case restricted([TableSeatIdentifier])](controllingseats/restricted(_:).md)
  Lets players in specific seats interact with the equipment.
- [ControllingSeats.inherited](controllingseats/inherited.md)
  The value is inherited from the parent. The table implicit value is considered to be `.any`.
- [ControllingSeats.current](controllingseats/current.md)
  Lets only seats currently in turn interact with the equipment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/controllingseats/restrictedcurrent(_:))*