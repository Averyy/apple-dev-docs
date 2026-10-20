# CGPathElementType.addQuadCurveToPoint

**Framework**: Core Graphics  
**Kind**: case  
**Role**: Case

The path element that adds a quadratic curve from the current point to the specified point.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
case addQuadCurveToPoint
```

```c
kCGPathElementAddQuadCurveToPoint
```

#### Discussion

The element holds a control point and a destination point. See the function [`CGPathAddQuadCurveToPoint`](../cgpathaddquadcurvetopoint.md).

## See Also

### Constants
- [CGPathElementType.moveToPoint](./movetopoint.md)
  The path element that starts a new subpath.
- [CGPathElementType.addLineToPoint](./addlinetopoint.md)
  The path element that adds a line from the current point to a new point.
- [CGPathElementType.addCurveToPoint](./addcurvetopoint.md)
  The path element that adds a cubic curve from the current point to the specified point.
- [CGPathElementType.closeSubpath](./closesubpath.md)
  The path element that closes and completes a subpath. The element does not contain any points. See the function [`closeSubpath()`](../cgmutablepath/closesubpath%28%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpathelementtype/addquadcurvetopoint)*