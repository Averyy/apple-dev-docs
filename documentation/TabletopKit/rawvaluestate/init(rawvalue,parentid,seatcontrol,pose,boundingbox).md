# init(rawValue:parentID:seatControl:pose:boundingBox:)

**Framework**: TabletopKit  
**Kind**: init  
**Role**: Initializer

Creates a state for equipment using the specified raw value, location, and player interactions.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
init(rawValue: UInt64, parentID: EquipmentIdentifier, seatControl: ControllingSeats = .any, pose: TableVisualState.Pose2D = .identity, boundingBox: Rect3D)
```

## See Also

### Creating a die state
- [init(rawValue: UInt64, parentID: EquipmentIdentifier, seatControl: ControllingSeats, pose: TableVisualState.Pose2D, entity: Entity)](./init%28rawvalue,parentid,seatcontrol,pose,entity%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/rawvaluestate/init(rawvalue:parentid:seatcontrol:pose:boundingbox:))*