# itemForMultiPolygon(itemCollection, geoJSON)

**Framework**: MapKit JS  
**Kind**: method  
**Role**: Interface Method

Overrides a multipolygon.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
itemForMultiPolygon?<D extends GeoJSONTypes.MultiPolygon>(
    itemCollection: ItemCollection<D>,
    geoJSON: D,
): ItemCollection<D> | Item[] | null;
```

#### Return Value

A map item or an array of map items.

#### Discussion

MapKit JS calls this method for every `MultiPolygon` object. The framework also calls this method after constructing subitems, and calling their delegate functions.

## Parameters

- `itemCollection`: A collection containing associated overlays.
- `geoJSON`: The original GeoJSON object for the `MultiPolygon`. It contains an array of geometries.

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
- [styleForOverlay(overlay, geoJSON)](./styleforoverlay.md)
  Overrides the style of overlays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/geojsondelegate/itemformultipolygon)*