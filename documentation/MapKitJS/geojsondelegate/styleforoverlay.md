# styleForOverlay

**Framework**: MapKit JS  
**Kind**: method

Overrides the style of overlays.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
mapkit.Style styleForOverlay(
	mapkit.Overlay overlay,
	Object geoJSON
);
```

#### Return Value

This method returns a [`mapkit.Style`](mapkit.style.md) object for the provided overlay.

#### Discussion

MapKit JS calls this method for each overlay, and after each call to [`itemForPoint`](geojsondelegate/itemforpoint.md) and [`itemForPolygon`](geojsondelegate/itemforpolygon.md).

## Parameters

- `overlay`: The overlay to style.
- `geoJSON`: The original GeoJSON for the   or   object

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
- [itemForMultiPolygon](geojsondelegate/itemformultipolygon.md)
  Overrides a multipolygon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/geojsondelegate/styleforoverlay)*