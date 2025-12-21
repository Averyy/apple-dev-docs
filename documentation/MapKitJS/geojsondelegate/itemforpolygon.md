# itemForPolygon(overlay, geoJSON)

**Framework**: MapKit JS  
**Kind**: method

Overrides a polygon.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
itemForPolygon?(
        overlay: PolygonOverlay,
        geoJSON: GeoJSONTypes.Polygon,
    ): PolygonOverlay | null;
```

#### Return Value

A map item or an array of map items.

#### Discussion

MapKit JS calls this method for each individual `polygon` geometry object. The framework breaks `MultiPolygon` geometry types into individual polygon types.

## Parameters

- `overlay`: You can customize the provided overlay before returning it, or you can completely replace the overlay.
- `geoJSON`: The original GeoJSON object for the polygon.

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
- [itemForMultiPoint(itemCollection, geoJSON)](geojsondelegate/itemformultipoint.md)
  Overrides a multipoint object.
- [itemForMultiPolygon(itemCollection, geoJSON)](geojsondelegate/itemformultipolygon.md)
  Overrides a multipolygon.
- [styleForOverlay(overlay, geoJSON)](geojsondelegate/styleforoverlay.md)
  Overrides the style of overlays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/geojsondelegate/itemforpolygon)*