# GCExtendedGamepadSnapshotData

**Framework**: Game Controller  
**Kind**: struct

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
struct GCExtendedGamepadSnapshotData
```

## Topics

### Initializers
- [init()](gcextendedgamepadsnapshotdata/init.md)
- [init(version: UInt16, size: UInt16, dpadX: Float, dpadY: Float, buttonA: Float, buttonB: Float, buttonX: Float, buttonY: Float, leftShoulder: Float, rightShoulder: Float, leftThumbstickX: Float, leftThumbstickY: Float, rightThumbstickX: Float, rightThumbstickY: Float, leftTrigger: Float, rightTrigger: Float, supportsClickableThumbsticks: ObjCBool, leftThumbstickButton: ObjCBool, rightThumbstickButton: ObjCBool)](gcextendedgamepadsnapshotdata/init(version:size:dpadx:dpady:buttona:buttonb:buttonx:buttony:leftshoulder:rightshoulder:leftthumbstickx:leftthumbsticky:rightthumbstickx:rightthumbsticky:lefttrigger:righttrigger:supportsclickablethumbsticks:leftthumbstickbutton:rightthumb-26via.md)
### Instance Properties
- [var buttonA: Float](gcextendedgamepadsnapshotdata/buttona.md)
- [var buttonB: Float](gcextendedgamepadsnapshotdata/buttonb.md)
- [var buttonX: Float](gcextendedgamepadsnapshotdata/buttonx.md)
- [var buttonY: Float](gcextendedgamepadsnapshotdata/buttony.md)
- [var dpadX: Float](gcextendedgamepadsnapshotdata/dpadx.md)
- [var dpadY: Float](gcextendedgamepadsnapshotdata/dpady.md)
- [var leftShoulder: Float](gcextendedgamepadsnapshotdata/leftshoulder.md)
- [var leftThumbstickButton: ObjCBool](gcextendedgamepadsnapshotdata/leftthumbstickbutton.md)
- [var leftThumbstickX: Float](gcextendedgamepadsnapshotdata/leftthumbstickx.md)
- [var leftThumbstickY: Float](gcextendedgamepadsnapshotdata/leftthumbsticky.md)
- [var leftTrigger: Float](gcextendedgamepadsnapshotdata/lefttrigger.md)
- [var rightShoulder: Float](gcextendedgamepadsnapshotdata/rightshoulder.md)
- [var rightThumbstickButton: ObjCBool](gcextendedgamepadsnapshotdata/rightthumbstickbutton.md)
- [var rightThumbstickX: Float](gcextendedgamepadsnapshotdata/rightthumbstickx.md)
- [var rightThumbstickY: Float](gcextendedgamepadsnapshotdata/rightthumbsticky.md)
- [var rightTrigger: Float](gcextendedgamepadsnapshotdata/righttrigger.md)
- [var size: UInt16](gcextendedgamepadsnapshotdata/size.md)
- [var supportsClickableThumbsticks: ObjCBool](gcextendedgamepadsnapshotdata/supportsclickablethumbsticks.md)
- [var version: UInt16](gcextendedgamepadsnapshotdata/version.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class GCGamepad](gcgamepad.md)
  The standard set of gamepad controls.
- [class GCExtendedGamepadSnapshot](gcextendedgamepadsnapshot.md)
  A recording of all of the values provided by a [`GCExtendedGamepad`](gcextendedgamepad.md) object.
- [class GCGamepadSnapshot](gcgamepadsnapshot.md)
  A recording of all of the values provided by a [`GCGamepad`](gcgamepad.md) object.
- [class GCMicroGamepadSnapshot](gcmicrogamepadsnapshot.md)
  A recording of all of the values provided by a [`GCMicroGamepad`](gcmicrogamepad.md) object.
- [struct GCMicroGamepadSnapshotData](gcmicrogamepadsnapshotdata.md)
- [enum GCExtendedGamepadSnapshotDataVersion](gcextendedgamepadsnapshotdataversion.md)
- [enum GCMicroGamepadSnapshotDataVersion](gcmicrogamepadsnapshotdataversion.md)
- [let GCCurrentExtendedGamepadSnapshotDataVersion: GCExtendedGamepadSnapshotDataVersion](gccurrentextendedgamepadsnapshotdataversion.md)
- [let GCCurrentMicroGamepadSnapshotDataVersion: GCMicroGamepadSnapshotDataVersion](gccurrentmicrogamepadsnapshotdataversion.md)
- [func GCExtendedGamepadSnapshotDataFromNSData(UnsafeMutablePointer<GCExtendedGamepadSnapshotData>?, Data?) -> Bool](gcextendedgamepadsnapshotdatafromnsdata(_:_:).md)
- [func GCMicroGamepadSnapshotDataFromNSData(UnsafeMutablePointer<GCMicroGamepadSnapshotData>?, Data?) -> Bool](gcmicrogamepadsnapshotdatafromnsdata(_:_:).md)
- [func NSDataFromGCExtendedGamepadSnapshotData(UnsafeMutablePointer<GCExtendedGamepadSnapshotData>?) -> Data?](nsdatafromgcextendedgamepadsnapshotdata(_:).md)
- [func NSDataFromGCMicroGamepadSnapshotData(UnsafeMutablePointer<GCMicroGamepadSnapshotData>?) -> Data?](nsdatafromgcmicrogamepadsnapshotdata(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepadsnapshotdata)*