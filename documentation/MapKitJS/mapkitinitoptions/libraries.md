# libraries

**Framework**: MapKit JS  
**Kind**: property

An array of libraries to load at initialization.

**Availability**:
- MapKit JS 5.73+

## Declaration

```swift
attribute string[] libraries;
```

#### Discussion

> **Note**:  The full bundle of MapKit JS ignores this option.

MapKit JS divides its interfaces into libraries that you can specify when loading the framework. To optimize your app load time, pick only the interfaces you need:

- `services` — All services interfaces (such as Search and Geocoder) and relevant data types.
- `full-map` — All `mapkit.Map` features and relevant data types.
- `map` — Basic `mapkit.Map` features without overlays, annotations, and relevant data types.
- `overlays` — Overlays, data types, and displays on `mapkit.Map`.
- `annotations` — Annotations, data types, and displays on `mapkit.Map`.
- `geojson` — The GeoJSON importer.
- `user-location` — User location display and controls on `mapkit.Map`.

You can set the libraries to load statically by defining them within script tag in the `data-libraries` attribute or in the [`load`](mapkit/load.md) method, or by passing a `libraries` property in the [`init`](mapkit/init.md) options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkitinitoptions/libraries)*