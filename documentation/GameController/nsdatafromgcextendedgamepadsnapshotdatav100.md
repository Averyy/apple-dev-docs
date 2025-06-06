# NSDataFromGCExtendedGamepadSnapShotDataV100(_:)

**Framework**: Game Controller  
**Kind**: func

Encapsulates the controller data from an extended gamepad structure into a data object.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func NSDataFromGCExtendedGamepadSnapShotDataV100(_ snapshotData: UnsafeMutablePointer<GCExtendedGamepadSnapShotDataV100>?) -> Data?
```

#### Return Value

A new [`NSData`](https://developer.apple.com/documentation/Foundation/NSData) object that contains the snapshot data, or `nil` if an error occurred.

#### Discussion

If the version and size is not set in the snapshot the data will automatically have a version of `0x100` and a size equal to `sizeof(GCExtendedGamepadSnapShotDataV100)`.

## Parameters

- `snapshotData`: A pointer to memory that contains a set of extended gamepad control values.

## See Also

- [struct GCExtendedGamepadSnapShotDataV100](gcextendedgamepadsnapshotdatav100.md)
  A structure that holds a snapshot of an extended gamepad controller’s input data.
- [func GCExtendedGamepadSnapShotDataV100FromNSData(UnsafeMutablePointer<GCExtendedGamepadSnapShotDataV100>?, Data?) -> Bool](gcextendedgamepadsnapshotdatav100fromnsdata(_:_:).md)
  Copies the recorded data from an extended gamepad snapshot into a readable structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/nsdatafromgcextendedgamepadsnapshotdatav100(_:))*