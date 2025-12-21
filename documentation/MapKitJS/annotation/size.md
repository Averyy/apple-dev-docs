# size

**Framework**: MapKit JS  
**Kind**: property

The desired dimensions of the annotation, in CSS pixels.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
get size(): Size | undefined;
set size(value: Size);
```

#### Discussion

If supplied, indicates the desired size of the annotation in CSS pixels. The value must be an object with `width` and `height` number properties:

```javascript
{
    size: { width: 32, height: 39 }
}
```

## See Also

- [coordinate](annotation/coordinate.md)
  The annotation’s coordinate.
- [anchorOffset](annotation/anchoroffset.md)
  An offset that changes the annotation’s default anchor point.
- [appearanceAnimation](annotation/appearanceanimation.md)
  A CSS animation that runs when the annotation appears on the map.
- [displayPriority](annotation/displaypriority-data.property.md)
  A numeric hint that the map uses to prioritize how it displays annotations.
- [padding](annotation/padding.md)
  Spacing to add around the annotation when showing items.
- [visible](annotation/visible.md)
  A Boolean value that determines whether the annotation is visible or hidden.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/annotation/size)*