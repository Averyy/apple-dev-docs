# userLocationAnnotation

**Framework**: MapKit JS  
**Kind**: property

An annotation that indicates the user’s location on the map.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
get userLocationAnnotation(): UserLocationAnnotation | null;
```

#### Discussion

This is the annotation, or blue dot, that indicates the user’s location on the map. This property is `null` if:

- [`showsUserLocation`](map/showsuserlocation.md) is `false`.
- MapKit JS is trying to acquire the user’s location.
- MapKit JS fails to acquire the user’s location.

The map’s [`annotations`](map/annotations.md) property only holds annotations you can modify. MapKit JS doesn’t add the [`userLocationAnnotation`](map/userlocationannotation.md) property to the annotations array, and you can’t remove it by using [`removeAnnotation(annotation)`](map/removeannotation.md). Use [`selectedAnnotation`](map/selectedannotation.md) to reference the user’s location annotation when it’s in a selected state.

The default value of the [`collisionMode`](annotation/collisionmode-data.property.md) property on the user’s location annotation is [`None`](collisionmode/none.md). The user’s location annotation doesn’t collide with other annotations unless you set the collision mode property to a value other than `None`.

## See Also

- [showsUserLocation](map/showsuserlocation.md)
  A Boolean value that determines whether to show the user’s location on the map.
- [tracksUserLocation](map/tracksuserlocation.md)
  A Boolean value that determines whether to center the map on the user’s location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/map/userlocationannotation)*