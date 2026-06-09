# lookup(place, callback, options)

**Framework**: MapKit JS  
**Kind**: method

Converts an address to geographic coordinates.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
lookup(
    place: string,
    callback: (
        error: Error | null,
        result: GeocoderResponse | null,
    ) => void,
    options?: GeocoderLookupOptions,
): Promise<GeocoderResponse>;
```

#### Return Value

A promise that resolves with a [`GeocoderResponse`](geocoderresponse.md) on success.

#### Discussion

Geocoding converts a human-readable address to latitude and longitude coordinates. You can use [`Geocoder`](geocoder.md) to look up coordinates for a city, landmark, or address.

## Parameters

- `place`: A case-insensitive string MapKit JS converts to geographic coordinates, such as: “`San Francisco City Hall`”, “`San Francisco City Hall, San Francisco`”, “`San Francisco City Hall, San Francisco, CA USA`”. Delimiter characters are optional.
- `callback`: MapKit JS returns geocoding results asynchronously through a callback function. MapKit JS invokes the callback function with two arguments, `error` on failure and `data` on success. - `error` (`Error`). Contains an error code and descriptive message.
- `data` ([`GeocoderResponse`](geocoderresponse.md)). An object that contains an array of places named [`results`](geocoderresponse/results.md).
- `options`: The geocoder returns the most relevant results for a query. For example, a query for *Paris* returns results for Paris, France. Use [`GeocoderLookupOptions`](geocoderlookupoptions.md) to constrain the search to specific countries, or to a desired area with a coordinate or region.

## See Also

- [reverseLookup(coordinate, callback, options)](geocoder/reverselookup1.md)
  Converts a geographic coordinate to an address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/geocoder/lookup1)*