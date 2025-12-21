# distances

**Framework**: MapKit JS  
**Kind**: property

The system of measurement that displays on the map.

**Availability**:
- MapKit JS 5.12+

## Declaration

```swift
get distances(): Distance;
set distances(distances: Distance);
```

## Mentions

- [MapKit JS 5](mapkit-js-5.md)

#### Discussion

Sets the system of measurement for displaying map distances. See [`Distance`](distance.md) for accepted values.

This property applies to the scale, if it displays. The default value is [`Adaptive`](distance/adaptive.md), which means that the measurement system depends on the map’s set [`language`](mapkitinitializationoptions/language.md). This property affects displayed distances only; it doesn’t affect data that returns from a service, such as [`Directions`](directions.md).

## Topics

### Distances
- [const Distance](distance.md)
  Constants indicating the system of measurement that displays on the map.

## See Also

- [colorScheme](map/colorscheme.md)
  The map’s color scheme when displaying standard or muted standard map types.
- [const ColorScheme](colorscheme.md)
  Constants that indicate the color scheme of the map or a place detail.
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

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/map/distances-data.property)*