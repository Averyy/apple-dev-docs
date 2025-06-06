# isSnapshot

**Framework**: Game Controller  
**Kind**: property

A Boolean value that indicates whether the object is a snapshot of a racing wheel.

**Availability**:
- Mac Catalyst 16.0+
- macOS 13.0+

## Declaration

```swift
var isSnapshot: Bool { get }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/swift/true), the racing wheel is a snapshot at a moment in time of a real device; otherwise, it’s an actual racing wheel.

## See Also

- [func capture() -> GCRacingWheel](gcracingwheel/capture.md)
  Returns a snapshot of the racing wheel with its current element values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcracingwheel/issnapshot)*