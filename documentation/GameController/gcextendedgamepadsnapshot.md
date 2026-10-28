# GCExtendedGamepadSnapshot

**Framework**: Game Controller  
**Kind**: class  
**Role**: Class

A recording of all of the values provided by a [`GCExtendedGamepad`](./gcextendedgamepad.md) object.

**Availability**:
- iOS 7.0+ - Deprecated in 13.0
- iPadOS 7.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.9+ - Deprecated in 10.15
- tvOS 9.0+ - Deprecated in 13.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use the [`withExtendedGamepad()`](./gccontroller/withextendedgamepad%28%29.md) method instead.

## Declaration

```swift
class GCExtendedGamepadSnapshot
```

```objc
@interface GCExtendedGamepadSnapshot : GCExtendedGamepad
```

## Overview

To create a gamepad snapshot, call the [`saveSnapshot()`](./gcextendedgamepad/savesnapshot%28%29.md) method on a [`GCExtendedGamepad`](./gcextendedgamepad.md) object. The [`GCExtendedGamepadSnapshot`](./gcextendedgamepadsnapshot.md) class is a subclass of the [`GCExtendedGamepad`](./gcextendedgamepad.md) class, so you use the parent class’s properties to read the individual element values. The snapshot is stored in a device independent format. To get the flattened data representation of the snapshot data, read the [`snapshotData`](./gcextendedgamepadsnapshot/snapshotdata.md) property.

## Topics

### Converting Between Extended Snapshots and Data Objects
- [init(snapshotData: Data)](./gcextendedgamepadsnapshot/init%28snapshotdata%29.md)
  Initializes a snapshot object with the flattened data representation obtained from another snapshot.
- [init(controller: GCController, snapshotData: Data)](./gcextendedgamepadsnapshot/init%28controller,snapshotdata%29.md)
  Initializes a snapshot object associated with a specific controller using a flattened data representation obtained from another snapshot.
- [var snapshotData: Data](./gcextendedgamepadsnapshot/snapshotdata.md)
  Flattens a snapshot into an archivable memory representation.
### Flattening a Snapshot to Memory
- [struct GCExtendedGamepadSnapShotDataV100](./gcextendedgamepadsnapshotdatav100.md)
  A structure that holds a snapshot of an extended gamepad controller’s input data.
- [func NSDataFromGCExtendedGamepadSnapShotDataV100(UnsafeMutablePointer<GCExtendedGamepadSnapShotDataV100>?) -> Data?](./nsdatafromgcextendedgamepadsnapshotdatav100%28_%29.md)
  Encapsulates the controller data from an extended gamepad structure into a data object.
- [func GCExtendedGamepadSnapShotDataV100FromNSData(UnsafeMutablePointer<GCExtendedGamepadSnapShotDataV100>?, Data?) -> Bool](./gcextendedgamepadsnapshotdatav100fromnsdata%28_,_%29.md)
  Copies the recorded data from an extended gamepad snapshot into a readable structure.

## Relationships

### Inherits From
- [GCExtendedGamepad](./gcextendedgamepad.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Deprecated symbols
- [class GCGamepad](./gcgamepad.md)
  The standard set of gamepad controls.
- [class GCGamepadSnapshot](./gcgamepadsnapshot.md)
  A recording of all of the values provided by a [`GCGamepad`](./gcgamepad.md) object.
- [class GCMicroGamepadSnapshot](./gcmicrogamepadsnapshot.md)
  A recording of all of the values provided by a [`GCMicroGamepad`](./gcmicrogamepad.md) object.
- [struct GCExtendedGamepadSnapshotData](./gcextendedgamepadsnapshotdata.md)
- [struct GCMicroGamepadSnapshotData](./gcmicrogamepadsnapshotdata.md)
- [enum GCExtendedGamepadSnapshotDataVersion](./gcextendedgamepadsnapshotdataversion.md)
- [enum GCMicroGamepadSnapshotDataVersion](./gcmicrogamepadsnapshotdataversion.md)
- [let GCCurrentExtendedGamepadSnapshotDataVersion: GCExtendedGamepadSnapshotDataVersion](./gccurrentextendedgamepadsnapshotdataversion.md)
- [let GCCurrentMicroGamepadSnapshotDataVersion: GCMicroGamepadSnapshotDataVersion](./gccurrentmicrogamepadsnapshotdataversion.md)
- [func GCExtendedGamepadSnapshotDataFromNSData(UnsafeMutablePointer<GCExtendedGamepadSnapshotData>?, Data?) -> Bool](./gcextendedgamepadsnapshotdatafromnsdata%28_,_%29.md)
- [func GCMicroGamepadSnapshotDataFromNSData(UnsafeMutablePointer<GCMicroGamepadSnapshotData>?, Data?) -> Bool](./gcmicrogamepadsnapshotdatafromnsdata%28_,_%29.md)
- [func NSDataFromGCExtendedGamepadSnapshotData(UnsafeMutablePointer<GCExtendedGamepadSnapshotData>?) -> Data?](./nsdatafromgcextendedgamepadsnapshotdata%28_%29.md)
- [func NSDataFromGCMicroGamepadSnapshotData(UnsafeMutablePointer<GCMicroGamepadSnapshotData>?) -> Data?](./nsdatafromgcmicrogamepadsnapshotdata%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepadsnapshot)*