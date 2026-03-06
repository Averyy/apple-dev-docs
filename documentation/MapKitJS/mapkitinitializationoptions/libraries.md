# libraries

**Framework**: MapKit JS  
**Kind**: property

An array of libraries to load at initialization.

**Availability**:
- MapKit JS 5.75+

## Declaration

```swift
libraries?: string[];
```

#### Discussion

> **Note**:  The full bundle of MapKit JS ignores this option.

MapKit JS divides its interfaces into libraries that you can specify when loading the framework. To optimize your app load time, pick only the interfaces you need:

- **`services`**: All services interfaces (such as Search and Geocoder) and relevant data types.
- **`full-map`**: All `mapkit.Map` features and relevant data types.
- **`map`**: Basic `mapkit.Map` features without overlays, annotations, and relevant data types.
- **`overlays`**: Overlays, data types, and displays on [`Map`](map.md).
- **`annotations`**: Annotations, data types, and displays on [`Map`](map.md).
- **`geojson`**: The GeoJSON importer.
- **`user-location`**: User location display and controls on [`Map`](map.md).
- **`look-around`**: [`LookAround`](lookaround.md) and [`LookAroundPreview`](lookaroundpreview.md).

You can set the libraries to load statically by defining them within script tag in the `data-libraries` attribute or in the [`load(libraryNames)`](mapkit/load.md) method, or by passing a `libraries` property in the [`init(options)`](mapkit/init.md) options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkitinitializationoptions/libraries)*