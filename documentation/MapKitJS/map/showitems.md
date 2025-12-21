# showItems(items, options)

**Framework**: MapKit JS  
**Kind**: method

Adjusts the map’s visible region to bring the specified overlays and annotations into view.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
showItems(
        items: (Overlay | Annotation)[],
        options?: MapShowItemsOptions,
    ): (Annotation | Overlay)[];
```

## Mentions

- [MapKit JS 5](mapkit-js-5.md)

#### Return Value

Returns the items array that you pass.

#### Discussion

The method [`showItems(items, options)`](map/showitems.md) adjusts the map’s [`region`](map/region.md) to bring all of the specified items — annotations and overlays — into view. The system only adds items if they’re not already on the map.

The map’s adjusted region covers the smallest longitudinal span possible. For example, passing an array that consists of two annotations for the cities Tokyo and Los Angeles, and a polyline that represents the flight path between them, to [`showItems(items, options)`](map/showitems.md) updates the region to cover the Pacific Ocean.

The [`showItems(items, options)`](map/showitems.md) method factors in the size of the specified annotations when updating the map’s region so the entirety of the annotations are visible. Similarly, it ensures that the map shows an overlay with thick lines in its entirety. In some cases, it’s possible that the map can’t show all items at once, or the actual padding doesn’t match the requested padding. This happens if:

- One or more items falls outside of the visible map region, even at the minimum zoom level.
- The zoom level, which determines the amount of padding, snaps to a level that has a different amount of padding than you request.

This method throws an `Error` if the arguments to the method are invalid.

The following example demonstrates how to use `showItems:`

```javascript
const park = new mapkit.MarkerAnnotation(new mapkit.Coordinate(37.749581, -119.524212), { title: "Yosemite" }),
    surf = new mapkit.MarkerAnnotation(new mapkit.Coordinate(37.49557, -122.496687), { title: "Mavericks" });
map.showItems([park, surf],
              { animate: true,
                padding: new mapkit.Padding(60, 25, 60, 25)
              });
```

## Parameters

- `items`: An array of annotations and overlays to make visible.
- `options`: Options that   defines that let you determine animation, and the framing of the map.

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
- [interface MapShowItemsOptions](mapshowitemsoptions.md)
  Options that determine the map parameters to use when showing items.
- [tintColor](map/tintcolor.md)
  The CSS color that MapKit JS uses for user interface controls on the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/map/showitems)*