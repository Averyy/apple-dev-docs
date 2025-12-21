# itemForFeature(item, geoJSON)

**Framework**: MapKit JS  
**Kind**: method

Overrides a feature.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
itemForFeature?(
        item: Item | null,
        geoJSON: GeoJSONTypes.Feature,
    ): Item | null;
```

#### Return Value

A map item for the `feature`.

#### Discussion

MapKit JS calls this method for every GeoJSON `feature`.

## Parameters

- `item`: An item the system creates for the geometry of the feature, or   for features with   geometry.
- `geoJSON`: The original GeoJSON object for the  .

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/geojsondelegate/itemforfeature)*