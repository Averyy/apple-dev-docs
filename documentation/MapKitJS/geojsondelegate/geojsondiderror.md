# geoJSONDidError

**Framework**: MapKit JS  
**Kind**: method

Indicates when the GeoJSON import fails.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
void geoJSONDidError(
	Error error,
	Object geoJSON
);
```

#### Discussion

MapKit JS calls this method when the GeoJSON fails to load.

## Parameters

- `error`: An   instance related to the last blocking error.
- `geoJSON`: The original parsed GeoJSON object.

## See Also

- [geoJSONDidComplete](geojsondelegate/geojsondidcomplete.md)
  Completes the GeoJSON import.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/geojsondelegate/geojsondiderror)*