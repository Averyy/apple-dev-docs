# MapShowItemsOptions

**Framework**: MapKit JS  
**Kind**: struct

Options that determine the map parameters to use when showing items.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
interface MapShowItemsOptions
```

#### Overview

Use these options when calling [`showItems(items, options)`](map/showitems.md).

## Topics

### Show item options
- [animate](mapshowitemsoptions/animate.md)
  A Boolean value that determines whether the map animates as the map region changes to show the items.
- [minimumSpan](mapshowitemsoptions/minimumspan.md)
  The minimum longitudinal and latitudinal span the map displays.
- [padding](mapshowitemsoptions/padding.md)
  Spacing that the framework adds around the computed map region when showing items.
- [cameraDistance](mapshowitemsoptions/cameradistance.md)
  The distance from the center of the map to the camera, when showing the items.

## See Also

- [colorScheme](map/colorscheme.md)
  The map’s color scheme when displaying standard or muted standard map types.
- [const ColorScheme](colorscheme.md)
  Constants that indicate the color scheme of the map or a place detail.
- [distances](map/distances-data.property.md)
  The system of measurement that displays on the map.
- [const Distance](distance.md)
  Constants indicating the system of measurement that displays on the map.
- [mapType](map/maptype.md)
  The type of data that the map displays.
- [const MapType](maptype.md)
  Constants representing the type of map to display.
- [padding](map/padding.md)
  The map’s inset margins.
- [pointOfInterestFilter](map/pointofinterestfilter.md)
  The filter that determines the points of interest that display on the map.
- [showsPointsOfInterest](map/showspointsofinterest.md)
  A Boolean value that determines whether the map displays points of interest.
- [showItems(items, options)](map/showitems.md)
  Adjusts the map’s visible region to bring the specified overlays and annotations into view.
- [tintColor](map/tintcolor.md)
  The CSS color that MapKit JS uses for user interface controls on the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapshowitemsoptions)*