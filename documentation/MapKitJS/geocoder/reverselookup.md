# reverseLookup(coordinate, options)

**Framework**: MapKit JS  
**Kind**: method

Converts a geographic coordinate to an address.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
reverseLookup(
    coordinate: Coordinate,
    options?: GeocoderReverseLookupOptions,
): Promise<GeocoderResponse>;
```

#### Return Value

A promise that resolves with a [`GeocoderResponse`](geocoderresponse.md) on success, or rejects with an `Error` on failure.

#### Discussion

Reverse geocoding converts geographic coordinates to the nearest human-readable address.

The resolved [`GeocoderResponse`](geocoderresponse.md) contains an array of places named [`results`](geocoderresponse/results.md). Each place in [`results`](geocoderresponse/results.md) has a [`coordinate`](place/coordinate.md) property and a [`formattedAddress`](place/formattedaddress.md) property. [`results`](geocoderresponse/results.md) is an empty array if there isn’t a match.

Pass an `AbortSignal` from an `AbortController` to the [`signal`](geocoderreverselookupoptions/signal.md) option to allow the controller to cancel a pending request. When the controller aborts, the promise it returns rejects with a `DOMException` whose `name` is `"AbortError"`.

## Parameters

- `coordinate`: The coordinate to convert to a human-readable address. For example, `new` ``Coordinate```(37.779268, -122.419248)`, which represents San Francisco City Hall.
- `options`: An option that constrains reverse lookup results to a specific language. See [`GeocoderReverseLookupOptions`](geocoderreverselookupoptions.md).

## Topics

- [interface GeocoderReverseLookupOptions](geocoderreverselookupoptions.md)
  An option that constrains reverse lookup results to a specific language.

## See Also

- [lookup(place, options)](geocoder/lookup.md)
  Converts an address to geographic coordinates.
- [interface GeocoderLookupOptions](geocoderlookupoptions.md)
  Options that constrain geocoder lookup results to a specific area or a specific language.
- [interface GeocoderReverseLookupOptions](geocoderreverselookupoptions.md)
  An option that constrains reverse lookup results to a specific language.
- [interface GeocoderResponse](geocoderresponse.md)
  The response from a geocoder lookup or reverse lookup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/geocoder/reverselookup)*