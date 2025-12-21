# Displaying Indoor Maps with MapKit JS

**Framework**: MapKit JS

Use the Indoor Mapping Data Format (IMDF) to show an indoor map with custom overlays and points of interest in your browser.

#### Overview

This sample uses the [`importGeoJSON(data, callback)`](mapkit/importgeojson.md) method from MapKit JS to import data in [`Indoor Mapping Data Format (IMDF)`](https://developer.apple.comhttps://register.apple.com/resources/imdf/), and render an indoor map in your browser. The sample app demonstrates decoding, rendering, and styling of a small subset of the IMDF feature types and properties.

Use these examples to create your own indoor map with a style that is consistent with your app’s design. You can handle feature categories specific to your venue, and configure the map style using your own colors, icons, and level picker.

> **Note**: This sample code project is associated with WWDC 2019 session [`241: Adding Indoor Maps to your App and Website`](https://developer.apple.comhttps://developer.apple.com/wwdc19/241).

##### Configure Your Sample Code Project

To run this sample code:

- Run a web server to serve the assets in a directory for the project.
- Host the directory `Dinoseum`, and its content, at the root of your web server.
- Generate a MapKit JS token and copy it into the `jwtoken` file within the `Dinoseum` directory. For more information, see [`Creating and using tokens with Maps Server API`](https://developer.apple.com/documentation/AppleMapsServerAPI/creating-and-using-tokens-with-maps-server-api).

## See Also

- [importGeoJSON(data, callback)](mapkit/importgeojson.md)
  Converts imported GeoJSON data to MapKit JS compatible items.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/displaying-indoor-maps-with-mapkit-js)*