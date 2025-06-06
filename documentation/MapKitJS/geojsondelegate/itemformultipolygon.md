# itemForMultiPolygon

**Framework**: MapKit JS  
**Kind**: method

Overrides a multipolygon.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
optional(mapkit.Annotation|mapkit.Overlay|(mapkit.Annotation|mapkit.Overlay)[]) itemForMultiPolygon(
	ItemCollection itemCollection,
	Object geoJSON
);
```

#### Return Value

A map item or an array of map items.

#### Discussion

MapKit JS calls this method for every `MultiPolygon` object. The framework also calls this method after constructing subitems, and calling their delegate functions.

## Parameters

- `itemCollection`: A collection containing associated overlays.
- `geoJSON`: The original GeoJSON object for the  . It contains an array of geometries.

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
- [itemForPolygon](geojsondelegate/itemforpolygon.md)
  Overrides a polygon.
- [styleForOverlay](geojsondelegate/styleforoverlay.md)
  Overrides the style of overlays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/geojsondelegate/itemformultipolygon)*