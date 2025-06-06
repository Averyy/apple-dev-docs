# calloutOffset

**Framework**: MapKit JS  
**Kind**: property

An offset that changes the annotation callout’s default placement.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
attribute DOMPoint calloutOffset;
```

#### Discussion

By default, MapKit JS places the callout bubble slightly (1 pixel) above the top-center point of the annotation element.

To choose a different placement, provide an offset point where positive x-values move the callout bubble to the left, and positive y-values move the callout bubble up. For example, to leave a 5-pixel margin between the top of the annotation and the bottom of the callout, use a callout offset of `DOMPoint(0, 5)`.

## See Also

- [callout](mapkit.annotation/callout.md)
  A delegate that enables you to customize the annotation’s callout.
- [calloutEnabled](mapkit.annotation/calloutenabled.md)
  A Boolean value that determines whether the map shows an annotation’s callout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.annotation/calloutoffset)*