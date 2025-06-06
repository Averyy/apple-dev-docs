# itemForLineString

**Framework**: MapKit JS  
**Kind**: method

Overrides a line string.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
optional(mapkit.Annotation|mapkit.Overlay|(mapkit.Annotation|mapkit.Overlay)[]) itemForLineString(
	mapkit.PolylineOverlay overlay,
	Object geoJSON
);
```

#### Return Value

A map item or an array of map items.

#### Discussion

MapKit JS calls this method for each individual `LineString` geometry object. You can customize or completely replace the provided overlay before returning it.

## Parameters

- `overlay`: A   object.
- `geoJSON`: The original GeoJSON object for the   object.

## See Also

- [itemForFeature](geojsondelegate/itemforfeature.md)
  Overrides a feature.
- [itemForFeatureCollection](geojsondelegate/itemforfeaturecollection.md)
  Overrides a feature collection.
- [itemForMultiLineString](geojsondelegate/itemformultilinestring.md)
  Overrides a multiline string.
- [itemForPoint](geojsondelegate/itemforpoint.md)
  Overrides a point.
- [itemForMultiPoint](geojsondelegate/itemformultipoint.md)
  Overrides a multipoint object.
- [itemForPolygon](geojsondelegate/itemforpolygon.md)
  Overrides a polygon.
- [itemForMultiPolygon](geojsondelegate/itemformultipolygon.md)
  Overrides a multipolygon.
- [styleForOverlay](geojsondelegate/styleforoverlay.md)
  Overrides the style of overlays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/geojsondelegate/itemforlinestring)*