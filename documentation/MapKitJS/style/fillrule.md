# fillRule

**Framework**: MapKit JS  
**Kind**: property

A rule for determining whether a point is inside or outside a polygon.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
get fillRule(): CanvasFillRule;
set fillRule(fillRule: CanvasFillRule);
```

#### Discussion

This can be either the nonzero winding rule (`nonzero`), or the even-odd rule (`evenodd`). The default fill rule is `nonzero`.

## See Also

- [fillColor](style/fillcolor.md)
  The fill color of a shape.
- [fillOpacity](style/fillopacity.md)
  The opacity of the fill color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/style/fillrule)*