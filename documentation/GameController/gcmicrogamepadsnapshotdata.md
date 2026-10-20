# GCMicroGamepadSnapshotData

**Framework**: Game Controller  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 13.0+ - Deprecated in 13.0
- iPadOS 13.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.15+ - Deprecated in 10.15
- tvOS 13.0+ - Deprecated in 13.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use the -[GCController controllerWithMicroGamepad] method instead

## Declaration

```swift
struct GCMicroGamepadSnapshotData
```

```c
typedef struct { ... } GCMicroGamepadSnapshotData;
```

## Topics

### Initializers
- [init()](./gcmicrogamepadsnapshotdata/init%28%29.md)
- [init(version: UInt16, size: UInt16, dpadX: Float, dpadY: Float, buttonA: Float, buttonX: Float)](./gcmicrogamepadsnapshotdata/init%28version,size,dpadx,dpady,buttona,buttonx%29.md)
### Instance Properties
- [var buttonA: Float](./gcmicrogamepadsnapshotdata/buttona.md)
- [var buttonX: Float](./gcmicrogamepadsnapshotdata/buttonx.md)
- [var dpadX: Float](./gcmicrogamepadsnapshotdata/dpadx.md)
- [var dpadY: Float](./gcmicrogamepadsnapshotdata/dpady.md)
- [var size: UInt16](./gcmicrogamepadsnapshotdata/size.md)
- [var version: UInt16](./gcmicrogamepadsnapshotdata/version.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Deprecated symbols
- [class GCGamepad](./gcgamepad.md)
  The standard set of gamepad controls.
- [class GCExtendedGamepadSnapshot](./gcextendedgamepadsnapshot.md)
  A recording of all of the values provided by a [`GCExtendedGamepad`](./gcextendedgamepad.md) object.
- [class GCGamepadSnapshot](./gcgamepadsnapshot.md)
  A recording of all of the values provided by a [`GCGamepad`](./gcgamepad.md) object.
- [class GCMicroGamepadSnapshot](./gcmicrogamepadsnapshot.md)
  A recording of all of the values provided by a [`GCMicroGamepad`](./gcmicrogamepad.md) object.
- [struct GCExtendedGamepadSnapshotData](./gcextendedgamepadsnapshotdata.md)
- [enum GCExtendedGamepadSnapshotDataVersion](./gcextendedgamepadsnapshotdataversion.md)
- [enum GCMicroGamepadSnapshotDataVersion](./gcmicrogamepadsnapshotdataversion.md)
- [let GCCurrentExtendedGamepadSnapshotDataVersion: GCExtendedGamepadSnapshotDataVersion](./gccurrentextendedgamepadsnapshotdataversion.md)
- [let GCCurrentMicroGamepadSnapshotDataVersion: GCMicroGamepadSnapshotDataVersion](./gccurrentmicrogamepadsnapshotdataversion.md)
- [func GCExtendedGamepadSnapshotDataFromNSData(UnsafeMutablePointer<GCExtendedGamepadSnapshotData>?, Data?) -> Bool](./gcextendedgamepadsnapshotdatafromnsdata%28_,_%29.md)
- [func GCMicroGamepadSnapshotDataFromNSData(UnsafeMutablePointer<GCMicroGamepadSnapshotData>?, Data?) -> Bool](./gcmicrogamepadsnapshotdatafromnsdata%28_,_%29.md)
- [func NSDataFromGCExtendedGamepadSnapshotData(UnsafeMutablePointer<GCExtendedGamepadSnapshotData>?) -> Data?](./nsdatafromgcextendedgamepadsnapshotdata%28_%29.md)
- [func NSDataFromGCMicroGamepadSnapshotData(UnsafeMutablePointer<GCMicroGamepadSnapshotData>?) -> Data?](./nsdatafromgcmicrogamepadsnapshotdata%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepadsnapshotdata)*