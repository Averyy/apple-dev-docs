# isEmpty

**Framework**: Core Graphics  
**Kind**: property  
**Role**: Instance Property

Indicates whether or not a graphics path is empty.

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
var isEmpty: Bool { get }
```

```c
extern bool CGPathIsEmpty(CGPathRef path);
```

#### Discussion

An empty path contains no elements.

## See Also

### Examining a Graphics Path
- [var boundingBox: CGRect](./boundingbox.md)
  Returns the bounding box containing all points in a graphics path.
- [var boundingBoxOfPath: CGRect](./boundingboxofpath.md)
  Returns the bounding box of a graphics path.
- [var currentPoint: CGPoint](./currentpoint.md)
  Returns the current point in a graphics path.
- [func contains(CGPoint, using: CGPathFillRule, transform: CGAffineTransform) -> Bool](./contains%28_,using,transform%29.md)
  Returns whether the specified point is interior to the path.
- [func isRect(UnsafeMutablePointer<CGRect>?) -> Bool](./isrect%28_%29.md)
  Indicates whether or not a graphics path represents a rectangle.
- [CGPathEqualToPath](../cgpathequaltopath.md)
  Indicates whether two graphics paths are equivalent.
- [CGPathContainsPoint](../cgpathcontainspoint.md)
  Checks whether a point is contained in a graphics path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpath/isempty)*