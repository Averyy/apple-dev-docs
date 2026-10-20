# GCMicroGamepadSnapShotDataV100

**Framework**: Game Controller  
**Kind**: struct  
**Role**: Structure

A structure that holds a snapshot of a micro gamepad controller’s input data.

**Availability**:
- iOS 9.0+ - Deprecated in 13.0
- iPadOS 9.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.11+ - Deprecated in 10.15
- tvOS 9.0+ - Deprecated in 13.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use the -[GCController controllerWithMicroGamepad] method instead

## Declaration

```swift
struct GCMicroGamepadSnapShotDataV100
```

```c
typedef struct { ... } GCMicroGamepadSnapShotDataV100;
```

## Topics

### Instance Properties
- [var buttonA: Float](./gcmicrogamepadsnapshotdatav100/buttona.md)
  The value of the A button.
- [var buttonX: Float](./gcmicrogamepadsnapshotdatav100/buttonx.md)
- [var dpadX: Float](./gcmicrogamepadsnapshotdatav100/dpadx.md)
  The value of the horizontal axis of the dpad.
- [var dpadY: Float](./gcmicrogamepadsnapshotdatav100/dpady.md)
  The value of the vertical axis of the dpad.
- [var size: UInt16](./gcmicrogamepadsnapshotdatav100/size.md)
  The size of the recorded structure, in bytes.
- [var version: UInt16](./gcmicrogamepadsnapshotdatav100/version.md)
  A value that indicates the version number of the data structure.
### Initializers
- [init()](./gcmicrogamepadsnapshotdatav100/init%28%29.md)
- [init(version: UInt16, size: UInt16, dpadX: Float, dpadY: Float, buttonA: Float, buttonX: Float)](./gcmicrogamepadsnapshotdatav100/init%28version,size,dpadx,dpady,buttona,buttonx%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Flattening a Snapshot to Memory
- [func NSDataFromGCMicroGamepadSnapShotDataV100(UnsafeMutablePointer<GCMicroGamepadSnapShotDataV100>?) -> Data?](./nsdatafromgcmicrogamepadsnapshotdatav100%28_%29.md)
  Encapsulates the controller data from a micro gamepad structure into a data object.
- [func GCMicroGamepadSnapShotDataV100FromNSData(UnsafeMutablePointer<GCMicroGamepadSnapShotDataV100>?, Data?) -> Bool](./gcmicrogamepadsnapshotdatav100fromnsdata%28_,_%29.md)
  Copies the recorded data from a micro gamepad snapshot into a readable structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepadsnapshotdatav100)*