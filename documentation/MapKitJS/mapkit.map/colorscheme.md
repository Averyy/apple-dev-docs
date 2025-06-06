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

## Mentions

- [MapKit JS 5](mapkit-js-5.md)

#### Discussion

This property accepts a property from [`mapkit.Map.ColorSchemes`](mapkit.map.colorschemes.md) to determine whether the map displays with a dark or light theme when [`Standard`](mapkit.map.maptypes/standard.md) or [`MutedStandard`](mapkit.map.maptypes/mutedstandard.md) are the configured [`mapType`](mapkit.map/maptype.md). The default is [`Light`](mapkit.map.colorschemes/light.md).

The grid, user location accuracy ring, labels for marker annotations, and controls of the map change appearance to complement the Dark Mode style.

## Topics

### Color Schemes
- [mapkit.Map.ColorSchemes](mapkit.map.colorschemes.md)
  Constants indicating the color scheme of the map.

## See Also

- [mapkit.Map.ColorSchemes](mapkit.map.colorschemes.md)
  Constants indicating the color scheme of the map.
- [distances](mapkit.map/distances.md)
  The system of measurement that displays on the map.
- [mapkit.Map.Distances](mapkit.map.distances.md)
  Constants indicating the system of measurement that displays on the map.
- [mapType](mapkit.map/maptype.md)
  The type of data that the map displays.
- [mapkit.Map.MapTypes](mapkit.map.maptypes.md)
  Constants representing the type of map to display.
- [padding](mapkit.map/padding.md)
  The map’s inset margins.
- [pointOfInterestFilter](mapkit.map/pointofinterestfilter.md)
  The filter that determines the points of interest that display on the map.
- [showsPointsOfInterest](mapkit.map/showspointsofinterest.md)
  A Boolean value that determines whether the map displays points of interest.
- [showItems](mapkit.map/showitems.md)
  Adjusts the map’s visible region to bring the specified overlays and annotations into view.
- [MapShowItemsOptions](mapshowitemsoptions.md)
  Options that determine the map parameters to use when showing items.
- [tintColor](mapkit.map/tintcolor.md)
  The CSS color that MapKit JS uses for user interface controls on the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.map/colorscheme)*