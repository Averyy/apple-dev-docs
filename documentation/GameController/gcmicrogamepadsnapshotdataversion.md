# GCMicroGamepadSnapshotDataVersion

**Framework**: Game Controller  
**Kind**: enum  
**Role**: Enumeration

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
enum GCMicroGamepadSnapshotDataVersion
```

```c
enum GCMicroGamepadSnapshotDataVersion : NSInteger;
```

## Topics

### Enumeration Cases
- [GCMicroGamepadSnapshotDataVersion.version1](./gcmicrogamepadsnapshotdataversion/version1.md)
### Initializers
- [init?(rawValue: Int)](./gcmicrogamepadsnapshotdataversion/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

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
- [struct GCMicroGamepadSnapshotData](./gcmicrogamepadsnapshotdata.md)
- [enum GCExtendedGamepadSnapshotDataVersion](./gcextendedgamepadsnapshotdataversion.md)
- [let GCCurrentExtendedGamepadSnapshotDataVersion: GCExtendedGamepadSnapshotDataVersion](./gccurrentextendedgamepadsnapshotdataversion.md)
- [let GCCurrentMicroGamepadSnapshotDataVersion: GCMicroGamepadSnapshotDataVersion](./gccurrentmicrogamepadsnapshotdataversion.md)
- [func GCExtendedGamepadSnapshotDataFromNSData(UnsafeMutablePointer<GCExtendedGamepadSnapshotData>?, Data?) -> Bool](./gcextendedgamepadsnapshotdatafromnsdata%28_,_%29.md)
- [func GCMicroGamepadSnapshotDataFromNSData(UnsafeMutablePointer<GCMicroGamepadSnapshotData>?, Data?) -> Bool](./gcmicrogamepadsnapshotdatafromnsdata%28_,_%29.md)
- [func NSDataFromGCExtendedGamepadSnapshotData(UnsafeMutablePointer<GCExtendedGamepadSnapshotData>?) -> Data?](./nsdatafromgcextendedgamepadsnapshotdata%28_%29.md)
- [func NSDataFromGCMicroGamepadSnapshotData(UnsafeMutablePointer<GCMicroGamepadSnapshotData>?) -> Data?](./nsdatafromgcmicrogamepadsnapshotdata%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepadsnapshotdataversion)*