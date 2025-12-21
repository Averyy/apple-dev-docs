# itemForLineString(overlay, geoJSON)

**Framework**: MapKit JS  
**Kind**: method

Overrides a line string.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
itemForLineString?(
        overlay: PolylineOverlay,
        geoJSON: GeoJSONTypes.LineString,
    ): PolylineOverlay | null;
```

#### Return Value

A map item or an array of map items.

#### Discussion

MapKit JS calls this method for each individual `LineString` geometry object. You can customize or completely replace the provided overlay before returning it.

## Parameters

- `overlay`: A   object.
- `geoJSON`: The original GeoJSON object for the   object.

## See Also

- [itemForFeature(item, geoJSON)](geojsondelegate/itemforfeature.md)
  Overrides a feature.
- [itemForFeatureCollection(itemCollection, geoJSON)](geojsondelegate/itemforfeaturecollection.md)
  Overrides a feature collection.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/geojsondelegate/itemforlinestring)*