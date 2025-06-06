# NSDataFromGCMicroGamepadSnapShotDataV100(_:)

**Framework**: Game Controller  
**Kind**: func

Encapsulates the controller data from a micro gamepad structure into a data object.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func NSDataFromGCMicroGamepadSnapShotDataV100(_ snapshotData: UnsafeMutablePointer<GCMicroGamepadSnapShotDataV100>?) -> Data?
```

#### Return Value

A new [`NSData`](https://developer.apple.com/documentation/Foundation/NSData) object that contains the snapshot data, or `nil` if an error occurred.

#### Discussion

If the version and size is not set in the snapshot the data will automatically have a version of `0x100` and a size equal to `sizeof(GCMicroGamepadSnapShotDataV100)`.

## Parameters

- `snapshotData`: A pointer to memory that contains a set of gamepad control values.

## See Also

- [struct GCMicroGamepadSnapShotDataV100](gcmicrogamepadsnapshotdatav100.md)
  A structure that holds a snapshot of a micro gamepad controller’s input data.
- [func GCMicroGamepadSnapShotDataV100FromNSData(UnsafeMutablePointer<GCMicroGamepadSnapShotDataV100>?, Data?) -> Bool](gcmicrogamepadsnapshotdatav100fromnsdata(_:_:).md)
  Copies the recorded data from a micro gamepad snapshot into a readable structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/nsdatafromgcmicrogamepadsnapshotdatav100(_:))*