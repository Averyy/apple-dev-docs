# showsUserLocation

**Framework**: Mapkitjs  
**Kind**: property

A Boolean value that determines whether to show the user’s location on the map.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
attribute boolean showsUserLocation;
```

## Mentions

- [Handling map events](handling-map-events.md)

#### Discussion

Set this property to `true` to determine the user’s location and make it visible on the map as a pulsing blue dot annotation.

Set this property to `false` to remove the user location annotation and to stop monitoring the user’s location.

> **Note**:  This property affects the annotation’s visibility, but it doesn’t update the visible region of the map to put the user’s location in the view.

## See Also

- [tracksUserLocation](mapkit.map/tracksuserlocation.md)
  A Boolean value that determines whether to center the map on the user’s location.
- [userLocationAnnotation](mapkit.map/userlocationannotation.md)
  An annotation that indicates the user’s location on the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/MapKitJS/mapkit.map/showsuserlocation)*