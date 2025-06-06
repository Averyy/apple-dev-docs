# itemForPoint

**Framework**: MapKit JS  
**Kind**: method

Overrides a point.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
optional(mapkit.Annotation|mapkit.Overlay|(mapkit.Annotation|mapkit.Overlay)[]) itemForPoint(
	mapkit.Coordinate coordinate,
	Object geoJSON
);
```

#### Return Value

An array of map items.

#### Discussion

MapKit JS calls this method for every `Point` object. For a `MultiPoint` object or for a `GeometryCollection` of `Points` and `MultiPoints`, the framework calls [`itemForPoint`](geojsondelegate/itemforpoint.md) for each individual `Point` object.

## Parameters

- `coordinate`: A GeoJSON   generates the coordinate. You can use the coordinate to instantiate an item to return.
- `geoJSON`: The original GeoJSON object for the  . This object may be a simple   or a   with the   geometry type.

## See Also

- [itemForFeature](geojsondelegate/itemforfeature.md)
  Overrides a feature.
- [itemForFeatureCollection](geojsondelegate/itemforfeaturecollection.md)
  Overrides a feature collection.
- [itemForLineString](geojsondelegate/itemforlinestring.md)
  Overrides a line string.
- [itemForMultiLineString](geojsondelegate/itemformultilinestring.md)
  Overrides a multiline string.
- [itemForMultiPoint](geojsondelegate/itemformultipoint.md)
  Overrides a multipoint object.
- [itemForPolygon](geojsondelegate/itemforpolygon.md)
  Overrides a polygon.
- [itemForMultiPolygon](geojsondelegate/itemformultipolygon.md)
  Overrides a multipolygon.
- [styleForOverlay](geojsondelegate/styleforoverlay.md)
  Overrides the style of overlays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/geojsondelegate/itemforpoint)*