# styleForOverlay(overlay, geoJSON)

**Framework**: MapKit JS  
**Kind**: method  
**Role**: Interface Method

Overrides the style of overlays.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
styleForOverlay?(
    overlay: PolylineOverlay | PolygonOverlay,
    geoJSON: GeoJSONTypes.LineString | GeoJSONTypes.Polygon,
): Style;
```

## Return Value

This method returns a [`Style`](../style.md) object for the provided overlay.

## Discussion

MapKit JS calls this method for each overlay, and after each call to [`itemForPoint()`](./itemforpoint.md) and [`itemForPolygon()`](./itemforpolygon.md).

## Parameters

- `overlay`: The overlay to style.
- `geoJSON`: The original GeoJSON for the `feature` or `geometry` object`.`

## See Also

### Overriding items
- [itemForFeature(item, geoJSON)](./itemforfeature.md)
  Overrides a feature.
- [itemForFeatureCollection(itemCollection, geoJSON)](./itemforfeaturecollection.md)
  Overrides a feature collection.
- [itemForLineString(overlay, geoJSON)](./itemforlinestring.md)
  Overrides a line string.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/geojsondelegate/styleforoverlay)*