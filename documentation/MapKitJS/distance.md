# Distance

**Framework**: MapKit JS  
**Kind**: enum

Constants indicating the system of measurement that displays on the map.

**Availability**:
- MapKit JS 5.13+

## Declaration

```swift
const Distance: Readonly<{
    readonly Adaptive: "adaptive";
    readonly Metric: "metric";
    readonly Imperial: "imperial";
}>
```

#### Overview

Use these constants with the map’s [`distances`](map/distances-data.property.md) property.

## Topics

### Distances Values
- [Adaptive](distance/adaptive.md)
  A constant indicating the measurement system is adaptive, and determined based on the map’s language.
- [Metric](distance/metric.md)
  A constant indicating the measurement system is metric.
- [Imperial](distance/imperial.md)
  A constant indicating the measurement system is imperial.
### Type Aliases
- [type Distance](distance/distance.md)
  A type alias that represents the values of the distance enumeration.

## See Also

- [colorScheme](map/colorscheme.md)
  The map’s color scheme when displaying standard or muted standard map types.
- [const ColorScheme](colorscheme.md)
  Constants that indicate the color scheme of the map or a place detail.
- [distances](map/distances-data.property.md)
  The system of measurement that displays on the map.
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

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/distance)*