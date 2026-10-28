# showsScale

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Instance Property

A feature visibility setting that determines when the map displays the map’s scale indicator.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
get showsScale(): FeatureVisibility;
set showsScale(showsScale: FeatureVisibility);
```

## Discussion

The scale doesn’t display above a specific zoom threshold (7500 meters per point). MapKit JS handles the placement of the scale automatically as follows:

- When the map shows the zoom control, the map displays the scale indicator in the opposite top corner.
- When the user location control already occupies the opposite corner, the scale indicator shifts horizontally to prevent overlap.
- When the map has no zoom or user location control, the map positions the scale indicator in the leading corner based on the text direction (top-left for LTR and top-right for RTL).

MapKit JS ignores invalid values, but reports them to the console.

## See Also

### Showing the map’s controls
- [showsCompass](./showscompass.md)
  A feature visibility setting that determines when the compass is visible.
- [showsMapTypeControl](./showsmaptypecontrol.md)
  A Boolean value that determines whether to display a control that lets users choose the map type.
- [showsUserLocationControl](./showsuserlocationcontrol.md)
  A Boolean value that determines whether the user location control is visible.
- [showsZoomControl](./showszoomcontrol.md)
  A Boolean value that determines whether to display a control for zooming in and zooming out on a map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/map/showsscale)*