# boundingBoxOfPath

**Framework**: Core Graphics  
**Kind**: property

Returns the smallest rectangle that contains the current path.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var boundingBoxOfPath: CGRect { get }
```

#### Discussion

The bounding box is the smallest rectangle completely enclosing all points in a path, including control points for Bézier cubic and quadratic curves.

## See Also

- [var currentPointOfPath: CGPoint](cgcontext/currentpointofpath.md)
  Returns the current point in a non-empty path.
- [var isPathEmpty: Bool](cgcontext/ispathempty.md)
  Indicates whether the current path contains any subpaths.
- [func pathContains(CGPoint, mode: CGPathDrawingMode) -> Bool](cgcontext/pathcontains(_:mode:).md)
  Checks to see whether the specified point is contained in the current path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/boundingboxofpath)*