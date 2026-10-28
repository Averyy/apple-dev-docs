# GCGamepadSnapshot

**Framework**: Game Controller  
**Kind**: class  
**Role**: Class

A recording of all of the values provided by a [`GCGamepad`](./gcgamepad.md) object.

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
class GCGamepadSnapshot
```

```objc
@interface GCGamepadSnapshot : GCGamepad
```

## Overview

To create a gamepad snapshot, call the [`saveSnapshot()`](./gcgamepad/savesnapshot%28%29.md) method on a [`GCGamepad`](./gcgamepad.md) object. The [`GCGamepadSnapshot`](./gcgamepadsnapshot.md) class is a subclass of the [`GCGamepad`](./gcgamepad.md) class, so you use the parent class’s properties to read the individual element values. The snapshot is stored in a device independent format. To get the flattened data representation of the snapshot data, read the [`snapshotData`](./gcgamepadsnapshot/snapshotdata.md) property.

## Topics

### Converting Between Snapshots and Data Objects
- [init(snapshotData: Data)](./gcgamepadsnapshot/init%28snapshotdata%29.md)
  Initializes a snapshot object with the flattened data representation obtained from another snapshot.
- [init(controller: GCController, snapshotData: Data)](./gcgamepadsnapshot/init%28controller,snapshotdata%29.md)
  Initializes a snapshot object associated with a specific controller using a flattened data representation obtained from another snapshot.
- [var snapshotData: Data](./gcgamepadsnapshot/snapshotdata.md)
  The flattened control input values for the snapshot.
### Flattening a Snapshot to Memory
- [struct GCGamepadSnapShotDataV100](./gcgamepadsnapshotdatav100.md)
  A structure that holds a snapshot of a gamepad controller’s input data.
- [func NSDataFromGCGamepadSnapShotDataV100(UnsafeMutablePointer<GCGamepadSnapShotDataV100>?) -> Data?](./nsdatafromgcgamepadsnapshotdatav100%28_%29.md)
  Encapsulates the controller data from a gamepad structure into a data object.
- [func GCGamepadSnapShotDataV100FromNSData(UnsafeMutablePointer<GCGamepadSnapShotDataV100>?, Data?) -> Bool](./gcgamepadsnapshotdatav100fromnsdata%28_,_%29.md)
  Copies the recorded data from a gamepad snapshot into a readable structure.

## Relationships

### Inherits From
- [GCGamepad](./gcgamepad.md)
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
- [class GCExtendedGamepadSnapshot](./gcextendedgamepadsnapshot.md)
  A recording of all of the values provided by a [`GCExtendedGamepad`](./gcextendedgamepad.md) object.
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

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcgamepadsnapshot)*