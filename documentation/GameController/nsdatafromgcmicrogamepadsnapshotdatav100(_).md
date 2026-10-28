# NSDataFromGCMicroGamepadSnapShotDataV100(_:)

**Framework**: Game Controller  
**Kind**: func  
**Role**: Function

Encapsulates the controller data from a micro gamepad structure into a data object.

**Availability**:
- iOS 9.0+ - Deprecated in 13.0
- iPadOS 9.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.11+ - Deprecated in 10.15
- tvOS 9.0+ - Deprecated in 13.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use the [`withMicroGamepad()`](./gccontroller/withmicrogamepad%28%29.md) method instead.

## Declaration

```swift
func NSDataFromGCMicroGamepadSnapShotDataV100(_ snapshotData: UnsafeMutablePointer<GCMicroGamepadSnapShotDataV100>?) -> Data?
```

```c
NSData *NSDataFromGCMicroGamepadSnapShotDataV100(GCMicroGamepadSnapShotDataV100 *snapshotData);
```

## Return Value

A new [`NSData`](../Foundation/nsdata.md) object that contains the snapshot data, or `nil` if an error occurred.

## Discussion

If the version and size is not set in the snapshot the data will automatically have a version of `0x100` and a size equal to `sizeof(GCMicroGamepadSnapShotDataV100)`.

## Parameters

- `snapshotData`: A pointer to memory that contains a set of gamepad control values.

## See Also

### Flattening a Snapshot to Memory
- [struct GCMicroGamepadSnapShotDataV100](./gcmicrogamepadsnapshotdatav100.md)
  A structure that holds a snapshot of a micro gamepad controller’s input data.
- [func GCMicroGamepadSnapShotDataV100FromNSData(UnsafeMutablePointer<GCMicroGamepadSnapShotDataV100>?, Data?) -> Bool](./gcmicrogamepadsnapshotdatav100fromnsdata%28_,_%29.md)
  Copies the recorded data from a micro gamepad snapshot into a readable structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/nsdatafromgcmicrogamepadsnapshotdatav100(_:))*