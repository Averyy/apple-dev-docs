# reverseLookup(coordinate, callback, options)

**Framework**: MapKit JS  
**Kind**: method

Converts a geographic coordinate to an address.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
reverseLookup(
        coordinate: Coordinate,
        callback: (error: Error | null, result?: GeocoderResponse) => void,
        options?: GeocoderReverseLookupOptions,
    ): number;
```

#### Return Value

A request ID that you can pass to [`cancel(id)`](service/cancel.md) to stop a pending request.

#### Discussion

Reverse geocoding converts geographic coordinates to the nearest human-readable address.

## Parameters

- `coordinate`: The coordinate to convert to a human-readable address. For example,   ``Coordinate```(37.779268, -122.419248)`, which represents San Francisco City Hall.
- `callback`: MapKit JS invokes this callback function with two arguments,   on failure and   on success. If you cancel the request before you receive a response, the framework doesn’t call this function.
- `options`:   is the only option that you can set for the reverse geocoder. For example,   tells the server to send results localized to Canadian French. If you set it, this option overrides the language you provide in the   constructor.

## Topics

- [interface GeocoderReverseLookupOptions](geocoderreverselookupoptions.md)
  An option that constrains reverse lookup results to a specific language.

## See Also

- [lookup(place, callback, options)](geocoder/lookup.md)
  Converts an address to geographic coordinates.
- [interface GeocoderLookupOptions](geocoderlookupoptions.md)
  Options that constrain geocoder lookup results to a specific area or a specific language.
- [interface GeocoderReverseLookupOptions](geocoderreverselookupoptions.md)
  An option that constrains reverse lookup results to a specific language.
- [interface GeocoderResponse](geocoderresponse.md)
  The response from a geocoder lookup or reverse lookup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/geocoder/reverselookup)*