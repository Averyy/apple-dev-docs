# init(snapshotData:)

**Framework**: Game Controller  
**Kind**: init

Initializes a snapshot object with the flattened data representation obtained from another snapshot.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(snapshotData data: Data)
```

#### Return Value

A new snapshot object.

#### Discussion

The data format for a snapshot is private. Your snapshot object should only be created from flattened data previously obtained from an extended snapshot.

## Parameters

- `data`: A data object that contains snapshot data.

## See Also

- [init(controller: GCController, snapshotData: Data)](gcextendedgamepadsnapshot/init(controller:snapshotdata:).md)
  Initializes a snapshot object associated with a specific controller using a flattened data representation obtained from another snapshot.
- [var snapshotData: Data](gcextendedgamepadsnapshot/snapshotdata.md)
  Flattens a snapshot into an archivable memory representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepadsnapshot/init(snapshotdata:))*