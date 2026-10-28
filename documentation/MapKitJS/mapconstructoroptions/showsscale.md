# showsScale

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Interface Property

A feature visibility setting that allows you to determine when to display the map’s scale.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
showsScale?: FeatureVisibility;
```

## Discussion

The default value is `mapkit.FeatureVisibility.Hidden`. See [`FeatureVisibility`](../featurevisibility.md) for other values that determine when the map shows the scale. See MapKit’s [`showsScale`](../map/showsscale.md) for more information about how the values determine when to show the scale.

## See Also

### Setting the map’s appearance and controls
- [colorScheme](./colorscheme.md)
  The map’s color scheme when displaying standard or muted standard map types.
- [mapType](./maptype.md)
  The type of data that the map view displays.
- [padding](./padding.md)
  The map’s inset margins.
- [showsMapTypeControl](./showsmaptypecontrol.md)
  A Boolean value that determines whether to display a control that lets users choose the map type.
- [isRotationEnabled](./isrotationenabled.md)
  A Boolean value that determines whether the user may rotate the map using the compass control or a rotate gesture.
- [showsCompass](./showscompass.md)
  A feature visibility setting that determines when the compass is visible.
- [isZoomEnabled](./iszoomenabled.md)
  A Boolean value that determines whether the user may zoom in and out on the map using pinch gestures or the zoom control.
- [showsZoomControl](./showszoomcontrol.md)
  A Boolean value that determines whether to display a control for zooming in and zooming out on a map.
- [isScrollEnabled](./isscrollenabled.md)
  A Boolean value that determines whether the user may scroll the map with a pointing device or gestures on a touchscreen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapconstructoroptions/showsscale)*