# colorScheme

**Framework**: MapKit JS  
**Kind**: property

The map’s color scheme when displaying standard or muted standard map types.

**Availability**:
- MapKit JS 5.13+

## Declaration

```swift
get colorScheme(): ColorScheme;
set colorScheme(colorScheme: ColorScheme);
```

## Mentions

- [MapKit JS 5](mapkit-js-5.md)

#### Discussion

This property accepts a property from [`ColorScheme`](colorscheme.md) to determine whether the map displays with a dark or light theme when [`Standard`](maptype/standard.md) or [`MutedStandard`](maptype/mutedstandard.md) are the configured [`mapType`](map/maptype.md). The default is [`Light`](colorscheme/light.md).

The grid, user location accuracy ring, labels for marker annotations, and controls of the map change appearance to complement the Dark Mode style.

## Topics

### Color Schemes
- [const ColorScheme](colorscheme.md)
  Constants that indicate the color scheme of the map or a place detail.

## See Also

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
- [interface MapShowItemsOptions](mapshowitemsoptions.md)
  Options that determine the map parameters to use when showing items.
- [tintColor](map/tintcolor.md)
  The CSS color that MapKit JS uses for user interface controls on the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/map/colorscheme)*