# isEmpty

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the path is empty.

**Availability**:
- macOS ?+

## Declaration

```swift
var isEmpty: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) if the path contains no elements, or [`false`](https://developer.apple.com/documentation/swift/false) if it contains at least one element.

## See Also

- [var bounds: NSRect](nsbezierpath/bounds.md)
  The bounding box of the path.
- [var controlPointBounds: NSRect](nsbezierpath/controlpointbounds.md)
  The bounding box of the path, including any control points.
- [var currentPoint: NSPoint](nsbezierpath/currentpoint.md)
  The current point (the trailing point or ending point in the most recently added segment).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/isempty)*