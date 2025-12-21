# displayPriority

**Framework**: MapKit JS  
**Kind**: property

A numeric hint that the map uses to prioritize how it displays annotations.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
get displayPriority(): number;
set displayPriority(value: number);
```

## Mentions

- [MapKit JS 5](mapkit-js-5.md)

#### Discussion

Maps use the display priority as a hint to determine whether to display annotations at any given time. By default, the display priority is [`Required`](displaypriority/required.md), which indicates the annotation always displays on the map.

Display priority can be any number from `0` to `1000`. There are three preset values:

- [`Low`](displaypriority/low.md) (`250`)
- [`High`](displaypriority/high.md) (`750`)
- [`Required`](displaypriority/required.md) (`1000`)

Maps ignores this value when [`collisionMode`](annotation/collisionmode-data.property.md) is `None`.

## See Also

- [coordinate](annotation/coordinate.md)
  The annotation’s coordinate.
- [anchorOffset](annotation/anchoroffset.md)
  An offset that changes the annotation’s default anchor point.
- [appearanceAnimation](annotation/appearanceanimation.md)
  A CSS animation that runs when the annotation appears on the map.
- [padding](annotation/padding.md)
  Spacing to add around the annotation when showing items.
- [size](annotation/size.md)
  The desired dimensions of the annotation, in CSS pixels.
- [visible](annotation/visible.md)
  A Boolean value that determines whether the annotation is visible or hidden.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/annotation/displaypriority-data.property)*