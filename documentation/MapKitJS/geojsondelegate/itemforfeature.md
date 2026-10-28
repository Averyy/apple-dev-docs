# itemForFeature(item, geoJSON)

**Framework**: MapKit JS  
**Kind**: method  
**Role**: Interface Method

Overrides a feature.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
itemForFeature?(
    item: Item | null,
    geoJSON: GeoJSONTypes.Feature,
): Item | null;
```

## Return Value

A map item for the `feature`.

## Discussion

MapKit JS calls this method for every GeoJSON `feature`.

## Parameters

- `item`: An item the system creates for the geometry of the feature, or `null` for features with `null` geometry.
- `geoJSON`: The original GeoJSON object for the `feature`.

## See Also

### Overriding items
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
- [styleForOverlay(overlay, geoJSON)](./styleforoverlay.md)
  Overrides the style of overlays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/geojsondelegate/itemforfeature)*