# GCMicroGamepadSnapShotDataV100FromNSData(_:_:)

**Framework**: Game Controller  
**Kind**: func  
**Role**: Function

Copies the recorded data from a micro gamepad snapshot into a readable structure.

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
func GCMicroGamepadSnapShotDataV100FromNSData(_ snapshotData: UnsafeMutablePointer<GCMicroGamepadSnapShotDataV100>?, _ data: Data?) -> Bool
```

```c
BOOL GCMicroGamepadSnapShotDataV100FromNSData(GCMicroGamepadSnapShotDataV100 *snapshotData, NSData *data);
```

#### Return Value

[`true`](../Swift/true.md) if the data could be copied, [`false`](../Swift/false.md) if `snapshotData` is `nil`, `data` is `nil`, or if the contents of `data` do not contain a compatible snapshot.

## Parameters

- `snapshotData`: A pointer to memory to fill with the shapshot data.
- `data`: An [`NSData`](../Foundation/nsdata.md) object that contains recorded data. Often, this is obtained by calling the [`snapshotData`](./gcgamepadsnapshot/snapshotdata.md) method of a  `GCMicroGamepadSnapshot`object.

## See Also

### Flattening a Snapshot to Memory
- [struct GCMicroGamepadSnapShotDataV100](./gcmicrogamepadsnapshotdatav100.md)
  A structure that holds a snapshot of a micro gamepad controller’s input data.
- [func NSDataFromGCMicroGamepadSnapShotDataV100(UnsafeMutablePointer<GCMicroGamepadSnapShotDataV100>?) -> Data?](./nsdatafromgcmicrogamepadsnapshotdatav100%28_%29.md)
  Encapsulates the controller data from a micro gamepad structure into a data object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepadsnapshotdatav100fromnsdata(_:_:))*