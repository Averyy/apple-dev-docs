# snapshotData

**Framework**: Game Controller  
**Kind**: property

The flattened control input values for the snapshot.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var snapshotData: Data { get set }
```

#### Discussion

You can assign another [`NSData`](https://developer.apple.com/documentation/Foundation/NSData) object containing snapshot data to this property. The elements of the snapshot are updated to the values stored in the flattened data. This triggers any value handlers attached to those elements.

## See Also

- [init(snapshotData: Data)](gcmicrogamepadsnapshot/init(snapshotdata:).md)
  Initializes a snapshot object with the flattened data representation obtained from another snapshot.
- [init(controller: GCController, snapshotData: Data)](gcmicrogamepadsnapshot/init(controller:snapshotdata:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepadsnapshot/snapshotdata)*