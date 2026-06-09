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

This property accepts a value from [`ColorScheme`](colorscheme.md) to determine whether the map displays with a dark or light theme when [`Standard`](maptype/standard.md) or [`MutedStandard`](maptype/mutedstandard.md) are the configured [`mapType`](map/maptype.md). The default is [`Light`](colorscheme/light.md).

The map updates the grid, user location accuracy ring, marker annotation labels, and controls to complement the Dark Mode style.

## See Also

- [distances](map/distances-data.property.md)
  The system of measurement that displays on the map.
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

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/map/colorscheme)*