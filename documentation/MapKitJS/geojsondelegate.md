# GeoJSONDelegate

**Framework**: MapKit JS  
**Kind**: class

A delegate object that controls a GeoJSON import to override default behavior and provide custom style.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
interface GeoJSONDelegate
```

#### Overview

The delegate object provides hooks into the key moments in the GeoJSON import process. When you pass a delegate object to the [`importGeoJSON`](mapkit/importgeojson.md) method, you can:

- Modify or replace annotations and overlays before MapKit JS adds them to the [`ItemCollection`](itemcollection.md) object.
- Override the default GeoJSON mapping behavior.
- Provide custom styling by implementing [`styleForOverlay`](geojsondelegate/styleforoverlay.md).
- Receive feedback on the result from importing GeoJSON data.

## Topics

### Overriding items
- [itemForFeature](geojsondelegate/itemforfeature.md)
  Overrides a feature.
- [itemForFeatureCollection](geojsondelegate/itemforfeaturecollection.md)
  Overrides a feature collection.
- [itemForLineString](geojsondelegate/itemforlinestring.md)
  Overrides a line string.
- [itemForMultiLineString](geojsondelegate/itemformultilinestring.md)
  Overrides a multiline string.
- [itemForPoint](geojsondelegate/itemforpoint.md)
  Overrides a point.
- [itemForMultiPoint](geojsondelegate/itemformultipoint.md)
  Overrides a multipoint object.
- [itemForPolygon](geojsondelegate/itemforpolygon.md)
  Overrides a polygon.
- [itemForMultiPolygon](geojsondelegate/itemformultipolygon.md)
  Overrides a multipolygon.
- [styleForOverlay](geojsondelegate/styleforoverlay.md)
  Overrides the style of overlays.
### Handling errors and completion
- [geoJSONDidComplete](geojsondelegate/geojsondidcomplete.md)
  Completes the GeoJSON import.
- [geoJSONDidError](geojsondelegate/geojsondiderror.md)
  Indicates when the GeoJSON import fails.

## See Also

- [importGeoJSON](mapkit/importgeojson.md)
  Converts imported GeoJSON data to MapKit JS items.
- [ItemCollection](itemcollection.md)
  A tree structure containing annotations, overlays, and nested item collection objects.
- [Displaying Indoor Maps with MapKit JS](displaying-indoor-maps-with-mapkit-js.md)
  Use the Indoor Mapping Data Format (IMDF) to show an indoor map with custom overlays and points of interest in your browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/geojsondelegate)*