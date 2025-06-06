# itemForFeatureCollection

**Framework**: MapKit JS  
**Kind**: method

Overrides a feature collection.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
optional(mapkit.Annotation|mapkit.Overlay|(mapkit.Annotation|mapkit.Overlay)[]) itemForFeatureCollection(
	ItemCollection itemCollection,
	Object geoJSON
);
```

#### Return Value

A map item or an array of map items.

#### Discussion

MapKit JS calls this method for every GeoJSON `FeatureCollection` object. The framework also calls this method after constructing subitems and calling their delegate functions.

## Parameters

- `itemCollection`: A collection containing associated annotations and overlays.
- `geoJSON`: The original GeoJSON object for the  . This contains an array of   types.

## See Also

- [itemForFeature](geojsondelegate/itemforfeature.md)
  Overrides a feature.
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

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/geojsondelegate/itemforfeaturecollection)*