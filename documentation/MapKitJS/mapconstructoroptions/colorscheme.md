# colorScheme

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Interface Property

The map’s color scheme when displaying standard or muted standard map types.

**Availability**:
- MapKit JS 5.13+

## Declaration

```
colorScheme?: ColorScheme;
```

## Discussion

This property accepts a property from [`ColorScheme`](../colorscheme.md) to determine whether the map displays with a dark or light theme when [`Standard`](../maptype/standard.md) or [`MutedStandard`](../maptype/mutedstandard.md) are the configured [`mapType`](../map/maptype.md). The default is [`Light`](../colorscheme/light.md).

The grid, user location accuracy ring, labels for marker annotations, and controls of the map change appearance to complement the Dark Mode style.

## See Also

### Setting the map’s appearance and controls
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
- [showsScale](./showsscale.md)
  A feature visibility setting that allows you to determine when to display the map’s scale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapconstructoroptions/colorscheme)*