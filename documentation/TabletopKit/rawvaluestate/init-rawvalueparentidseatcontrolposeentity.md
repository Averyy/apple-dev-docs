# init(rawValue:parentID:seatControl:pose:entity:)

**Framework**: TabletopKit  
**Kind**: init

**Availability**:
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency init(rawValue: UInt64, parentID: EquipmentIdentifier, seatControl: ControllingSeats = .any, pose: TableVisualState.Pose2D = .identity, entity: Entity)
```

## See Also

- [init(rawValue: UInt64, parentID: EquipmentIdentifier, seatControl: ControllingSeats, pose: TableVisualState.Pose2D, boundingBox: Rect3D)](rawvaluestate/init(rawvalue:parentid:seatcontrol:pose:boundingbox:).md)
  Creates a state for equipment using the specified raw value, location, and player interactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/rawvaluestate/init(rawvalue:parentid:seatcontrol:pose:entity:))*