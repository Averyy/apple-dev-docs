# visible

**Framework**: MapKit JS  
**Kind**: property

A Boolean value that determines whether the annotation is visible or hidden.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
attribute boolean visible;
```

#### Discussion

Set this property to `false` to temporarily hide an annotation.

If there’s a dense cluster of annotations at low zoom levels, it’s good practice to hide some annotations.

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
- [size](mapkit.annotation/size.md)
  The desired dimensions of the annotation, in CSS pixels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.annotation/visible)*