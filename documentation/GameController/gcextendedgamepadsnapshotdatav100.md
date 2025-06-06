# GCExtendedGamepadSnapShotDataV100

**Framework**: Game Controller  
**Kind**: struct

A structure that holds a snapshot of an extended gamepad controller’s input data.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
struct GCExtendedGamepadSnapShotDataV100
```

## Topics

### Instance Properties
- [var buttonA: Float](gcextendedgamepadsnapshotdatav100/buttona.md)
  The value of the A button.
- [var buttonB: Float](gcextendedgamepadsnapshotdatav100/buttonb.md)
  The value of the B button.
- [var buttonX: Float](gcextendedgamepadsnapshotdatav100/buttonx.md)
  The value of the X button.
- [var buttonY: Float](gcextendedgamepadsnapshotdatav100/buttony.md)
  The value of the Y button.
- [var dpadX: Float](gcextendedgamepadsnapshotdatav100/dpadx.md)
  The value of the horizontal axis of the dpad.
- [var dpadY: Float](gcextendedgamepadsnapshotdatav100/dpady.md)
  The value of the vertical axis of the dpad.
- [var leftShoulder: Float](gcextendedgamepadsnapshotdatav100/leftshoulder.md)
  The value of the left shoulder button.
- [var leftThumbstickX: Float](gcextendedgamepadsnapshotdatav100/leftthumbstickx.md)
  The value of the horizontal axis of the left thumbstick.
- [var leftThumbstickY: Float](gcextendedgamepadsnapshotdatav100/leftthumbsticky.md)
  The value of the vertical axis of the left thumbstick.
- [var leftTrigger: Float](gcextendedgamepadsnapshotdatav100/lefttrigger.md)
  The value of the left trigger.
- [var rightShoulder: Float](gcextendedgamepadsnapshotdatav100/rightshoulder.md)
  The value of the right shoulder button.
- [var rightThumbstickX: Float](gcextendedgamepadsnapshotdatav100/rightthumbstickx.md)
  The value of the horizontal axis of the right thumbstick.
- [var rightThumbstickY: Float](gcextendedgamepadsnapshotdatav100/rightthumbsticky.md)
  The value of the vertical axis of the right thumbstick.
- [var rightTrigger: Float](gcextendedgamepadsnapshotdatav100/righttrigger.md)
  The value of the right trigger.
- [var size: UInt16](gcextendedgamepadsnapshotdatav100/size.md)
  The size of the recorded structure, in bytes.
- [var version: UInt16](gcextendedgamepadsnapshotdatav100/version.md)
  A value that indicates the version number of the data structure.
### Initializers
- [init()](gcextendedgamepadsnapshotdatav100/init.md)
- [init(version: UInt16, size: UInt16, dpadX: Float, dpadY: Float, buttonA: Float, buttonB: Float, buttonX: Float, buttonY: Float, leftShoulder: Float, rightShoulder: Float, leftThumbstickX: Float, leftThumbstickY: Float, rightThumbstickX: Float, rightThumbstickY: Float, leftTrigger: Float, rightTrigger: Float)](gcextendedgamepadsnapshotdatav100/init(version:size:dpadx:dpady:buttona:buttonb:buttonx:buttony:leftshoulder:rightshoulder:leftthumbstickx:leftthumbsticky:rightthumbstickx:rightthumbsticky:lefttrigger:righttrigger:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func NSDataFromGCExtendedGamepadSnapShotDataV100(UnsafeMutablePointer<GCExtendedGamepadSnapShotDataV100>?) -> Data?](nsdatafromgcextendedgamepadsnapshotdatav100(_:).md)
  Encapsulates the controller data from an extended gamepad structure into a data object.
- [func GCExtendedGamepadSnapShotDataV100FromNSData(UnsafeMutablePointer<GCExtendedGamepadSnapShotDataV100>?, Data?) -> Bool](gcextendedgamepadsnapshotdatav100fromnsdata(_:_:).md)
  Copies the recorded data from an extended gamepad snapshot into a readable structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepadsnapshotdatav100)*