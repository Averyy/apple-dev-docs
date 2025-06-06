# itemForPolygon

**Framework**: MapKit JS  
**Kind**: method

Overrides a polygon.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
optional(mapkit.Annotation|mapkit.Overlay|(mapkit.Annotation|mapkit.Overlay)[]) itemForPolygon(
	mapkit.PolygonOverlay overlay,
	Object geoJSON
);
```

#### Return Value

A map item or an array of map items.

#### Discussion

MapKit JS calls this method for each individual `polygon` geometry object. The framework breaks `MultiPolygon` geometry types into individual polygon types.

## Parameters

- `overlay`: You can customize the provided overlay before returning it, or you can completely replace the overlay.
- `geoJSON`: The original GeoJSON object for the polygon.

## See Also

- [itemForFeature](geojsondelegate/itemforfeature.md)
  Overrides a feature.
- [itemForFeatureCollection](geojsondelegate/itemforfeaturecollection.md)
  Overrides a feature collection.
- [itemForLineString](geojsondelegate/itemforlinestring.md)
  Overrides a line string.
- [itemForMultiLineString](geojsondelegate/itemformultilinestring.md)
  Overrides a multiline string.
- [itemForPoint](geojsondelegate/itemforpoint.md)
  Overrides a point.
- [itemForMultiPoint](geojsondelegate/itemformultipoint.md)
  Overrides a multipoint object.
- [itemForMultiPolygon](geojsondelegate/itemformultipolygon.md)
  Overrides a multipolygon.
- [styleForOverlay](geojsondelegate/styleforoverlay.md)
  Overrides the style of overlays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/geojsondelegate/itemforpolygon)*