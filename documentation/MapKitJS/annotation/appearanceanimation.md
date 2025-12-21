# appearanceAnimation

**Framework**: MapKit JS  
**Kind**: property

A CSS animation that runs when the annotation appears on the map.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
get appearanceAnimation(): string;
set appearanceAnimation(appearanceAnimation: string);
```

#### Discussion

The value of this property is a string specifying a [`CSS animation shorthand property syntax`](https://developer.apple.comhttp://dev.w3.org/csswg/css-animations/#animation). The string refers to keyframes that you need to provide in a stylesheet or a style element.

## See Also

- [coordinate](annotation/coordinate.md)
  The annotation’s coordinate.
- [anchorOffset](annotation/anchoroffset.md)
  An offset that changes the annotation’s default anchor point.
- [displayPriority](annotation/displaypriority-data.property.md)
  A numeric hint that the map uses to prioritize how it displays annotations.
- [padding](annotation/padding.md)
  Spacing to add around the annotation when showing items.
- [size](annotation/size.md)
  The desired dimensions of the annotation, in CSS pixels.
- [visible](annotation/visible.md)
  A Boolean value that determines whether the annotation is visible or hidden.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/annotation/appearanceanimation)*