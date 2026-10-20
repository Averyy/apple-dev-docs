# showsCompass

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Instance Property

A feature visibility setting that determines when the compass is visible.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
get showsCompass(): FeatureVisibility;
set showsCompass(value: FeatureVisibility);
```

#### Discussion

By default, the compass is adaptive ([`Adaptive`](../featurevisibility/adaptive.md)), meaning that it isn’t visible when [`rotation`](./rotation.md) is `0` on touch devices. Otherwise, the compass is visible.

## See Also

### Showing the map’s controls
- [showsMapTypeControl](./showsmaptypecontrol.md)
  A Boolean value that determines whether to display a control that lets users choose the map type.
- [showsScale](./showsscale.md)
  A feature visibility setting that determines when the map displays the map’s scale indicator.
- [showsUserLocationControl](./showsuserlocationcontrol.md)
  A Boolean value that determines whether the user location control is visible.
- [showsZoomControl](./showszoomcontrol.md)
  A Boolean value that determines whether to display a control for zooming in and zooming out on a map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/map/showscompass)*