# pathContains(_:mode:)

**Framework**: Core Graphics  
**Kind**: method

Checks to see whether the specified point is contained in the current path.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func pathContains(_ point: CGPoint, mode: CGPathDrawingMode) -> Bool
```

#### Return Value

Returns `true` if `point` is inside the current path of the graphics context; `false` otherwise.

#### Discussion

A point is contained within the path of a graphics context if the point is inside the painted region when the path is stroked or filled with opaque colors using the specified path drawing mode. A point can be inside a path only if the path is explicitly closed by calling the function [`closePath()`](cgcontext/closepath().md) for paths drawn directly to the current context, or [`closeSubpath()`](cgmutablepath/closesubpath().md) for paths first created as [`CGPath`](cgpath.md) objects and then drawn to the current context.

## Parameters

- `point`: The point to check, specified in user space units.
- `mode`: A path drawing mode. See  .

## See Also

- [var boundingBoxOfPath: CGRect](cgcontext/boundingboxofpath.md)
  Returns the smallest rectangle that contains the current path.
- [var currentPointOfPath: CGPoint](cgcontext/currentpointofpath.md)
  Returns the current point in a non-empty path.
- [var isPathEmpty: Bool](cgcontext/ispathempty.md)
  Indicates whether the current path contains any subpaths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/pathcontains(_:mode:))*