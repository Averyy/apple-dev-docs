# GeoJSONImporterCallback

**Framework**: MapKit JS  
**Kind**: typealias

A callback function that MapKit JS invokes when importing a GeoJSON object.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
type GeoJSONImporterCallback = (
    ...args:
        | [GeoJSONImportError, GeoJSONTypes.GeoJSON | undefined]
        | [null, ItemCollection]
) => void;
```

#### Discussion

MapKit JS invokes this callback with two arguments, `error` on failure and `result` on success, as follows:

## See Also

- [importGeoJSON(data, callback)](mapkit/importgeojson.md)
  Converts imported GeoJSON data to MapKit JS compatible items.
- [interface GeoJSONDelegate](geojsondelegate.md)
  A delegate object that controls a GeoJSON import to override default behavior and provide custom style.
- [type Item](item.md)
  A type alias that represents all objects that the framework sets in an item collection.
- [class ItemCollection](itemcollection.md)
  A tree structure containing annotations, overlays, and nested item collection objects.
- [class GeoJSONImportError](geojsonimporterror.md)
  An error object that indicates an error occurred while importing a GeoJSON object.
- [Displaying Indoor Maps with MapKit JS](displaying-indoor-maps-with-mapkit-js.md)
  Use the Indoor Mapping Data Format (IMDF) to show an indoor map with custom overlays and points of interest in your browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/geojsonimportercallback)*