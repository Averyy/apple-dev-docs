# itemForLineString(overlay, geoJSON)

**Framework**: MapKit JS  
**Kind**: method  
**Role**: Interface Method

Overrides a line string.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
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

- `overlay`: A [`PolylineOverlay`](../polylineoverlay.md) object.
- `geoJSON`: The original GeoJSON object for the `LineString` object.

## See Also

### Overriding items
- [itemForFeature(item, geoJSON)](./itemforfeature.md)
  Overrides a feature.
- [itemForFeatureCollection(itemCollection, geoJSON)](./itemforfeaturecollection.md)
  Overrides a feature collection.
- [itemForMultiLineString(itemCollection, geoJSON)](./itemformultilinestring.md)
  Overrides a multiline string.
- [itemForPoint(coordinate, geoJSON)](./itemforpoint.md)
  Overrides a point.
- [itemForMultiPoint(itemCollection, geoJSON)](./itemformultipoint.md)
  Overrides a multipoint object.
- [itemForPolygon(overlay, geoJSON)](./itemforpolygon.md)
  Overrides a polygon.
- [itemForMultiPolygon(itemCollection, geoJSON)](./itemformultipolygon.md)
  Overrides a multipolygon.
- [styleForOverlay(overlay, geoJSON)](./styleforoverlay.md)
  Overrides the style of overlays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/geojsondelegate/itemforlinestring)*