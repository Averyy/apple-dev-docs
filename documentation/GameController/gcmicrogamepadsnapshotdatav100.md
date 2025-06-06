# GCMicroGamepadSnapShotDataV100

**Framework**: Game Controller  
**Kind**: struct

A structure that holds a snapshot of a micro gamepad controller’s input data.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
struct GCMicroGamepadSnapShotDataV100
```

## Topics

### Instance Properties
- [var buttonA: Float](gcmicrogamepadsnapshotdatav100/buttona.md)
  The value of the A button.
- [var buttonX: Float](gcmicrogamepadsnapshotdatav100/buttonx.md)
- [var dpadX: Float](gcmicrogamepadsnapshotdatav100/dpadx.md)
  The value of the horizontal axis of the dpad.
- [var dpadY: Float](gcmicrogamepadsnapshotdatav100/dpady.md)
  The value of the vertical axis of the dpad.
- [var size: UInt16](gcmicrogamepadsnapshotdatav100/size.md)
  The size of the recorded structure, in bytes.
- [var version: UInt16](gcmicrogamepadsnapshotdatav100/version.md)
  A value that indicates the version number of the data structure.
### Initializers
- [init()](gcmicrogamepadsnapshotdatav100/init.md)
- [init(version: UInt16, size: UInt16, dpadX: Float, dpadY: Float, buttonA: Float, buttonX: Float)](gcmicrogamepadsnapshotdatav100/init(version:size:dpadx:dpady:buttona:buttonx:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func NSDataFromGCMicroGamepadSnapShotDataV100(UnsafeMutablePointer<GCMicroGamepadSnapShotDataV100>?) -> Data?](nsdatafromgcmicrogamepadsnapshotdatav100(_:).md)
  Encapsulates the controller data from a micro gamepad structure into a data object.
- [func GCMicroGamepadSnapShotDataV100FromNSData(UnsafeMutablePointer<GCMicroGamepadSnapShotDataV100>?, Data?) -> Bool](gcmicrogamepadsnapshotdatav100fromnsdata(_:_:).md)
  Copies the recorded data from a micro gamepad snapshot into a readable structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepadsnapshotdatav100)*