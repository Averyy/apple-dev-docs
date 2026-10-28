# init(controller:snapshotData:)

**Framework**: Game Controller  
**Kind**: init  
**Role**: Initializer

Initializes a snapshot object associated with a specific controller using a flattened data representation obtained from another snapshot.

**Availability**:
- iOS 7.0+ - Deprecated in 13.0
- iPadOS 7.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.9+ - Deprecated in 10.15
- tvOS 9.0+ - Deprecated in 13.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use the [`withExtendedGamepad()`](../gccontroller/withextendedgamepad%28%29.md) method instead.

## Declaration

```swift
init(controller: GCController, snapshotData data: Data)
```

```objc
- (instancetype) initWithController:(GCController *) controller snapshotData:(NSData *) data;
```

## Return Value

A new snapshot object.

## Discussion

The data format for a snapshot is private. Your snapshot object should only be created from flattened data previously obtained from an extended snapshot.

## Parameters

- `controller`: The controller to associate the snapshot with.
- `data`: A data object that contains snapshot data.

## See Also

### Converting Between Extended Snapshots and Data Objects
- [init(snapshotData: Data)](./init%28snapshotdata%29.md)
  Initializes a snapshot object with the flattened data representation obtained from another snapshot.
- [var snapshotData: Data](./snapshotdata.md)
  Flattens a snapshot into an archivable memory representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepadsnapshot/init(controller:snapshotdata:))*