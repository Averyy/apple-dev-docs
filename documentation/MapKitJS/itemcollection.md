# ItemCollection

**Framework**: MapKit JS  
**Kind**: class

A tree structure containing annotations, overlays, and nested item collection objects.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
class ItemCollection<D = any>
```

#### Overview

The [`importGeoJSON(data, callback)`](mapkit/importgeojson.md) method returns item collections. Don’t instantiate them directly.

## Topics

### Item collection properties
- [data](itemcollection/data.md)
  The raw GeoJSON data.
- [getFlattenedItemList()](itemcollection/getflatteneditemlist.md)
  A flattened array of items that includes annotations and overlays.
- [items](itemcollection/items.md)
  A nested list of annotations, overlays, and other item collections.

## See Also

- [importGeoJSON(data, callback)](mapkit/importgeojson.md)
  Converts imported GeoJSON data to MapKit JS compatible items.
- [interface GeoJSONDelegate](geojsondelegate.md)
  A delegate object that controls a GeoJSON import to override default behavior and provide custom style.
- [type Item](item.md)
  A type alias that represents all objects that the framework sets in an item collection.
- [type GeoJSONImporterCallback](geojsonimportercallback.md)
  A callback function that MapKit JS invokes when importing a GeoJSON object.
- [class GeoJSONImportError](geojsonimporterror.md)
  An error object that indicates an error occurred while importing a GeoJSON object.
- [Displaying Indoor Maps with MapKit JS](displaying-indoor-maps-with-mapkit-js.md)
  Use the Indoor Mapping Data Format (IMDF) to show an indoor map with custom overlays and points of interest in your browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/itemcollection)*