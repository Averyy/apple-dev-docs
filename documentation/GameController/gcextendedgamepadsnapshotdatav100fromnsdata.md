# GCExtendedGamepadSnapShotDataV100FromNSData(_:_:)

**Framework**: Game Controller  
**Kind**: func

Copies the recorded data from an extended gamepad snapshot into a readable structure.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func GCExtendedGamepadSnapShotDataV100FromNSData(_ snapshotData: UnsafeMutablePointer<GCExtendedGamepadSnapShotDataV100>?, _ data: Data?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the data could be copied, [`false`](https://developer.apple.com/documentation/swift/false) if `snapshotData` is `nil`, `data` is `nil`, or if the contents of `data` do not contain a compatible snapshot.

## Parameters

- `snapshotData`: A pointer to memory to fill with the shapshot data.
- `data`: An   object that contains recorded data. Often, this is obtained by calling the   method of a   object.

## See Also

- [struct GCExtendedGamepadSnapShotDataV100](gcextendedgamepadsnapshotdatav100.md)
  A structure that holds a snapshot of an extended gamepad controller’s input data.
- [func NSDataFromGCExtendedGamepadSnapShotDataV100(UnsafeMutablePointer<GCExtendedGamepadSnapShotDataV100>?) -> Data?](nsdatafromgcextendedgamepadsnapshotdatav100(_:).md)
  Encapsulates the controller data from an extended gamepad structure into a data object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepadsnapshotdatav100fromnsdata(_:_:))*