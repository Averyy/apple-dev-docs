# size

**Framework**: MapKit JS  
**Kind**: property

The desired dimensions of the annotation, in CSS pixels.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
attribute Object size;
```

#### Discussion

If supplied, indicates the desired size of the annotation in CSS pixels. The value must be an object with `width` and `height` number properties:

```javascript
{
    size: { width: 32, height: 39 }
}
```

## See Also

- [coordinate](mapkit.annotation/coordinate.md)
  The annotation’s coordinate.
- [anchorOffset](mapkit.annotation/anchoroffset.md)
  An offset that changes the annotation’s default anchor point.
- [appearanceAnimation](mapkit.annotation/appearanceanimation.md)
  A CSS animation that runs when the annotation appears on the map.
- [displayPriority](mapkit.annotation/displaypriority.md)
  A numeric hint that the map uses to prioritize how it displays annotations.
- [mapkit.Annotation.DisplayPriority](mapkit.annotation.displaypriority.md)
  Constant values that provide a hint the map uses to prioritize displaying annotations.
- [padding](mapkit.annotation/padding.md)
  Spacing to add around the annotation when showing items.
- [visible](mapkit.annotation/visible.md)
  A Boolean value that determines whether the annotation is visible or hidden.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.annotation/size)*