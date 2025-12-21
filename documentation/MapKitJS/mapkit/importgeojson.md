# importGeoJSON(data, callback)

**Framework**: MapKit JS  
**Kind**: method

Converts imported GeoJSON data to MapKit JS compatible items.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
importGeoJSON(
        data: string | GeoJSONTypes.GeoJSON,
        callback?: GeoJSONDelegate | GeoJSONImporterCallback,
    ):
        | ItemCollection<
              GeoJSONTypes.GeoJSON<
                  GeoJSONTypes.Geometry,
                  GeoJSONTypes.GeoJsonProperties
              >
          >
        | undefined;
```

## Mentions

- [MapKit JS 5](mapkit-js-5.md)

#### Return Value

If the data argument is a GeoJSON object instead of a URL and you don’t provide a `callback` function, [`importGeoJSON(data, callback)`](mapkit/importgeojson.md) returns an [`ItemCollection`](itemcollection.md). If the data import fails, this method returns an error.

#### Discussion

> **Note**:  You must load the `geojson` library first before accessing the method, otherwise, the method throws an `Error`.

This function converts imported GeoJSON data into MapKit JS items, which are [`Annotation`](mapkit/annotation.md), [`Overlay`](overlay.md), and [`ItemCollection`](itemcollection.md) objects. Access the original GeoJSON data through the object’s [`data`](itemcollection/data.md) property.

You can customize the import by implementing a [`GeoJSONDelegate`](geojsondelegate.md) delegate:

- If you provide a GeoJSON object for the `data` parameter, [`importGeoJSON(data, callback)`](mapkit/importgeojson.md) returns the result directly. However, the system uses the optional callback, if you provide it.
- If you provide a URL to a GeoJSON file in the `data` parameter, you need to provide a callback function or delegate object.

> **Note**:  GeoJSON is a format that encodes geographic data. See the GeoJSON standard specification [`RFC 7946`](https://developer.apple.comhttps://tools.ietf.org/html/rfc7946) for more information.

## Parameters

- `data`: The original GeoJSON data, either a URL to a GeoJSON file, or a GeoJSON object.
- `callback`: A callback function or an object that MapKit JS requires if you provide a URL for the   parameter. It’s optional, otherwise.

## See Also

- [interface GeoJSONDelegate](geojsondelegate.md)
  A delegate object that controls a GeoJSON import to override default behavior and provide custom style.
- [type Item](item.md)
  A type alias that represents all objects that the framework sets in an item collection.
- [class ItemCollection](itemcollection.md)
  A tree structure containing annotations, overlays, and nested item collection objects.
- [type GeoJSONImporterCallback](geojsonimportercallback.md)
  A callback function that MapKit JS invokes when importing a GeoJSON object.
- [class GeoJSONImportError](geojsonimporterror.md)
  An error object that indicates an error occurred while importing a GeoJSON object.
- [Displaying Indoor Maps with MapKit JS](displaying-indoor-maps-with-mapkit-js.md)
  Use the Indoor Mapping Data Format (IMDF) to show an indoor map with custom overlays and points of interest in your browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit/importgeojson)*