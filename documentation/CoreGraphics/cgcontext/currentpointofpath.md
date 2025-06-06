# currentPointOfPath

**Framework**: Core Graphics  
**Kind**: property

Returns the current point in a non-empty path.

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
var currentPointOfPath: CGPoint { get }
```

## See Also

- [var boundingBoxOfPath: CGRect](cgcontext/boundingboxofpath.md)
  Returns the smallest rectangle that contains the current path.
- [var isPathEmpty: Bool](cgcontext/ispathempty.md)
  Indicates whether the current path contains any subpaths.
- [func pathContains(CGPoint, mode: CGPathDrawingMode) -> Bool](cgcontext/pathcontains(_:mode:).md)
  Checks to see whether the specified point is contained in the current path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/currentpointofpath)*