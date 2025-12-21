# GCGamepadSnapShotDataV100FromNSData(_:_:)

**Framework**: Game Controller  
**Kind**: func

Copies the recorded data from a gamepad snapshot into a readable structure.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func GCGamepadSnapShotDataV100FromNSData(_ snapshotData: UnsafeMutablePointer<GCGamepadSnapShotDataV100>?, _ data: Data?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the data could be copied, [`false`](https://developer.apple.com/documentation/Swift/false) if `snapshotData` is `nil`, `data` is `nil`, or if the contents of `data` do not contain a compatible snapshot.

## Parameters

- `snapshotData`: A pointer to memory to fill with the shapshot data.
- `data`: An   object that contains recorded data. Often, this is obtained by calling the   method of a   object.

## See Also

- [struct GCGamepadSnapShotDataV100](gcgamepadsnapshotdatav100.md)
  A structure that holds a snapshot of a gamepad controller’s input data.
- [func NSDataFromGCGamepadSnapShotDataV100(UnsafeMutablePointer<GCGamepadSnapShotDataV100>?) -> Data?](nsdatafromgcgamepadsnapshotdatav100(_:).md)
  Encapsulates the controller data from a gamepad structure into a data object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcgamepadsnapshotdatav100fromnsdata(_:_:))*