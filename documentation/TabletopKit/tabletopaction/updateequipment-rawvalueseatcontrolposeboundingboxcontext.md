# updateEquipment(_:rawValue:seatControl:pose:boundingBox:context:)

**Framework**: TabletopKit  
**Kind**: method

**Availability**:
- visionOS 2.0+

## Declaration

```swift
static func updateEquipment<E>(_ equipment: E, rawValue: UInt64? = nil, seatControl: ControllingSeats? = nil, pose: TableVisualState.Pose2D? = nil, boundingBox: Rect3D? = nil, context: UInt64 = 0) -> Self where E : Equipment, E.State == RawValueState
```

## See Also

- [static func updateEquipment<E>(E, faceUp: Bool?, seatControl: ControllingSeats?, pose: TableVisualState.Pose2D?, boundingBox: Rect3D?, context: UInt64) -> Self](tabletopaction/updateequipment(_:faceup:seatcontrol:pose:boundingbox:context:).md)
- [static func updateEquipment<E>(E, seatControl: ControllingSeats?, pose: TableVisualState.Pose2D?, boundingBox: Rect3D?, context: UInt64) -> Self](tabletopaction/updateequipment(_:seatcontrol:pose:boundingbox:context:).md)
- [static func updateEquipment<E>(E, state: E.State, context: UInt64) -> Self](tabletopaction/updateequipment(_:state:context:)-6kawf.md)
- [static func updateEquipment<E>(E, state: E.State, context: UInt64) -> Self](tabletopaction/updateequipment(_:state:context:)-88v3m.md)
- [static func updateEquipment<E>(E, state: E.State, context: UInt64) -> Self](tabletopaction/updateequipment(_:state:context:)-8tmnn.md)
- [static func updateEquipment<E>(E, state: E.State, context: UInt64) -> Self](tabletopaction/updateequipment(_:state:context:)-j62v.md)
- [static func updateEquipment<E>(E, value: Int?, seatControl: ControllingSeats?, pose: TableVisualState.Pose2D?, boundingBox: Rect3D?, context: UInt64) -> Self](tabletopaction/updateequipment(_:value:seatcontrol:pose:boundingbox:context:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopaction/updateequipment(_:rawvalue:seatcontrol:pose:boundingbox:context:))*