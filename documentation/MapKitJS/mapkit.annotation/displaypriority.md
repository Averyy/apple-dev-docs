# displayPriority

**Framework**: MapKit JS  
**Kind**: property

A numeric hint that the map uses to prioritize how it displays annotations.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
attribute number displayPriority;
```

## Mentions

- [MapKit JS 5](mapkit-js-5.md)

#### Discussion

Maps use the display priority as a hint to determine whether to display annotations at any given time. By default, the display priority is [`Required`](mapkit.annotation.displaypriority/required.md), which indicates the annotation always displays on the map.

Display priority can be any number from `0` to `1000`. There are three preset values:

- [`Low`](mapkit.annotation.displaypriority/low.md) (`250`)
- [`High`](mapkit.annotation.displaypriority/high.md) (`750`)
- [`Required`](mapkit.annotation.displaypriority/required.md) (`1000`)

Maps ignore this value when [`collisionMode`](mapkit.annotation/collisionmode.md) is `None`.

## See Also

- [coordinate](mapkit.annotation/coordinate.md)
  The annotation’s coordinate.
- [anchorOffset](mapkit.annotation/anchoroffset.md)
  An offset that changes the annotation’s default anchor point.
- [appearanceAnimation](mapkit.annotation/appearanceanimation.md)
  A CSS animation that runs when the annotation appears on the map.
- [mapkit.Annotation.DisplayPriority](mapkit.annotation.displaypriority.md)
  Constant values that provide a hint the map uses to prioritize displaying annotations.
- [padding](mapkit.annotation/padding.md)
  Spacing to add around the annotation when showing items.
- [size](mapkit.annotation/size.md)
  The desired dimensions of the annotation, in CSS pixels.
- [visible](mapkit.annotation/visible.md)
  A Boolean value that determines whether the annotation is visible or hidden.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.annotation/displaypriority)*