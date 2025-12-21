# showsCompass

**Framework**: MapKit JS  
**Kind**: property

A feature visibility setting that determines when the compass is visible.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
get showsCompass(): FeatureVisibility;
set showsCompass(value: FeatureVisibility);
```

#### Discussion

By default, the compass is adaptive ([`Adaptive`](featurevisibility/adaptive.md)), meaning that it isn’t visible when [`rotation`](map/rotation.md) is `0` on touch devices. Otherwise, the compass is visible.

## See Also

- [showsMapTypeControl](map/showsmaptypecontrol.md)
  A Boolean value that determines whether to display a control that lets users choose the map type.
- [showsScale](map/showsscale.md)
  A feature visibility setting that determines when the map displays the map’s scale indicator.
- [showsUserLocationControl](map/showsuserlocationcontrol.md)
  A Boolean value that determines whether the user location control is visible.
- [showsZoomControl](map/showszoomcontrol.md)
  A Boolean value that determines whether to display a control for zooming in and zooming out on a map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/map/showscompass)*