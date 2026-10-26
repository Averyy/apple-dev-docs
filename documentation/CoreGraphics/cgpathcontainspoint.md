# CGPathContainsPoint

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Checks whether a point is contained in a graphics path.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern bool CGPathContainsPoint(CGPathRef path, const CGAffineTransform *m, CGPoint point, bool eoFill);
```

#### Return Value

Returns [`true`](../Swift/true.md) if the point is contained in the path; [`false`](../Swift/false.md) otherwise.

#### Discussion

A point is contained in a path if it would be inside the painted region when the path is filled.

## Parameters

- `path`: The path to evaluate the point against.
- `m`: An affine transform. If `m` is not `NULL` then the point is transformed by this affine transform prior to determining whether the path contains the point.
- `point`: The point to check.
- `eoFill`: A Boolean value that, if [`true`](../Swift/true.md), specifies to use the even-odd fill rule to evaluate the painted region of the path. If [`false`](../Swift/false.md), the winding fill rule is used.

## See Also

### Examining a Graphics Path
- [CGPathEqualToPath](./cgpathequaltopath.md)
  Indicates whether two graphics paths are equivalent.
- [var boundingBox: CGRect](./cgpath/boundingbox.md)
  Returns the bounding box containing all points in a graphics path.
- [var boundingBoxOfPath: CGRect](./cgpath/boundingboxofpath.md)
  Returns the bounding box of a graphics path.
- [var currentPoint: CGPoint](./cgpath/currentpoint.md)
  Returns the current point in a graphics path.
- [var isEmpty: Bool](./cgpath/isempty.md)
  Indicates whether or not a graphics path is empty.
- [func isRect(UnsafeMutablePointer<CGRect>?) -> Bool](./cgpath/isrect%28_%29.md)
  Indicates whether or not a graphics path represents a rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpathcontainspoint)*