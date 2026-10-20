# updateEquipment(_:state:context:)

**Framework**: TabletopKit  
**Kind**: method  
**Role**: Type Method

**Availability**:
- visionOS 2.0+

## Declaration

```swift
static func updateEquipment<E>(_ equipment: E, state: E.State, context: UInt64 = 0) -> Self where E : Equipment, E.State == RawValueState
```

Available when `Self` is `UpdateEquipmentAction<RawValueState>`.

## See Also

### Changing equipment state properties
- [static func updateEquipment<E>(E, faceUp: Bool?, seatControl: ControllingSeats?, pose: TableVisualState.Pose2D?, boundingBox: Rect3D?, context: UInt64) -> Self](./updateequipment%28_,faceup,seatcontrol,pose,boundingbox,context%29.md)
- [static func updateEquipment<E>(E, rawValue: UInt64?, seatControl: ControllingSeats?, pose: TableVisualState.Pose2D?, boundingBox: Rect3D?, context: UInt64) -> Self](./updateequipment%28_,rawvalue,seatcontrol,pose,boundingbox,context%29.md)
- [static func updateEquipment<E>(E, seatControl: ControllingSeats?, pose: TableVisualState.Pose2D?, boundingBox: Rect3D?, context: UInt64) -> Self](./updateequipment%28_,seatcontrol,pose,boundingbox,context%29.md)
- [static func updateEquipment<E>(E, state: E.State, context: UInt64) -> Self](./updateequipment%28_,state,context%29-6kawf.md)
- [static func updateEquipment<E>(E, state: E.State, context: UInt64) -> Self](./updateequipment%28_,state,context%29-88v3m.md)
- [static func updateEquipment<E>(E, state: E.State, context: UInt64) -> Self](./updateequipment%28_,state,context%29-j62v.md)
- [static func updateEquipment<E>(E, value: Int?, seatControl: ControllingSeats?, pose: TableVisualState.Pose2D?, boundingBox: Rect3D?, context: UInt64) -> Self](./updateequipment%28_,value,seatcontrol,pose,boundingbox,context%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopaction/updateequipment(_:state:context:)-8tmnn)*