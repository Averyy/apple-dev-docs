# visible

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the annotation is visible or hidden.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
get visible(): boolean;
set visible(value: boolean);
```

## Discussion

Set this property to `false` to temporarily hide an annotation.

If there’s a dense cluster of annotations at low zoom levels, it’s good practice to hide some annotations.

## See Also

### Getting and setting annotation appearance
- [coordinate](./coordinate.md)
  The annotation’s coordinate.
- [anchorOffset](./anchoroffset.md)
  An offset that changes the annotation’s default anchor point.
- [appearanceAnimation](./appearanceanimation.md)
  A CSS animation that runs when the annotation appears on the map.
- [displayPriority](./displaypriority-data.property.md)
  A numeric hint that the map uses to prioritize how it displays annotations.
- [padding](./padding.md)
  Spacing to add around the annotation when showing items.
- [size](./size.md)
  The desired dimensions of the annotation, in CSS pixels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/annotation/visible)*