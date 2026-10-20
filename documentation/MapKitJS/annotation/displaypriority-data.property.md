# displayPriority

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Instance Property

A numeric hint that the map uses to prioritize how it displays annotations.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
get displayPriority(): number;
set displayPriority(value: number);
```

## Mentions

- [MapKit JS 5](../mapkit-js-5.md)

#### Discussion

Maps use the display priority as a hint to determine whether to display annotations at any given time. By default, the display priority is [`Required`](../annotationdisplaypriority/required.md), which indicates the annotation always displays on the map.

Display priority can be any number from `0` to `1000`. There are three preset values:

- [`Low`](../annotationdisplaypriority/low.md) (`250`)
- [`High`](../annotationdisplaypriority/high.md) (`750`)
- [`Required`](../annotationdisplaypriority/required.md) (`1000`)

Maps ignores this value when [`collisionMode`](./collisionmode-data.property.md) is `None`.

## See Also

### Getting and setting annotation appearance
- [coordinate](./coordinate.md)
  The annotation’s coordinate.
- [anchorOffset](./anchoroffset.md)
  An offset that changes the annotation’s default anchor point.
- [appearanceAnimation](./appearanceanimation.md)
  A CSS animation that runs when the annotation appears on the map.
- [padding](./padding.md)
  Spacing to add around the annotation when showing items.
- [size](./size.md)
  The desired dimensions of the annotation, in CSS pixels.
- [visible](./visible.md)
  A Boolean value that determines whether the annotation is visible or hidden.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/annotation/displaypriority-data.property)*