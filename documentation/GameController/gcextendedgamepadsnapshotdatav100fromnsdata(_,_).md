# GCExtendedGamepadSnapShotDataV100FromNSData(_:_:)

**Framework**: Game Controller  
**Kind**: func  
**Role**: Function

Copies the recorded data from an extended gamepad snapshot into a readable structure.

**Availability**:
- iOS 7.0+ - Deprecated in 13.0
- iPadOS 7.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.9+ - Deprecated in 10.15
- tvOS 9.0+ - Deprecated in 13.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use the [`GCExtendedGamepad`](./gcextendedgamepad.md) class instead.

## Declaration

```swift
func GCExtendedGamepadSnapShotDataV100FromNSData(_ snapshotData: UnsafeMutablePointer<GCExtendedGamepadSnapShotDataV100>?, _ data: Data?) -> Bool
```

```c
BOOL GCExtendedGamepadSnapShotDataV100FromNSData(GCExtendedGamepadSnapShotDataV100 *snapshotData, NSData *data);
```

## Return Value

[`true`](../Swift/true.md) if the data could be copied, [`false`](../Swift/false.md) if `snapshotData` is `nil`, `data` is `nil`, or if the contents of `data` do not contain a compatible snapshot.

## Parameters

- `snapshotData`: A pointer to memory to fill with the shapshot data.
- `data`: An [`NSData`](../Foundation/nsdata.md) object that contains recorded data. Often, this is obtained by calling the [`snapshotData`](./gcextendedgamepadsnapshot/snapshotdata.md) method of a [`GCExtendedGamepadSnapshot`](./gcextendedgamepadsnapshot.md) object.

## See Also

### Flattening a Snapshot to Memory
- [struct GCExtendedGamepadSnapShotDataV100](./gcextendedgamepadsnapshotdatav100.md)
  A structure that holds a snapshot of an extended gamepad controller’s input data.
- [func NSDataFromGCExtendedGamepadSnapShotDataV100(UnsafeMutablePointer<GCExtendedGamepadSnapShotDataV100>?) -> Data?](./nsdatafromgcextendedgamepadsnapshotdatav100%28_%29.md)
  Encapsulates the controller data from an extended gamepad structure into a data object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepadsnapshotdatav100fromnsdata(_:_:))*