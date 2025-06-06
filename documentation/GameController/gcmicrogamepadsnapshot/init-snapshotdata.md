# init(snapshotData:)

**Framework**: Game Controller  
**Kind**: init

Initializes a snapshot object with the flattened data representation obtained from another snapshot.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(snapshotData data: Data)
```

#### Return Value

A new snapshot object.

#### Discussion

The data format for a snapshot is private. Your snapshot object should only be created from flattened data previously obtained from a snapshot.

## Parameters

- `data`: A data object that contains snapshot data.

## See Also

- [init(controller: GCController, snapshotData: Data)](gcmicrogamepadsnapshot/init(controller:snapshotdata:).md)
- [var snapshotData: Data](gcmicrogamepadsnapshot/snapshotdata.md)
  The flattened control input values for the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepadsnapshot/init(snapshotdata:))*