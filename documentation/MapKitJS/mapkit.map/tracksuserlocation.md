# tracksUserLocation

**Framework**: MapKit JS  
**Kind**: property

A Boolean value that determines whether to center the map on the user’s location.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
attribute boolean tracksUserLocation;
```

#### Discussion

Set this property to `true` to center the map on the user location annotation. Enabling this property automatically enables [`showsUserLocation`](mapkit.map/showsuserlocation.md).

Set this property to `false` to stop centering the map on the current location.

A programmatic or user-initiated change to the map’s region that moves the user location annotation off the center automatically disables [`tracksUserLocation`](mapkit.map/tracksuserlocation.md).

## See Also

- [showsUserLocation](mapkit.map/showsuserlocation.md)
  A Boolean value that determines whether to show the user’s location on the map.
- [userLocationAnnotation](mapkit.map/userlocationannotation.md)
  An annotation that indicates the user’s location on the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.map/tracksuserlocation)*