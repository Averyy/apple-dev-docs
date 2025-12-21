# ColorScheme

**Framework**: MapKit JS  
**Kind**: enum

Constants that indicate the color scheme of the map or a place detail.

**Availability**:
- MapKit JS 5.12+

## Declaration

```swift
const ColorScheme: Readonly<{
    readonly Dark: "dark";
    readonly Light: "light";
    readonly Adaptive: "adaptive";
}>
```

#### Overview

Color schemes apply to maps that have a [`Standard`](maptype/standard.md) or [`MutedStandard`](maptype/mutedstandard.md) map type. Use these constants with the map’s [`colorScheme`](map/colorscheme.md) property.

## Topics

### Color scheme values
- [Adaptive](colorscheme/adaptive.md)
  A constant indicating a color scheme that follows the current system setting.
- [Light](colorscheme/light.md)
  A constant indicating a light color scheme.
- [Dark](colorscheme/dark.md)
  A constant indicating a dark color scheme.
### Type Aliases
- [type ColorScheme](colorscheme/colorscheme.md)
  A type alias that represents the values of the color scheme enumeration.

## See Also

- [colorScheme](map/colorscheme.md)
  The map’s color scheme when displaying standard or muted standard map types.
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
- [interface MapShowItemsOptions](mapshowitemsoptions.md)
  Options that determine the map parameters to use when showing items.
- [tintColor](map/tintcolor.md)
  The CSS color that MapKit JS uses for user interface controls on the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/colorscheme)*