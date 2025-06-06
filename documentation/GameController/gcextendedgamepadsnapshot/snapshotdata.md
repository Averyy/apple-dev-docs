# snapshotData

**Framework**: Game Controller  
**Kind**: property

Flattens a snapshot into an archivable memory representation.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var snapshotData: Data { get set }
```

#### Discussion

You can assign another [`NSData`](https://developer.apple.com/documentation/Foundation/NSData) object containing extended snapshot data to this property. The elements of the extended snapshot are updated to the values stored in the flattened data. This triggers any value handlers attached to those elements.

## See Also

- [init(snapshotData: Data)](gcextendedgamepadsnapshot/init(snapshotdata:).md)
  Initializes a snapshot object with the flattened data representation obtained from another snapshot.
- [init(controller: GCController, snapshotData: Data)](gcextendedgamepadsnapshot/init(controller:snapshotdata:).md)
  Initializes a snapshot object associated with a specific controller using a flattened data representation obtained from another snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepadsnapshot/snapshotdata)*