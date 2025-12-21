# tintColor

**Framework**: MapKit JS  
**Kind**: property

The CSS color that MapKit JS uses for user interface controls on the map.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
get tintColor(): string;
set tintColor(value: string);
```

#### Discussion

Use `tintColor` to color the outline of the controls, text, and glyphs. The tint color can be any valid [`CSS color value or standard color name`](https://developer.apple.comhttps://drafts.csswg.org/css-color/#named-colors).

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
- [interface MapShowItemsOptions](mapshowitemsoptions.md)
  Options that determine the map parameters to use when showing items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/map/tintcolor)*