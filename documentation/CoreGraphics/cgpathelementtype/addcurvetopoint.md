# CGPathElementType.addCurveToPoint

**Framework**: Core Graphics  
**Kind**: case

The path element that adds a cubic curve from the current point to the specified point.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
case addCurveToPoint
```

#### Discussion

The element holds two control points and a destination point. See the function [`CGPathAddCurveToPoint`](cgpathaddcurvetopoint.md).

## See Also

- [CGPathElementType.moveToPoint](cgpathelementtype/movetopoint.md)
  The path element that starts a new subpath.
- [CGPathElementType.addLineToPoint](cgpathelementtype/addlinetopoint.md)
  The path element that adds a line from the current point to a new point.
- [CGPathElementType.addQuadCurveToPoint](cgpathelementtype/addquadcurvetopoint.md)
  The path element that adds a quadratic curve from the current point to the specified point.
- [CGPathElementType.closeSubpath](cgpathelementtype/closesubpath.md)
  The path element that closes and completes a subpath. The element does not contain any points. See the function [`closeSubpath()`](cgmutablepath/closesubpath().md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpathelementtype/addcurvetopoint)*