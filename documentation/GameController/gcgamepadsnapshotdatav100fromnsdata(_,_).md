# GCGamepadSnapShotDataV100FromNSData(_:_:)

**Framework**: Game Controller  
**Kind**: func  
**Role**: Function

Copies the recorded data from a gamepad snapshot into a readable structure.

**Availability**:
- iOS 7.0+ - Deprecated in 13.0
- iPadOS 7.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.9+ - Deprecated in 10.15
- tvOS 9.0+ - Deprecated in 13.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use GCExtendedGamepad instead

## Declaration

```swift
func GCGamepadSnapShotDataV100FromNSData(_ snapshotData: UnsafeMutablePointer<GCGamepadSnapShotDataV100>?, _ data: Data?) -> Bool
```

```c
BOOL GCGamepadSnapShotDataV100FromNSData(GCGamepadSnapShotDataV100 *snapshotData, NSData *data);
```

## Return Value

[`true`](../Swift/true.md) if the data could be copied, [`false`](../Swift/false.md) if `snapshotData` is `nil`, `data` is `nil`, or if the contents of `data` do not contain a compatible snapshot.

## Parameters

- `snapshotData`: A pointer to memory to fill with the shapshot data.
- `data`: An [`NSData`](../Foundation/nsdata.md) object that contains recorded data. Often, this is obtained by calling the [`snapshotData`](./gcgamepadsnapshot/snapshotdata.md) method of a [`GCGamepadSnapshot`](./gcgamepadsnapshot.md) object.

## See Also

### Flattening a Snapshot to Memory
- [struct GCGamepadSnapShotDataV100](./gcgamepadsnapshotdatav100.md)
  A structure that holds a snapshot of a gamepad controller’s input data.
- [func NSDataFromGCGamepadSnapShotDataV100(UnsafeMutablePointer<GCGamepadSnapShotDataV100>?) -> Data?](./nsdatafromgcgamepadsnapshotdatav100%28_%29.md)
  Encapsulates the controller data from a gamepad structure into a data object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcgamepadsnapshotdatav100fromnsdata(_:_:))*