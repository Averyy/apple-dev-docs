# isSnapshot

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the object is a snapshot of a racing wheel.

**Availability**:
- Mac Catalyst 16.0+
- macOS 13.0+

## Declaration

```swift
var isSnapshot: Bool { get }
```

```objc
@property (atomic, readonly, getter=isSnapshot) BOOL snapshot;
```

#### Discussion

If [`true`](../../Swift/true.md), the racing wheel is a snapshot at a moment in time of a real device; otherwise, it’s an actual racing wheel.

## See Also

### Creating snapshots
- [func capture() -> GCRacingWheel](./capture%28%29.md)
  Returns a snapshot of the racing wheel with its current element values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcracingwheel/issnapshot)*