# currentPoint

**Framework**: Core Graphics  
**Kind**: property  
**Role**: Instance Property

Returns the current point in a graphics path.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var currentPoint: CGPoint { get }
```

```c
extern CGPoint CGPathGetCurrentPoint(CGPathRef path);
```

#### Discussion

If the path is empty—that is, if it has no elements—this function returns [`CGPointZero`](../cgpointzero.md) (see [CGGeometry](../cggeometry.md)). To determine whether a path is empty, use [`isEmpty`](./isempty.md).

## See Also

### Examining a Graphics Path
- [var boundingBox: CGRect](./boundingbox.md)
  Returns the bounding box containing all points in a graphics path.
- [var boundingBoxOfPath: CGRect](./boundingboxofpath.md)
  Returns the bounding box of a graphics path.
- [func contains(CGPoint, using: CGPathFillRule, transform: CGAffineTransform) -> Bool](./contains%28_,using,transform%29.md)
  Returns whether the specified point is interior to the path.
- [var isEmpty: Bool](./isempty.md)
  Indicates whether or not a graphics path is empty.
- [func isRect(UnsafeMutablePointer<CGRect>?) -> Bool](./isrect%28_%29.md)
  Indicates whether or not a graphics path represents a rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpath/currentpoint)*