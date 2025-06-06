# importGeoJSON

**Framework**: MapKit JS  
**Kind**: method

Converts imported GeoJSON data to MapKit JS items.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
ItemCollection|Error importGeoJSON(
	string|Object data,
	optional function|GeoJSONDelegate callback
);
```

## Mentions

- [MapKit JS 5](mapkit-js-5.md)

#### Return Value

If the data argument is a GeoJSON object instead of a URL and you don’t provide a `callback` function, [`importGeoJSON`](mapkit/importgeojson.md) returns an [`ItemCollection`](itemcollection.md). If the data import fails, this method returns an error.

#### Discussion

This function converts imported GeoJSON data into MapKit JS items, which are [`annotations`](mapkit.map/annotations.md), [`overlays`](mapkit.map/overlays.md), and [`ItemCollection`](itemcollection.md) objects. Access the original GeoJSON data through the object’s [`data`](itemcollection/data.md) property.

You can customize the import by implementing a [`GeoJSONDelegate`](geojsondelegate.md) callback:

- If you provide a GeoJSON object for the `data` parameter, [`importGeoJSON`](mapkit/importgeojson.md) returns the result directly. However, the system uses the optional callback, if you provide it.
- If you provide a URL to a GeoJSON file in the `data` parameter, you need to provide a callback function.

MapKit JS invokes this callback with two arguments, `error` on failure and `result` on success, as follows:

> **Note**:  GeoJSON is a format that encodes geographic data. See the GeoJSON standard specification [`RFC 7946`](https://developer.apple.comhttps://tools.ietf.org/html/rfc7946) for more information.

 GeoJSON is a format that encodes geographic data. See the GeoJSON standard specification [`RFC 7946`](https://developer.apple.comhttps://tools.ietf.org/html/rfc7946) for more information.

## Parameters

- `data`: The original GeoJSON data, either a URL to a GeoJSON file, or a GeoJSON object.
- `callback`: A callback function that MapKit JS requires if you provide a URL for the   parameter. It’s optional, otherwise.

## See Also

- [GeoJSONDelegate](geojsondelegate.md)
  A delegate object that controls a GeoJSON import to override default behavior and provide custom style.
- [ItemCollection](itemcollection.md)
  A tree structure containing annotations, overlays, and nested item collection objects.
- [Displaying Indoor Maps with MapKit JS](displaying-indoor-maps-with-mapkit-js.md)
  Use the Indoor Mapping Data Format (IMDF) to show an indoor map with custom overlays and points of interest in your browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit/importgeojson)*