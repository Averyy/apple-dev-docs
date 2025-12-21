# GeoJSONDelegate

**Framework**: MapKit JS  
**Kind**: struct

A delegate object that controls a GeoJSON import to override default behavior and provide custom style.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
interface GeoJSONDelegate
```

#### Overview

The delegate object provides hooks into the key moments in the GeoJSON import process. When you pass a delegate object to the [`importGeoJSON(data, callback)`](mapkit/importgeojson.md) method, you can:

- Modify or replace annotations and overlays before MapKit JS adds them to the [`ItemCollection`](itemcollection.md) object.
- Override the default GeoJSON mapping behavior.
- Provide custom styling by implementing [`styleForOverlay(overlay, geoJSON)`](geojsondelegate/styleforoverlay.md).
- Receive feedback on the result from importing GeoJSON data.

## Topics

### Overriding items
- [itemForFeature(item, geoJSON)](geojsondelegate/itemforfeature.md)
  Overrides a feature.
- [itemForFeatureCollection(itemCollection, geoJSON)](geojsondelegate/itemforfeaturecollection.md)
  Overrides a feature collection.
- [itemForLineString(overlay, geoJSON)](geojsondelegate/itemforlinestring.md)
  Overrides a line string.
- [itemForMultiLineString(itemCollection, geoJSON)](geojsondelegate/itemformultilinestring.md)
  Overrides a multiline string.
- [itemForPoint(coordinate, geoJSON)](geojsondelegate/itemforpoint.md)
  Overrides a point.
- [itemForMultiPoint(itemCollection, geoJSON)](geojsondelegate/itemformultipoint.md)
  Overrides a multipoint object.
- [itemForPolygon(overlay, geoJSON)](geojsondelegate/itemforpolygon.md)
  Overrides a polygon.
- [itemForMultiPolygon(itemCollection, geoJSON)](geojsondelegate/itemformultipolygon.md)
  Overrides a multipolygon.
- [styleForOverlay(overlay, geoJSON)](geojsondelegate/styleforoverlay.md)
  Overrides the style of overlays.
### Handling errors and completion
- [geoJSONDidComplete(result, geoJSON)](geojsondelegate/geojsondidcomplete.md)
  Completes the GeoJSON import.
- [geoJSONDidError(error, geoJSON)](geojsondelegate/geojsondiderror.md)
  Indicates when the GeoJSON import fails.
### Instance Methods
- [itemForGeometryCollection(item, object)](geojsondelegate/itemforgeometrycollection.md)
  Overrides a geometry collection with the provided item and object.

## See Also

- [importGeoJSON(data, callback)](mapkit/importgeojson.md)
  Converts imported GeoJSON data to MapKit JS compatible items.
- [type Item](item.md)
  A type alias that represents all objects that the framework sets in an item collection.
- [class ItemCollection](itemcollection.md)
  A tree structure containing annotations, overlays, and nested item collection objects.
- [type GeoJSONImporterCallback](geojsonimportercallback.md)
  A callback function that MapKit JS invokes when importing a GeoJSON object.
- [class GeoJSONImportError](geojsonimporterror.md)
  An error object that indicates an error occurred while importing a GeoJSON object.
- [Displaying Indoor Maps with MapKit JS](displaying-indoor-maps-with-mapkit-js.md)
  Use the Indoor Mapping Data Format (IMDF) to show an indoor map with custom overlays and points of interest in your browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/geojsondelegate)*