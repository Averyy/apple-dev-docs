# MapType

**Framework**: MapKit JS  
**Kind**: enum

Constants representing the type of map to display.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
const MapType: Readonly<{
    readonly Satellite: "satellite";
    readonly Hybrid: "hybrid";
    readonly MutedStandard: "mutedStandard";
    readonly Standard: "standard";
}>
```

## Topics

### Map type values
- [Hybrid](maptype/hybrid.md)
  A satellite image of the area with road and road name layers on top.
- [MutedStandard](maptype/mutedstandard.md)
  A street map that emphasizes your data over the underlying map details.
- [Satellite](maptype/satellite.md)
  A satellite image of the area.
- [Standard](maptype/standard.md)
  A street map that shows the position of all roads and some road names.
### Type Aliases
- [type MapType](maptype/maptype.md)
  A type alias that represents the values of map type enumeration.

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

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/maptype)*