# isPathEmpty

**Framework**: Core Graphics  
**Kind**: property  
**Role**: Instance Property

Indicates whether the current path contains any subpaths.

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
var isPathEmpty: Bool { get }
```

```c
extern bool CGContextIsPathEmpty(CGContextRef c);
```

## See Also

### Examining the Current Graphics Path
- [var boundingBoxOfPath: CGRect](./boundingboxofpath.md)
  Returns the smallest rectangle that contains the current path.
- [var currentPointOfPath: CGPoint](./currentpointofpath.md)
  Returns the current point in a non-empty path.
- [func pathContains(CGPoint, mode: CGPathDrawingMode) -> Bool](./pathcontains%28_,mode%29.md)
  Checks to see whether the specified point is contained in the current path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/ispathempty)*