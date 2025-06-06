# mapkit.Map.Distances

**Framework**: MapKit JS  
**Kind**: enum

Constants indicating the system of measurement that displays on the map.

**Availability**:
- MapKit JS 5.12+

## Declaration

```swift
interface mapkit.Map.Distances {
	const string Metric;
	const string Imperial;
	const string Adaptive;
};
```

#### Overview

Use these constants with the map’s [`distances`](mapkit.map/distances.md) property.

## Topics

### Distances Values
- [Adaptive](mapkit.map.distances/adaptive.md)
  A constant indicating the measurement system is adaptive, and determined based on the map’s language.
- [Metric](mapkit.map.distances/metric.md)
  A constant indicating the measurement system is metric.
- [Imperial](mapkit.map.distances/imperial.md)
  A constant indicating the measurement system is imperial.

## See Also

- [colorScheme](mapkit.map/colorscheme.md)
  The map’s color scheme when displaying standard or muted standard map types.
- [mapkit.Map.ColorSchemes](mapkit.map.colorschemes.md)
  Constants indicating the color scheme of the map.
- [distances](mapkit.map/distances.md)
  The system of measurement that displays on the map.
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

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.map.distances)*