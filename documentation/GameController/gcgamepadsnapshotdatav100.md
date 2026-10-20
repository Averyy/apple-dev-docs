# GCGamepadSnapShotDataV100

**Framework**: Game Controller  
**Kind**: struct  
**Role**: Structure

A structure that holds a snapshot of a gamepad controller’s input data.

**Availability**:
- iOS 7.0+ - Deprecated in 13.0
- iPadOS 7.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.9+ - Deprecated in 10.15
- tvOS 9.0+ - Deprecated in 13.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use GCExtendedGamepad instead

## Declaration

```swift
struct GCGamepadSnapShotDataV100
```

```c
typedef struct { ... } GCGamepadSnapShotDataV100;
```

## Topics

### Instance Properties
- [var buttonA: Float](./gcgamepadsnapshotdatav100/buttona.md)
  The value of the A button.
- [var buttonB: Float](./gcgamepadsnapshotdatav100/buttonb.md)
  The value of the B button.
- [var buttonX: Float](./gcgamepadsnapshotdatav100/buttonx.md)
  The value of the X button.
- [var buttonY: Float](./gcgamepadsnapshotdatav100/buttony.md)
  The value of the Y button.
- [var dpadX: Float](./gcgamepadsnapshotdatav100/dpadx.md)
  The value of the horizontal axis of the dpad.
- [var dpadY: Float](./gcgamepadsnapshotdatav100/dpady.md)
  The value of the vertical axis of the dpad.
- [var leftShoulder: Float](./gcgamepadsnapshotdatav100/leftshoulder.md)
  The value of the left shoulder button.
- [var rightShoulder: Float](./gcgamepadsnapshotdatav100/rightshoulder.md)
  The value of the right shoulder button.
- [var size: UInt16](./gcgamepadsnapshotdatav100/size.md)
  The size of the recorded structure, in bytes.
- [var version: UInt16](./gcgamepadsnapshotdatav100/version.md)
  A value that indicates the version number of the data structure.
### Initializers
- [init()](./gcgamepadsnapshotdatav100/init%28%29.md)
- [init(version: UInt16, size: UInt16, dpadX: Float, dpadY: Float, buttonA: Float, buttonB: Float, buttonX: Float, buttonY: Float, leftShoulder: Float, rightShoulder: Float)](./gcgamepadsnapshotdatav100/init%28version,size,dpadx,dpady,buttona,buttonb,buttonx,buttony,leftshoulder,rightshoulder%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Flattening a Snapshot to Memory
- [func NSDataFromGCGamepadSnapShotDataV100(UnsafeMutablePointer<GCGamepadSnapShotDataV100>?) -> Data?](./nsdatafromgcgamepadsnapshotdatav100%28_%29.md)
  Encapsulates the controller data from a gamepad structure into a data object.
- [func GCGamepadSnapShotDataV100FromNSData(UnsafeMutablePointer<GCGamepadSnapShotDataV100>?, Data?) -> Bool](./gcgamepadsnapshotdatav100fromnsdata%28_,_%29.md)
  Copies the recorded data from a gamepad snapshot into a readable structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcgamepadsnapshotdatav100)*