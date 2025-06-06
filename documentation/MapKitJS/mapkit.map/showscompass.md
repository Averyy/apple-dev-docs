# showsCompass

**Framework**: MapKit JS  
**Kind**: property

A feature visibility setting that determines when the compass is visible.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
attribute string showsCompass;
```

#### Discussion

By default, the compass is adaptive ([`Adaptive`](mapkit.featurevisibility/adaptive.md)), meaning that it isn’t visible when [`rotation`](mapkit.map/rotation.md) is `0` on touch devices. Otherwise, the compass is visible.

## See Also

- [showsMapTypeControl](mapkit.map/showsmaptypecontrol.md)
  A Boolean value that determines whether to display a control that lets users choose the map type.
- [showsScale](mapkit.map/showsscale.md)
  A feature visibility setting that determines when the map displays the map’s scale indicator.
- [showsUserLocationControl](mapkit.map/showsuserlocationcontrol.md)
  A Boolean value that determines whether the user location control is visible.
- [showsZoomControl](mapkit.map/showszoomcontrol.md)
  A Boolean value that determines whether to display a control for zooming in and zooming out on a map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.map/showscompass)*