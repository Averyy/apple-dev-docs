# itemForPoint(coordinate, geoJSON)

**Framework**: MapKit JS  
**Kind**: method

Overrides a point.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
itemForPoint?(
        coordinate: Coordinate,
        geoJSON: GeoJSONTypes.Point,
    ): Item | null;
```

#### Return Value

An array of map items.

#### Discussion

MapKit JS calls this method for every `Point` object. For a `MultiPoint` object or for a `GeometryCollection` of `Points` and `MultiPoints`, the framework calls [`itemForPoint(coordinate, geoJSON)`](geojsondelegate/itemforpoint.md) for each individual `Point` object.

## Parameters

- `coordinate`: A GeoJSON   generates the coordinate. You can use the coordinate to instantiate an item to return.
- `geoJSON`: The original GeoJSON object for the  . This object may be a simple   or a   with the   geometry type.

## See Also

- [itemForFeature(item, geoJSON)](geojsondelegate/itemforfeature.md)
  Overrides a feature.
- [itemForFeatureCollection(itemCollection, geoJSON)](geojsondelegate/itemforfeaturecollection.md)
  Overrides a feature collection.
- [itemForLineString(overlay, geoJSON)](geojsondelegate/itemforlinestring.md)
  Overrides a line string.
- [itemForMultiLineString(itemCollection, geoJSON)](geojsondelegate/itemformultilinestring.md)
  Overrides a multiline string.
- [itemForMultiPoint(itemCollection, geoJSON)](geojsondelegate/itemformultipoint.md)
  Overrides a multipoint object.
- [itemForPolygon(overlay, geoJSON)](geojsondelegate/itemforpolygon.md)
  Overrides a polygon.
- [itemForMultiPolygon(itemCollection, geoJSON)](geojsondelegate/itemformultipolygon.md)
  Overrides a multipolygon.
- [styleForOverlay(overlay, geoJSON)](geojsondelegate/styleforoverlay.md)
  Overrides the style of overlays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/geojsondelegate/itemforpoint)*