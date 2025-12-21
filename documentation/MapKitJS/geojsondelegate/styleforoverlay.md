# styleForOverlay(overlay, geoJSON)

**Framework**: MapKit JS  
**Kind**: method

Overrides the style of overlays.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
styleForOverlay?(
        overlay: PolylineOverlay | PolygonOverlay,
        geoJSON: GeoJSONTypes.LineString | GeoJSONTypes.Polygon,
    ): Style;
```

#### Return Value

This method returns a [`Style`](style.md) object for the provided overlay.

#### Discussion

MapKit JS calls this method for each overlay, and after each call to [`itemForPoint(coordinate, geoJSON)`](geojsondelegate/itemforpoint.md) and [`itemForPolygon(overlay, geoJSON)`](geojsondelegate/itemforpolygon.md).

## Parameters

- `overlay`: The overlay to style.
- `geoJSON`: The original GeoJSON for the   or   object

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/geojsondelegate/styleforoverlay)*