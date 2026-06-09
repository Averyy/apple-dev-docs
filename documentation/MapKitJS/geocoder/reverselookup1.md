# reverseLookup(coordinate, callback, options)

**Framework**: MapKit JS  
**Kind**: method

Converts a geographic coordinate to an address.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
reverseLookup(
    coordinate: CoordinateData,
    callback: (
        error: Error | null,
        result: GeocoderResponse | null,
    ) => void,
    options?: GeocoderReverseLookupOptions,
): Promise<GeocoderResponse>;
```

#### Return Value

A promise that resolves with a [`GeocoderResponse`](geocoderresponse.md) on success.

#### Discussion

Reverse geocoding converts geographic coordinates to the nearest human-readable address.

## Parameters

- `coordinate`: The coordinate to convert to a human-readable address. For example, `new` ``Coordinate```(37.779268, -122.419248)`, which represents San Francisco City Hall.
- `callback`: MapKit JS invokes this callback function with two arguments, `error` on failure and `data` on success. If you cancel the request before you receive a response, the framework doesn’t call this function. - `error` (`Error`). Contains an error code and descriptive message.
- `data` ([`GeocoderResponse`](geocoderresponse.md)). An object that contains an array of places named [`results`](geocoderresponse/results.md).
- `options`: [`language`](geocoderreverselookupoptions/language.md) is the only option that you can set for the reverse geocoder. For example, `{ language: 'fr-CA' }` tells the server to send results localized to Canadian French. If you set it, this option overrides the language you provide in the [`Geocoder`](geocoder.md) constructor.

## Topics

- [interface GeocoderReverseLookupOptions](geocoderreverselookupoptions.md)
  An option that constrains reverse lookup results to a specific language.

## See Also

- [lookup(place, callback, options)](geocoder/lookup1.md)
  Converts an address to geographic coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/geocoder/reverselookup1)*