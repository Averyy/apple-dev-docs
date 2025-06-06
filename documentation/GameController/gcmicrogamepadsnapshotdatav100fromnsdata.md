# GCMicroGamepadSnapShotDataV100FromNSData(_:_:)

**Framework**: Game Controller  
**Kind**: func

Copies the recorded data from a micro gamepad snapshot into a readable structure.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func GCMicroGamepadSnapShotDataV100FromNSData(_ snapshotData: UnsafeMutablePointer<GCMicroGamepadSnapShotDataV100>?, _ data: Data?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the data could be copied, [`false`](https://developer.apple.com/documentation/swift/false) if `snapshotData` is `nil`, `data` is `nil`, or if the contents of `data` do not contain a compatible snapshot.

## Parameters

- `snapshotData`: A pointer to memory to fill with the shapshot data.
- `data`: An   object that contains recorded data. Often, this is obtained by calling the   method of a   object.

## See Also

- [struct GCMicroGamepadSnapShotDataV100](gcmicrogamepadsnapshotdatav100.md)
  A structure that holds a snapshot of a micro gamepad controller’s input data.
- [func NSDataFromGCMicroGamepadSnapShotDataV100(UnsafeMutablePointer<GCMicroGamepadSnapShotDataV100>?) -> Data?](nsdatafromgcmicrogamepadsnapshotdatav100(_:).md)
  Encapsulates the controller data from a micro gamepad structure into a data object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepadsnapshotdatav100fromnsdata(_:_:))*