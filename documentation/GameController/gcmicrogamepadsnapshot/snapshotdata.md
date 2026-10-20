# snapshotData

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property

The flattened control input values for the snapshot.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepadsnapshot/snapshotdata)*