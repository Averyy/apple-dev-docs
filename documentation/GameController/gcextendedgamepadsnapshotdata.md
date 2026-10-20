# GCExtendedGamepadSnapshotData

**Framework**: Game Controller  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 13.0+ - Deprecated in 13.0
- iPadOS 13.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.15+ - Deprecated in 10.15
- tvOS 13.0+ - Deprecated in 13.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use the -[GCController controllerWithExtendedGamepad] method instead

## Declaration

```swift
struct GCExtendedGamepadSnapshotData
```

```c
typedef struct { ... } GCExtendedGamepadSnapshotData;
```

## Topics

### Initializers
- [init()](./gcextendedgamepadsnapshotdata/init%28%29.md)
- [init(version: UInt16, size: UInt16, dpadX: Float, dpadY: Float, buttonA: Float, buttonB: Float, buttonX: Float, buttonY: Float, leftShoulder: Float, rightShoulder: Float, leftThumbstickX: Float, leftThumbstickY: Float, rightThumbstickX: Float, rightThumbstickY: Float, leftTrigger: Float, rightTrigger: Float, supportsClickableThumbsticks: ObjCBool, leftThumbstickButton: ObjCBool, rightThumbstickButton: ObjCBool)](./gcextendedgamepadsnapshotdata/init%28version_size_dpadx_dpady_buttona_buttonb_buttonx_buttony_leftshoulder_rightshoulder_leftthumbstickx_leftthumbsticky_rightthumbstickx_rightthumbsticky_lefttrigger_righttrigger_supportsclickablethumbsticks_leftthumb-fbc7a5cd.md)
### Instance Properties
- [var buttonA: Float](./gcextendedgamepadsnapshotdata/buttona.md)
- [var buttonB: Float](./gcextendedgamepadsnapshotdata/buttonb.md)
- [var buttonX: Float](./gcextendedgamepadsnapshotdata/buttonx.md)
- [var buttonY: Float](./gcextendedgamepadsnapshotdata/buttony.md)
- [var dpadX: Float](./gcextendedgamepadsnapshotdata/dpadx.md)
- [var dpadY: Float](./gcextendedgamepadsnapshotdata/dpady.md)
- [var leftShoulder: Float](./gcextendedgamepadsnapshotdata/leftshoulder.md)
- [var leftThumbstickButton: ObjCBool](./gcextendedgamepadsnapshotdata/leftthumbstickbutton.md)
- [var leftThumbstickX: Float](./gcextendedgamepadsnapshotdata/leftthumbstickx.md)
- [var leftThumbstickY: Float](./gcextendedgamepadsnapshotdata/leftthumbsticky.md)
- [var leftTrigger: Float](./gcextendedgamepadsnapshotdata/lefttrigger.md)
- [var rightShoulder: Float](./gcextendedgamepadsnapshotdata/rightshoulder.md)
- [var rightThumbstickButton: ObjCBool](./gcextendedgamepadsnapshotdata/rightthumbstickbutton.md)
- [var rightThumbstickX: Float](./gcextendedgamepadsnapshotdata/rightthumbstickx.md)
- [var rightThumbstickY: Float](./gcextendedgamepadsnapshotdata/rightthumbsticky.md)
- [var rightTrigger: Float](./gcextendedgamepadsnapshotdata/righttrigger.md)
- [var size: UInt16](./gcextendedgamepadsnapshotdata/size.md)
- [var supportsClickableThumbsticks: ObjCBool](./gcextendedgamepadsnapshotdata/supportsclickablethumbsticks.md)
- [var version: UInt16](./gcextendedgamepadsnapshotdata/version.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Deprecated symbols
- [class GCGamepad](./gcgamepad.md)
  The standard set of gamepad controls.
- [class GCExtendedGamepadSnapshot](./gcextendedgamepadsnapshot.md)
  A recording of all of the values provided by a [`GCExtendedGamepad`](./gcextendedgamepad.md) object.
- [class GCGamepadSnapshot](./gcgamepadsnapshot.md)
  A recording of all of the values provided by a [`GCGamepad`](./gcgamepad.md) object.
- [class GCMicroGamepadSnapshot](./gcmicrogamepadsnapshot.md)
  A recording of all of the values provided by a [`GCMicroGamepad`](./gcmicrogamepad.md) object.
- [struct GCMicroGamepadSnapshotData](./gcmicrogamepadsnapshotdata.md)
- [enum GCExtendedGamepadSnapshotDataVersion](./gcextendedgamepadsnapshotdataversion.md)
- [enum GCMicroGamepadSnapshotDataVersion](./gcmicrogamepadsnapshotdataversion.md)
- [let GCCurrentExtendedGamepadSnapshotDataVersion: GCExtendedGamepadSnapshotDataVersion](./gccurrentextendedgamepadsnapshotdataversion.md)
- [let GCCurrentMicroGamepadSnapshotDataVersion: GCMicroGamepadSnapshotDataVersion](./gccurrentmicrogamepadsnapshotdataversion.md)
- [func GCExtendedGamepadSnapshotDataFromNSData(UnsafeMutablePointer<GCExtendedGamepadSnapshotData>?, Data?) -> Bool](./gcextendedgamepadsnapshotdatafromnsdata%28_,_%29.md)
- [func GCMicroGamepadSnapshotDataFromNSData(UnsafeMutablePointer<GCMicroGamepadSnapshotData>?, Data?) -> Bool](./gcmicrogamepadsnapshotdatafromnsdata%28_,_%29.md)
- [func NSDataFromGCExtendedGamepadSnapshotData(UnsafeMutablePointer<GCExtendedGamepadSnapshotData>?) -> Data?](./nsdatafromgcextendedgamepadsnapshotdata%28_%29.md)
- [func NSDataFromGCMicroGamepadSnapshotData(UnsafeMutablePointer<GCMicroGamepadSnapshotData>?) -> Data?](./nsdatafromgcmicrogamepadsnapshotdata%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepadsnapshotdata)*