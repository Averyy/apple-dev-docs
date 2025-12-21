# DisplayPriority

**Framework**: MapKit JS  
**Kind**: enum

Constant values that provide a hint the map uses to prioritize displaying annotations.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
const DisplayPriority: Readonly<{
    readonly Low: 250;
    readonly High: 750;
    readonly Required: 1000;
}>
```

## Topics

### Display priority values
- [High](displaypriority/high.md)
  A high display priority, with a preset value of 750 out of 1000.
- [Low](displaypriority/low.md)
  A low display priority, with a preset value of 250 out of 1000.
- [Required](displaypriority/required.md)
  The highest display priority, with a preset value of 1000 out of 1000.
### Type Aliases
- [type DisplayPriority](displaypriority/displaypriority.md)
  A type alias that represents the values of display priority enumeration.

## See Also

- [interface AnnotationCalloutDelegate](annotationcalloutdelegate.md)
  Methods for customizing the behavior and appearance of an annotation callout.
- [const CollisionMode](collisionmode.md)
  Constants that indicate whether an annotation collides and how to interpret the collision-frame rectangle of an annotation view.
- [interface Size](size.md)
  A structure that represents a size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/displaypriority)*