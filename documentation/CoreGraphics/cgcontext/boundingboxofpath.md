# boundingBoxOfPath

**Framework**: Core Graphics  
**Kind**: property  
**Role**: Instance Property

Returns the smallest rectangle that contains the current path.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var boundingBoxOfPath: CGRect { get }
```

```c
extern CGRect CGContextGetPathBoundingBox(CGContextRef c);
```

## Discussion

The bounding box is the smallest rectangle completely enclosing all points in a path, including control points for Bézier cubic and quadratic curves.

## See Also

### Examining the Current Graphics Path
- [var currentPointOfPath: CGPoint](./currentpointofpath.md)
  Returns the current point in a non-empty path.
- [var isPathEmpty: Bool](./ispathempty.md)
  Indicates whether the current path contains any subpaths.
- [func pathContains(CGPoint, mode: CGPathDrawingMode) -> Bool](./pathcontains%28_,mode%29.md)
  Checks to see whether the specified point is contained in the current path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/boundingboxofpath)*