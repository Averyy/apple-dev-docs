# CollisionMode

**Framework**: MapKit JS  
**Kind**: enum

Constants that indicate whether an annotation collides and how to interpret the collision-frame rectangle of an annotation view.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
const CollisionMode: Readonly<{
    readonly Rectangle: "rectangle";
    readonly Circle: "circle";
    readonly None: "none";
}>
```

## Topics

### Collision modes
- [Rectangle](collisionmode/rectangle.md)
  A constant indicating that the map should use a full collision rectangle for detecting collisions.
- [Circle](collisionmode/circle.md)
  A constant indicating that the map should use a circle inscribed in the collision frame rectangle to determine collisions.
- [None](collisionmode/none.md)
  A constant that indicates the annotation doesn’t collide with other annotations.
### Type Aliases
- [type CollisionMode](collisionmode/collisionmode.md)
  A type alias that represents the values of the collision mode enumeration.

## See Also

- [interface AnnotationCalloutDelegate](annotationcalloutdelegate.md)
  Methods for customizing the behavior and appearance of an annotation callout.
- [const DisplayPriority](displaypriority.md)
  Constant values that provide a hint the map uses to prioritize displaying annotations.
- [interface Size](size.md)
  A structure that represents a size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/collisionmode)*