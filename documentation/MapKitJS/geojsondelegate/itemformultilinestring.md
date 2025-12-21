# itemForMultiLineString(itemCollection, geoJSON)

**Framework**: MapKit JS  
**Kind**: method

Overrides a multiline string.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
itemForMultiLineString?<D extends GeoJSONTypes.MultiLineString>(
        itemCollection: ItemCollection<D>,
        geoJSON: D,
    ): ItemCollection<D> | Item[] | null;
```

#### Return Value

A map item or an array of map items.

#### Discussion

MapKit JS calls this method for every `MultiLineString` object. The framework also calls this method after constructing subitems and calling their delegate functions.

## Parameters

- `itemCollection`: An item collection containing associated overlays.
- `geoJSON`: The original GeoJSON object for the  . This contains an array of geometries.

## See Also

- [itemForFeature(item, geoJSON)](geojsondelegate/itemforfeature.md)
  Overrides a feature.
- [itemForFeatureCollection(itemCollection, geoJSON)](geojsondelegate/itemforfeaturecollection.md)
  Overrides a feature collection.
- [itemForLineString(overlay, geoJSON)](geojsondelegate/itemforlinestring.md)
  Overrides a line string.
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

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/geojsondelegate/itemformultilinestring)*