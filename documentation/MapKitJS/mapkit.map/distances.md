# distances

**Framework**: MapKit JS  
**Kind**: property

The system of measurement that displays on the map.

**Availability**:
- MapKit JS 5.12+

## Declaration

```swift
attribute string distances;
```

## Mentions

- [MapKit JS 5](mapkit-js-5.md)

#### Discussion

Sets the system of measurement for displaying map distances. See [`mapkit.Map.Distances`](mapkit.map.distances.md) for accepted values.

This property applies to the scale, if it displays. The default value is [`Adaptive`](mapkit.map.distances/adaptive.md), which means that the measurement system depends on the map’s set [`language`](mapkitinitoptions/language.md). This property affects displayed distances only; it doesn’t affect data that returns from a service, such as [`mapkit.Directions`](mapkit.directions.md).

## Topics

### Distances
- [mapkit.Map.Distances](mapkit.map.distances.md)
  Constants indicating the system of measurement that displays on the map.

## See Also

- [colorScheme](mapkit.map/colorscheme.md)
  The map’s color scheme when displaying standard or muted standard map types.
- [mapkit.Map.ColorSchemes](mapkit.map.colorschemes.md)
  Constants indicating the color scheme of the map.
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

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.map/distances)*