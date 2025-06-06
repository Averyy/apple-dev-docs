# MapShowItemsOptions

**Framework**: MapKit JS  
**Kind**: struct

Options that determine the map parameters to use when showing items.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
dictionary MapShowItemsOptions {
	boolean animate;
	mapkit.Padding padding;
	mapkit.CoordinateSpan minimumSpan;
};
```

#### Overview

Use these options when calling [`showItems`](mapkit.map/showitems.md).

## Topics

### Show item options
- [animate](mapshowitemsoptions/animate.md)
  A Boolean value that determines whether the map animates as the map region changes to show the items.
- [minimumSpan](mapshowitemsoptions/minimumspan.md)
  The minimum longitudinal and latitudinal span the map displays.
- [padding](mapshowitemsoptions/padding.md)
  Spacing that the framework adds around the computed map region when showing items.

## See Also

- [colorScheme](mapkit.map/colorscheme.md)
  The map’s color scheme when displaying standard or muted standard map types.
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
- [tintColor](mapkit.map/tintcolor.md)
  The CSS color that MapKit JS uses for user interface controls on the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapshowitemsoptions)*