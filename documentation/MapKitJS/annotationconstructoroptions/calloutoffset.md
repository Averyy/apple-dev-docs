# calloutOffset

**Framework**: MapKit JS  
**Kind**: property

The offset, in CSS pixels, of a callout from the top center of the element.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
calloutOffset?: DOMPoint;
```

#### Discussion

The default value is `DOMPoint(0, 1)`, placing the callout bubble is slightly (1 pixel) above the top-center point of the annotation element.

To choose a different placement, provide an offset point where positive x values move the callout bubble to the left, and positive y values move the callout bubble up. For example, to leave a 5px margin between the top of the annotation and the bottom of the callout, use a callout offset of `DOMPoint(0, 5)`.

## See Also

- [callout](annotationconstructoroptions/callout.md)
  A delegate that enables you to customize the annotation’s callout.
- [calloutEnabled](annotationconstructoroptions/calloutenabled.md)
  A Boolean value that determines whether the map shows a callout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/annotationconstructoroptions/calloutoffset)*