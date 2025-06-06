# ItemCollection

**Framework**: MapKit JS  
**Kind**: class

A tree structure containing annotations, overlays, and nested item collection objects.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
interface ItemCollection
```

#### Overview

The [`importGeoJSON`](mapkit/importgeojson.md) method returns item collections. Don’t instantiate them directly.

## Topics

### Item collection properties
- [data](itemcollection/data.md)
  The raw GeoJSON data.
- [getFlattenedItemList](itemcollection/getflatteneditemlist.md)
  A flattened array of items that includes annotations and overlays.
- [items](itemcollection/items.md)
  A nested list of annotations, overlays, and other item collections.

## See Also

- [importGeoJSON](mapkit/importgeojson.md)
  Converts imported GeoJSON data to MapKit JS items.
- [GeoJSONDelegate](geojsondelegate.md)
  A delegate object that controls a GeoJSON import to override default behavior and provide custom style.
- [Displaying Indoor Maps with MapKit JS](displaying-indoor-maps-with-mapkit-js.md)
  Use the Indoor Mapping Data Format (IMDF) to show an indoor map with custom overlays and points of interest in your browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/itemcollection)*