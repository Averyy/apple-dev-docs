# fillPath(using:)

**Framework**: Core Graphics  
**Kind**: method

Paints the area within the current path, as determined by the specified fill rule.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst ?+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func fillPath(using rule: CGPathFillRule = .winding)
```

#### Discussion

If the current path contains any non-closed subpaths, this method treats each subpath as if it had been closed with the [`closePath()`](cgcontext/closepath().md) method, then applies the specified rule to determine which areas to fill.

After filling the path, this method clears the context’s current path.

## Parameters

- `rule`: This parameter defaults to the   rule if unspecified.

## See Also

- [func drawPath(using: CGPathDrawingMode)](cgcontext/drawpath(using:).md)
  Draws the current path using the provided drawing mode.
- [enum CGPathDrawingMode](cgpathdrawingmode.md)
  Options for rendering a path.
- [func strokePath()](cgcontext/strokepath.md)
  Paints a line along the current path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/fillpath(using:))*