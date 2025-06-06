# currentPoint

**Framework**: Core Graphics  
**Kind**: property

Returns the current point in a graphics path.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var currentPoint: CGPoint { get }
```

#### Discussion

If the path is empty—that is, if it has no elements—this function returns [`CGPointZero`](cgpointzero.md) (see [`CGGeometry`](cggeometry.md)). To determine whether a path is empty, use [`isEmpty`](cgpath/isempty.md).

## See Also

- [var boundingBox: CGRect](cgpath/boundingbox.md)
  Returns the bounding box containing all points in a graphics path.
- [var boundingBoxOfPath: CGRect](cgpath/boundingboxofpath.md)
  Returns the bounding box of a graphics path.
- [func contains(CGPoint, using: CGPathFillRule, transform: CGAffineTransform) -> Bool](cgpath/contains(_:using:transform:).md)
  Returns whether the specified point is interior to the path.
- [var isEmpty: Bool](cgpath/isempty.md)
  Indicates whether or not a graphics path is empty.
- [func isRect(UnsafeMutablePointer<CGRect>?) -> Bool](cgpath/isrect(_:).md)
  Indicates whether or not a graphics path represents a rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpath/currentpoint)*