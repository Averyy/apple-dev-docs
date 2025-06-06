# colorScheme

**Framework**: MapKit JS  
**Kind**: property

The map’s color scheme when displaying standard or muted standard map types.

**Availability**:
- MapKit JS 5.12+

## Declaration

```swift
attribute string colorScheme;
```

#### Discussion

This property accepts a property from [`mapkit.Map.ColorSchemes`](mapkit.map.colorschemes.md) to determine whether the map displays with a dark or light theme when [`Standard`](mapkit.map.maptypes/standard.md) or [`MutedStandard`](mapkit.map.maptypes/mutedstandard.md) are the configured [`mapType`](mapkit.map/maptype.md). The default is [`Light`](mapkit.map.colorschemes/light.md).

The grid, user location accuracy ring, labels for marker annotations, and controls of the map change appearance to complement the Dark Mode style.

## See Also

- [mapType](mapconstructoroptions/maptype.md)
  The type of data that the map view displays.
- [padding](mapconstructoroptions/padding.md)
  The map’s inset margins.
- [showsMapTypeControl](mapconstructoroptions/showsmaptypecontrol.md)
  A Boolean value that determines whether to display a control that lets users choose the map type.
- [isRotationEnabled](mapconstructoroptions/isrotationenabled.md)
  A Boolean value that determines whether the user may rotate the map using the compass control or a rotate gesture.
- [showsCompass](mapconstructoroptions/showscompass.md)
  A feature visibility setting that determines when the compass is visible.
- [isZoomEnabled](mapconstructoroptions/iszoomenabled.md)
  A Boolean value that determines whether the user may zoom in and out on the map using pinch gestures or the zoom control.
- [showsZoomControl](mapconstructoroptions/showszoomcontrol.md)
  A Boolean value that determines whether to display a control for zooming in and zooming out on a map.
- [isScrollEnabled](mapconstructoroptions/isscrollenabled.md)
  A Boolean value that determines whether the user may scroll the map with a pointing device or gestures on a touchscreen.
- [showsScale](mapconstructoroptions/showsscale.md)
  A feature visibility setting that allows you to determine when to display the map’s scale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapconstructoroptions/colorscheme)*