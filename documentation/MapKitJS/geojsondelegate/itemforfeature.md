# itemForFeature

**Framework**: MapKit JS  
**Kind**: method

Overrides a feature.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
optional(mapkit.Annotation|mapkit.Overlay|(mapkit.Annotation|mapkit.Overlay)[]) itemForFeature();
```

#### Return Value

A map item for the `feature`.

#### Discussion

MapKit JS calls this method for every GeoJSON `feature`.

## Parameters

- `item`: An item the system creates for the geometry of the feature, or   for features with   geometry.
- `geoJSON`: The original GeoJSON object for the  .

## See Also

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
- [itemForMultiPolygon](geojsondelegate/itemformultipolygon.md)
  Overrides a multipolygon.
- [styleForOverlay](geojsondelegate/styleforoverlay.md)
  Overrides the style of overlays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/geojsondelegate/itemforfeature)*