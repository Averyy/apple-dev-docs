# init(controller:snapshotData:)

**Framework**: Game Controller  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 9.0+ - Deprecated in 13.0
- iPadOS 9.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.11+ - Deprecated in 10.15
- tvOS 9.0+ - Deprecated in 13.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use the [`withMicroGamepad()`](../gccontroller/withmicrogamepad%28%29.md) method instead.

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

The data format for a snapshot is private. Your snapshot object should only be created from flattened data previously obtained from a snapshot.

## Parameters

- `controller`: The controller to associate the snapshot with.
- `data`: A data object that contains snapshot data.

## See Also

### Converting Between Snapshots and Data Objects
- [init(snapshotData: Data)](./init%28snapshotdata%29.md)
  Initializes a snapshot object with the flattened data representation obtained from another snapshot.
- [var snapshotData: Data](./snapshotdata.md)
  The flattened control input values for the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepadsnapshot/init(controller:snapshotdata:))*