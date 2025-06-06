# init(controller:snapshotData:)

**Framework**: Game Controller  
**Kind**: init

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(controller: GCController, snapshotData data: Data)
```

#### Return Value

A new snapshot object.

#### Discussion

The data format for a snapshot is private. Your snapshot object should only be created from flattened data previously obtained from a snapshot.

## Parameters

- `controller`: The controller to associate the snapshot with.
- `data`: A data object that contains snapshot data.

## See Also

- [init(snapshotData: Data)](gcmicrogamepadsnapshot/init(snapshotdata:).md)
  Initializes a snapshot object with the flattened data representation obtained from another snapshot.
- [var snapshotData: Data](gcmicrogamepadsnapshot/snapshotdata.md)
  The flattened control input values for the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepadsnapshot/init(controller:snapshotdata:))*