# init(snapshotData:)

**Framework**: Game Controller  
**Kind**: init  
**Role**: Initializer

Initializes a snapshot object with the flattened data representation obtained from another snapshot.

**Availability**:
- iOS 7.0+ - Deprecated in 13.0
- iPadOS 7.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.9+ - Deprecated in 10.15
- tvOS 9.0+ - Deprecated in 13.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`GCExtendedGamepad`](../gcextendedgamepad.md) instead.

## Declaration

```swift
init(snapshotData data: Data)
```

```objc
- (instancetype) initWithSnapshotData:(NSData *) data;
```

## Return Value

A new snapshot object.

## Discussion

The data format for a snapshot is private. Your snapshot object should only be created from flattened data previously obtained from a snapshot.

## Parameters

- `data`: A data object that contains snapshot data.

## See Also

### Converting Between Snapshots and Data Objects
- [init(controller: GCController, snapshotData: Data)](./init%28controller,snapshotdata%29.md)
  Initializes a snapshot object associated with a specific controller using a flattened data representation obtained from another snapshot.
- [var snapshotData: Data](./snapshotdata.md)
  The flattened control input values for the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcgamepadsnapshot/init(snapshotdata:))*