# GCMicroGamepadSnapshot

**Framework**: Game Controller  
**Kind**: class

A recording of all of the values provided by a [`GCMicroGamepad`](gcmicrogamepad.md) object.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class GCMicroGamepadSnapshot
```

#### Overview

To create a gamepad snapshot, call the [`saveSnapshot()`](gcgamepad/savesnapshot().md) method on a [`GCMicroGamepad`](gcmicrogamepad.md) object. The [`GCMicroGamepadSnapshot`](gcmicrogamepadsnapshot.md) class is a subclass of the [`GCMicroGamepad`](gcmicrogamepad.md) class, so you use the parent class’s properties to read the individual element values. The snapshot is stored in a device independent format. To get the flattened data representation of the snapshot data, read the [`snapshotData`](gcmicrogamepadsnapshot/snapshotdata.md) property.

## Topics

### Converting Between Snapshots and Data Objects
- [init(snapshotData: Data)](gcmicrogamepadsnapshot/init(snapshotdata:).md)
  Initializes a snapshot object with the flattened data representation obtained from another snapshot.
- [init(controller: GCController, snapshotData: Data)](gcmicrogamepadsnapshot/init(controller:snapshotdata:).md)
- [var snapshotData: Data](gcmicrogamepadsnapshot/snapshotdata.md)
  The flattened control input values for the snapshot.
### Flattening a Snapshot to Memory
- [struct GCMicroGamepadSnapShotDataV100](gcmicrogamepadsnapshotdatav100.md)
  A structure that holds a snapshot of a micro gamepad controller’s input data.
- [func NSDataFromGCMicroGamepadSnapShotDataV100(UnsafeMutablePointer<GCMicroGamepadSnapShotDataV100>?) -> Data?](nsdatafromgcmicrogamepadsnapshotdatav100(_:).md)
  Encapsulates the controller data from a micro gamepad structure into a data object.
- [func GCMicroGamepadSnapShotDataV100FromNSData(UnsafeMutablePointer<GCMicroGamepadSnapShotDataV100>?, Data?) -> Bool](gcmicrogamepadsnapshotdatav100fromnsdata(_:_:).md)
  Copies the recorded data from a micro gamepad snapshot into a readable structure.

## Relationships

### Inherits From
- [GCMicroGamepad](gcmicrogamepad.md)
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
- [class GCGamepadSnapshot](gcgamepadsnapshot.md)
  A recording of all of the values provided by a [`GCGamepad`](gcgamepad.md) object.
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

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepadsnapshot)*