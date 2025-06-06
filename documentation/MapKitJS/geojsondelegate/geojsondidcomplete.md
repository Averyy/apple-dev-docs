# geoJSONDidComplete

**Framework**: MapKit JS  
**Kind**: method

Completes the GeoJSON import.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
void geoJSONDidComplete(
	ItemCollection result,
	Object geoJSON
);
```

#### Discussion

After MapKit JS loads the GeoJSON data and converts it to MapKit objects, the framework calls [`geoJSONDidComplete`](geojsondelegate/geojsondidcomplete.md) with the resulting [`ItemCollection`](itemcollection.md), which reflects any provided customizations. This is the same value that returns directly from [`importGeoJSON`](mapkit/importgeojson.md) in the synchronous case.

## Parameters

- `result`: The mapped item collection.
- `geoJSON`: The original parsed GeoJSON object.

## See Also

- [geoJSONDidError](geojsondelegate/geojsondiderror.md)
  Indicates when the GeoJSON import fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/geojsondelegate/geojsondidcomplete)*