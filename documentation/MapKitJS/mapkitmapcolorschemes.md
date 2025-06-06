# mapkit.Map.ColorSchemes

**Framework**: MapKit JS  
**Kind**: enum

Constants indicating the color scheme of the map.

**Availability**:
- MapKit JS 5.12+

## Declaration

```swift
interface mapkit.Map.ColorSchemes {
	const string Light;
	const string Dark;
	const string Adaptive;
};
```

#### Overview

Color schemes apply to maps that have a standard or muted standard map type ([`Standard`](mapkit.map.maptypes/standard.md) or [`MutedStandard`](mapkit.map.maptypes/mutedstandard.md)). Use these constants with the map’s [`colorScheme`](mapkit.map/colorscheme.md) property.

## Topics

### Color scheme values
- [Adaptive](mapkit.map.colorschemes/adaptive.md)
  A constant indicating a color scheme that follows the current system setting.
- [Light](mapkit.map.colorschemes/light.md)
  A constant indicating a light color scheme.
- [Dark](mapkit.map.colorschemes/dark.md)
  A constant indicating a dark color scheme.

## See Also

- [colorScheme](mapkit.map/colorscheme.md)
  The map’s color scheme when displaying standard or muted standard map types.
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

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.map.colorschemes)*