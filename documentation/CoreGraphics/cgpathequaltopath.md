# CGPathEqualToPath

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Indicates whether two graphics paths are equivalent.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern bool CGPathEqualToPath(CGPathRef path1, CGPathRef path2);
```

#### Return Value

A Boolean value that indicates whether or not the two specified paths contain the same sequence of path elements. If the paths are not the same, returns [`false`](../Swift/false.md).

## Parameters

- `path1`: The first path being compared.
- `path2`: The second path being compared.

## See Also

### Examining a Graphics Path
- [var boundingBox: CGRect](./cgpath/boundingbox.md)
  Returns the bounding box containing all points in a graphics path.
- [var boundingBoxOfPath: CGRect](./cgpath/boundingboxofpath.md)
  Returns the bounding box of a graphics path.
- [var currentPoint: CGPoint](./cgpath/currentpoint.md)
  Returns the current point in a graphics path.
- [CGPathContainsPoint](./cgpathcontainspoint.md)
  Checks whether a point is contained in a graphics path.
- [var isEmpty: Bool](./cgpath/isempty.md)
  Indicates whether or not a graphics path is empty.
- [func isRect(UnsafeMutablePointer<CGRect>?) -> Bool](./cgpath/isrect%28_%29.md)
  Indicates whether or not a graphics path represents a rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpathequaltopath)*