# isEmpty

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the path is empty.

**Availability**:
- macOS

## Declaration

```swift
var isEmpty: Bool { get }
```

```objc
@property (readonly, getter=isEmpty) BOOL empty;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) if the path contains no elements, or [`false`](../../Swift/false.md) if it contains at least one element.

## See Also

### Querying a Path
- [var bounds: NSRect](./bounds.md)
  The bounding box of the path.
- [var controlPointBounds: NSRect](./controlpointbounds.md)
  The bounding box of the path, including any control points.
- [var currentPoint: NSPoint](./currentpoint.md)
  The current point (the trailing point or ending point in the most recently added segment).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/isempty)*