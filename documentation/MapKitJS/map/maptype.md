# mapType

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Instance Property

The type of data that the map displays.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
get mapType(): MapType;
set mapType(mapType: MapType);
```

## Mentions

- [MapKit JS 5](../mapkit-js-5.md)

#### Discussion

The map type determines whether the map shows a standard view, a satellite view, or a hybrid view. The map type is a value of [`MapType`](../maptype.md).

## See Also

### Configuring the map’s appearance
- [colorScheme](./colorscheme.md)
  The map’s color scheme when displaying standard or muted standard map types.
- [distances](./distances-data.property.md)
  The system of measurement that displays on the map.
- [padding](./padding.md)
  The map’s inset margins.
- [pointOfInterestFilter](./pointofinterestfilter.md)
  The filter that determines the points of interest that display on the map.
- [showsPointsOfInterest](./showspointsofinterest.md)
  A Boolean value that determines whether the map displays points of interest.
- [showItems(items, options)](./showitems.md)
  Adjusts the map’s visible region to bring the specified overlays and annotations into view.
- [interface MapShowItemsOptions](../mapshowitemsoptions.md)
  Options that determine the map parameters to use when showing items.
- [tintColor](./tintcolor.md)
  The CSS color that MapKit JS uses for user interface controls on the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/map/maptype)*