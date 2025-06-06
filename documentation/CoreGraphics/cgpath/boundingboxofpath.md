# boundingBoxOfPath

**Framework**: Core Graphics  
**Kind**: property

Returns the bounding box of a graphics path.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var boundingBoxOfPath: CGRect { get }
```

#### Discussion

The path bounding box is the smallest rectangle completely enclosing all points in the path but not including control points for Bézier and quadratic curves. If the path is empty, this value is [`CGRectNull`](cgrectnull.md).

## See Also

- [var boundingBox: CGRect](cgpath/boundingbox.md)
  Returns the bounding box containing all points in a graphics path.
- [var currentPoint: CGPoint](cgpath/currentpoint.md)
  Returns the current point in a graphics path.
- [func contains(CGPoint, using: CGPathFillRule, transform: CGAffineTransform) -> Bool](cgpath/contains(_:using:transform:).md)
  Returns whether the specified point is interior to the path.
- [var isEmpty: Bool](cgpath/isempty.md)
  Indicates whether or not a graphics path is empty.
- [func isRect(UnsafeMutablePointer<CGRect>?) -> Bool](cgpath/isrect(_:).md)
  Indicates whether or not a graphics path represents a rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpath/boundingboxofpath)*