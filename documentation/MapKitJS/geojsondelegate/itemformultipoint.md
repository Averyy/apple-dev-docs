# itemForMultiPoint(itemCollection, geoJSON)

**Framework**: MapKit JS  
**Kind**: method

Overrides a multipoint object.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
itemForMultiPoint?<D extends GeoJSONTypes.MultiPoint>(
        itemCollection: ItemCollection<D>,
        geoJSON: D,
    ): ItemCollection<D> | Item[] | null;
```

#### Return Value

A map item or an array of map items.

#### Discussion

MapKit JS calls this method for every `MultiPoint` object. The framework also calls this method after constructing subitems, and calling their delegate functions.

## Parameters

- `itemCollection`: A collection containing associated annotations.
- `geoJSON`: The original GeoJSON object for the  . This contains an array of geometries.

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
- [itemForPolygon(overlay, geoJSON)](geojsondelegate/itemforpolygon.md)
  Overrides a polygon.
- [itemForMultiPolygon(itemCollection, geoJSON)](geojsondelegate/itemformultipolygon.md)
  Overrides a multipolygon.
- [styleForOverlay(overlay, geoJSON)](geojsondelegate/styleforoverlay.md)
  Overrides the style of overlays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/geojsondelegate/itemformultipoint)*