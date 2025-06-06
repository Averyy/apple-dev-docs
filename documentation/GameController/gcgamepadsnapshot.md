# GCGamepadSnapshot

**Framework**: Game Controller  
**Kind**: class

A recording of all of the values provided by a [`GCGamepad`](gcgamepad.md) object.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class GCGamepadSnapshot
```

#### Overview

To create a gamepad snapshot, call the [`saveSnapshot()`](gcgamepad/savesnapshot().md) method on a [`GCGamepad`](gcgamepad.md) object. The [`GCGamepadSnapshot`](gcgamepadsnapshot.md) class is a subclass of the [`GCGamepad`](gcgamepad.md) class, so you use the parent class’s properties to read the individual element values. The snapshot is stored in a device independent format. To get the flattened data representation of the snapshot data, read the [`snapshotData`](gcgamepadsnapshot/snapshotdata.md) property.

## Topics

### Converting Between Snapshots and Data Objects
- [init(snapshotData: Data)](gcgamepadsnapshot/init(snapshotdata:).md)
  Initializes a snapshot object with the flattened data representation obtained from another snapshot.
- [init(controller: GCController, snapshotData: Data)](gcgamepadsnapshot/init(controller:snapshotdata:).md)
  Initializes a snapshot object associated with a specific controller using a flattened data representation obtained from another snapshot.
- [var snapshotData: Data](gcgamepadsnapshot/snapshotdata.md)
  The flattened control input values for the snapshot.
### Flattening a Snapshot to Memory
- [struct GCGamepadSnapShotDataV100](gcgamepadsnapshotdatav100.md)
  A structure that holds a snapshot of a gamepad controller’s input data.
- [func NSDataFromGCGamepadSnapShotDataV100(UnsafeMutablePointer<GCGamepadSnapShotDataV100>?) -> Data?](nsdatafromgcgamepadsnapshotdatav100(_:).md)
  Encapsulates the controller data from a gamepad structure into a data object.
- [func GCGamepadSnapShotDataV100FromNSData(UnsafeMutablePointer<GCGamepadSnapShotDataV100>?, Data?) -> Bool](gcgamepadsnapshotdatav100fromnsdata(_:_:).md)
  Copies the recorded data from a gamepad snapshot into a readable structure.

## Relationships

### Inherits From
- [GCGamepad](gcgamepad.md)
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
- [class GCExtendedGamepadSnapshot](gcextendedgamepadsnapshot.md)
  A recording of all of the values provided by a [`GCExtendedGamepad`](gcextendedgamepad.md) object.
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

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcgamepadsnapshot)*