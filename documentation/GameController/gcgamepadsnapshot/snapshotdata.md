# snapshotData

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property

The flattened control input values for the snapshot.

**Availability**:
- iOS 7.0+ - Deprecated in 13.0
- iPadOS 7.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.9+ - Deprecated in 10.15
- tvOS 9.0+ - Deprecated in 13.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use the [`GCExtendedGamepad`](../gcextendedgamepad.md) class instead.

## Declaration

```swift
var snapshotData: Data { get set }
```

```objc
@property (atomic, copy) NSData * snapshotData;
```

#### Discussion

You can assign another [`NSData`](../../Foundation/nsdata.md) object containing snapshot data to this property. The elements of the snapshot are updated to the values stored in the flattened data. This triggers any value handlers attached to those elements.

## See Also

### Converting Between Snapshots and Data Objects
- [init(snapshotData: Data)](./init%28snapshotdata%29.md)
  Initializes a snapshot object with the flattened data representation obtained from another snapshot.
- [init(controller: GCController, snapshotData: Data)](./init%28controller,snapshotdata%29.md)
  Initializes a snapshot object associated with a specific controller using a flattened data representation obtained from another snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcgamepadsnapshot/snapshotdata)*