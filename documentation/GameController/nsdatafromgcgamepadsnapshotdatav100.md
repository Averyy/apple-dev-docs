# NSDataFromGCGamepadSnapShotDataV100(_:)

**Framework**: Game Controller  
**Kind**: func

Encapsulates the controller data from a gamepad structure into a data object.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func NSDataFromGCGamepadSnapShotDataV100(_ snapshotData: UnsafeMutablePointer<GCGamepadSnapShotDataV100>?) -> Data?
```

#### Return Value

A new [`NSData`](https://developer.apple.com/documentation/Foundation/NSData) object that contains the snapshot data, or `nil` if an error occurred.

#### Discussion

If the version and size is not set in the snapshot the data will automatically have a version of `0x100` and a size equal to `sizeof(GCGamepadSnapShotDataV100)`.

## Parameters

- `snapshotData`: A pointer to memory that contains a set of gamepad control values.

## See Also

- [struct GCGamepadSnapShotDataV100](gcgamepadsnapshotdatav100.md)
  A structure that holds a snapshot of a gamepad controller’s input data.
- [func GCGamepadSnapShotDataV100FromNSData(UnsafeMutablePointer<GCGamepadSnapShotDataV100>?, Data?) -> Bool](gcgamepadsnapshotdatav100fromnsdata(_:_:).md)
  Copies the recorded data from a gamepad snapshot into a readable structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/nsdatafromgcgamepadsnapshotdatav100(_:))*