# lookup(place, options)

**Framework**: MapKit JS  
**Kind**: method

Converts an address to geographic coordinates.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
lookup(
    place: string,
    options?: GeocoderLookupOptions,
): Promise<GeocoderResponse>;
```

#### Return Value

A promise that resolves with a [`GeocoderResponse`](geocoderresponse.md) on success, or rejects with an `Error` on failure.

#### Discussion

Geocoding converts a human-readable address to latitude and longitude coordinates. You can use [`Geocoder`](geocoder.md) to look up coordinates for a city, landmark, or address.

The resolved [`GeocoderResponse`](geocoderresponse.md) contains an array of places named [`results`](geocoderresponse/results.md). Each place in [`results`](geocoderresponse/results.md) has a [`coordinate`](place/coordinate.md) property and a [`formattedAddress`](place/formattedaddress.md) property. [`results`](geocoderresponse/results.md) is an empty array if there isn’t a match.

Pass an `AbortSignal` from an `AbortController` to the [`signal`](geocoderlookupoptions/signal.md) option to allow the controller to cancel a pending request. When the controller aborts, the promise it returns rejects with a `DOMException` whose `name` is `"AbortError"`.

## Parameters

- `place`: A case-insensitive string MapKit JS converts to geographic coordinates, such as: “`San Francisco City Hall`”, “`San Francisco City Hall, San Francisco`”, “`San Francisco City Hall, San Francisco, CA USA`”. Delimiter characters are optional.
- `options`: Options that constrain geocoder lookup results to a specific area or a specific language. See [`GeocoderLookupOptions`](geocoderlookupoptions.md).

## See Also

- [interface GeocoderLookupOptions](geocoderlookupoptions.md)
  Options that constrain geocoder lookup results to a specific area or a specific language.
- [reverseLookup(coordinate, options)](geocoder/reverselookup.md)
  Converts a geographic coordinate to an address.
- [interface GeocoderReverseLookupOptions](geocoderreverselookupoptions.md)
  An option that constrains reverse lookup results to a specific language.
- [interface GeocoderResponse](geocoderresponse.md)
  The response from a geocoder lookup or reverse lookup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/geocoder/lookup)*