# padding

**Framework**: MapKit JS  
**Kind**: property

Spacing to add around the annotation when showing items.

**Availability**:
- MapKit JS 5.16+

## Declaration

```swift
get padding(): Padding;
set padding(value: Padding);
```

#### Discussion

Padding prevents any items from touching the edges of the map. Set `padding` to a [`Padding`](padding.md) object (the default is no padding on all sides).

## See Also

- [coordinate](annotation/coordinate.md)
  The annotation’s coordinate.
- [anchorOffset](annotation/anchoroffset.md)
  An offset that changes the annotation’s default anchor point.
- [appearanceAnimation](annotation/appearanceanimation.md)
  A CSS animation that runs when the annotation appears on the map.
- [displayPriority](annotation/displaypriority-data.property.md)
  A numeric hint that the map uses to prioritize how it displays annotations.
- [size](annotation/size.md)
  The desired dimensions of the annotation, in CSS pixels.
- [visible](annotation/visible.md)
  A Boolean value that determines whether the annotation is visible or hidden.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/annotation/padding)*