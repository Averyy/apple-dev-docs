# itemForPoint(coordinate, geoJSON)

**Framework**: MapKit JS  
**Kind**: method  
**Role**: Interface Method

Overrides a point.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
itemForPoint?(
    coordinate: Coordinate,
    geoJSON: GeoJSONTypes.Point,
): Item | null;
```

## Return Value

An array of map items.

## Discussion

MapKit JS calls this method for every `Point` object. For a `MultiPoint` object or for a `GeometryCollection` of `Points` and `MultiPoints`, the framework calls [`itemForPoint()`](./itemforpoint.md) for each individual `Point` object.

## Parameters

- `coordinate`: A GeoJSON `Point` generates the coordinate. You can use the coordinate to instantiate an item to return.
- `geoJSON`: The original GeoJSON object for the `Point`. This object may be a simple `Point` or a `Feature` with the `Point` geometry type.

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
- [itemForMultiPoint(itemCollection, geoJSON)](./itemformultipoint.md)
  Overrides a multipoint object.
- [itemForPolygon(overlay, geoJSON)](./itemforpolygon.md)
  Overrides a polygon.
- [itemForMultiPolygon(itemCollection, geoJSON)](./itemformultipolygon.md)
  Overrides a multipolygon.
- [styleForOverlay(overlay, geoJSON)](./styleforoverlay.md)
  Overrides the style of overlays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/geojsondelegate/itemforpoint)*