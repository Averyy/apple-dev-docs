# geoJSONDidError(error, geoJSON)

**Framework**: MapKit JS  
**Kind**: method  
**Role**: Interface Method

Indicates when the GeoJSON import fails.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
geoJSONDidError?(
    error: GeoJSONImportError | Error,
    geoJSON?: GeoJSONTypes.GeoJSON,
): void;
```

#### Discussion

MapKit JS calls this method when the GeoJSON fails to load.

## Parameters

- `error`: An `Error` instance related to the last blocking error.
- `geoJSON`: The original parsed GeoJSON object.

## See Also

### Handling errors and completion
- [geoJSONDidComplete(result, geoJSON)](./geojsondidcomplete.md)
  Completes the GeoJSON import.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/geojsondelegate/geojsondiderror)*