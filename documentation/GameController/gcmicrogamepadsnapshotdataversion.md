# GCMicroGamepadSnapshotDataVersion

**Framework**: Game Controller  
**Kind**: enum

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
enum GCMicroGamepadSnapshotDataVersion
```

## Topics

### Enumeration Cases
- [GCMicroGamepadSnapshotDataVersion.version1](gcmicrogamepadsnapshotdataversion/version1.md)
### Initializers
- [init?(rawValue: Int)](gcmicrogamepadsnapshotdataversion/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class GCGamepad](gcgamepad.md)
  The standard set of gamepad controls.
- [class GCExtendedGamepadSnapshot](gcextendedgamepadsnapshot.md)
  A recording of all of the values provided by a [`GCExtendedGamepad`](gcextendedgamepad.md) object.
- [class GCGamepadSnapshot](gcgamepadsnapshot.md)
  A recording of all of the values provided by a [`GCGamepad`](gcgamepad.md) object.
- [class GCMicroGamepadSnapshot](gcmicrogamepadsnapshot.md)
  A recording of all of the values provided by a [`GCMicroGamepad`](gcmicrogamepad.md) object.
- [struct GCExtendedGamepadSnapshotData](gcextendedgamepadsnapshotdata.md)
- [struct GCMicroGamepadSnapshotData](gcmicrogamepadsnapshotdata.md)
- [enum GCExtendedGamepadSnapshotDataVersion](gcextendedgamepadsnapshotdataversion.md)
- [let GCCurrentExtendedGamepadSnapshotDataVersion: GCExtendedGamepadSnapshotDataVersion](gccurrentextendedgamepadsnapshotdataversion.md)
- [let GCCurrentMicroGamepadSnapshotDataVersion: GCMicroGamepadSnapshotDataVersion](gccurrentmicrogamepadsnapshotdataversion.md)
- [func GCExtendedGamepadSnapshotDataFromNSData(UnsafeMutablePointer<GCExtendedGamepadSnapshotData>?, Data?) -> Bool](gcextendedgamepadsnapshotdatafromnsdata(_:_:).md)
- [func GCMicroGamepadSnapshotDataFromNSData(UnsafeMutablePointer<GCMicroGamepadSnapshotData>?, Data?) -> Bool](gcmicrogamepadsnapshotdatafromnsdata(_:_:).md)
- [func NSDataFromGCExtendedGamepadSnapshotData(UnsafeMutablePointer<GCExtendedGamepadSnapshotData>?) -> Data?](nsdatafromgcextendedgamepadsnapshotdata(_:).md)
- [func NSDataFromGCMicroGamepadSnapshotData(UnsafeMutablePointer<GCMicroGamepadSnapshotData>?) -> Data?](nsdatafromgcmicrogamepadsnapshotdata(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepadsnapshotdataversion)*