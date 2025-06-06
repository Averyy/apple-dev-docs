# GCExtendedGamepadSnapshot

**Framework**: Game Controller  
**Kind**: class

A recording of all of the values provided by a [`GCExtendedGamepad`](gcextendedgamepad.md) object.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class GCExtendedGamepadSnapshot
```

#### Overview

To create a gamepad snapshot, call the [`saveSnapshot()`](gcextendedgamepad/savesnapshot().md) method on a [`GCExtendedGamepad`](gcextendedgamepad.md) object. The [`GCExtendedGamepadSnapshot`](gcextendedgamepadsnapshot.md) class is a subclass of the [`GCExtendedGamepad`](gcextendedgamepad.md) class, so you use the parent class’s properties to read the individual element values. The snapshot is stored in a device independent format. To get the flattened data representation of the snapshot data, read the [`snapshotData`](gcextendedgamepadsnapshot/snapshotdata.md) property.

## Topics

### Converting Between Extended Snapshots and Data Objects
- [init(snapshotData: Data)](gcextendedgamepadsnapshot/init(snapshotdata:).md)
  Initializes a snapshot object with the flattened data representation obtained from another snapshot.
- [init(controller: GCController, snapshotData: Data)](gcextendedgamepadsnapshot/init(controller:snapshotdata:).md)
  Initializes a snapshot object associated with a specific controller using a flattened data representation obtained from another snapshot.
- [var snapshotData: Data](gcextendedgamepadsnapshot/snapshotdata.md)
  Flattens a snapshot into an archivable memory representation.
### Flattening a Snapshot to Memory
- [struct GCExtendedGamepadSnapShotDataV100](gcextendedgamepadsnapshotdatav100.md)
  A structure that holds a snapshot of an extended gamepad controller’s input data.
- [func NSDataFromGCExtendedGamepadSnapShotDataV100(UnsafeMutablePointer<GCExtendedGamepadSnapShotDataV100>?) -> Data?](nsdatafromgcextendedgamepadsnapshotdatav100(_:).md)
  Encapsulates the controller data from an extended gamepad structure into a data object.
- [func GCExtendedGamepadSnapShotDataV100FromNSData(UnsafeMutablePointer<GCExtendedGamepadSnapShotDataV100>?, Data?) -> Bool](gcextendedgamepadsnapshotdatav100fromnsdata(_:_:).md)
  Copies the recorded data from an extended gamepad snapshot into a readable structure.

## Relationships

### Inherits From
- [GCExtendedGamepad](gcextendedgamepad.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class GCGamepad](gcgamepad.md)
  The standard set of gamepad controls.
- [class GCGamepadSnapshot](gcgamepadsnapshot.md)
  A recording of all of the values provided by a [`GCGamepad`](gcgamepad.md) object.
- [class GCMicroGamepadSnapshot](gcmicrogamepadsnapshot.md)
  A recording of all of the values provided by a [`GCMicroGamepad`](gcmicrogamepad.md) object.
- [struct GCExtendedGamepadSnapshotData](gcextendedgamepadsnapshotdata.md)
- [struct GCMicroGamepadSnapshotData](gcmicrogamepadsnapshotdata.md)
- [enum GCExtendedGamepadSnapshotDataVersion](gcextendedgamepadsnapshotdataversion.md)
- [enum GCMicroGamepadSnapshotDataVersion](gcmicrogamepadsnapshotdataversion.md)
- [let GCCurrentExtendedGamepadSnapshotDataVersion: GCExtendedGamepadSnapshotDataVersion](gccurrentextendedgamepadsnapshotdataversion.md)
- [let GCCurrentMicroGamepadSnapshotDataVersion: GCMicroGamepadSnapshotDataVersion](gccurrentmicrogamepadsnapshotdataversion.md)
- [func GCExtendedGamepadSnapshotDataFromNSData(UnsafeMutablePointer<GCExtendedGamepadSnapshotData>?, Data?) -> Bool](gcextendedgamepadsnapshotdatafromnsdata(_:_:).md)
- [func GCMicroGamepadSnapshotDataFromNSData(UnsafeMutablePointer<GCMicroGamepadSnapshotData>?, Data?) -> Bool](gcmicrogamepadsnapshotdatafromnsdata(_:_:).md)
- [func NSDataFromGCExtendedGamepadSnapshotData(UnsafeMutablePointer<GCExtendedGamepadSnapshotData>?) -> Data?](nsdatafromgcextendedgamepadsnapshotdata(_:).md)
- [func NSDataFromGCMicroGamepadSnapshotData(UnsafeMutablePointer<GCMicroGamepadSnapshotData>?) -> Data?](nsdatafromgcmicrogamepadsnapshotdata(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepadsnapshot)*