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
        callback: (error: Error | null, result?: GeocoderResponse) => void,
        options?: GeocoderLookupOptions,
    ): number;
```

#### Return Value

This method returns a request ID, which is an integer that you can pass to [`cancel(id)`](service/cancel.md) to stop a pending request.

#### Discussion

Geocoding converts a human-readable address to latitude and longitude coordinates. You can use [`Geocoder`](geocoder.md) to look up coordinates for a city, landmark, or address.

## Parameters

- `place`: A case-insensitive string MapKit JS converts to geographic coordinates, such as: “ ”, “ ”, “``San Francisco City Hall, San Francisco, CA USA`”. Delimiter characters are optional.
- `callback`: MapKit JS returns geocoding results asynchronously through a callback function. MapKit JS invokes the callback function with two arguments,   on failure and   on success.
- `options`: The geocoder returns the most relevant results for a query. For example, a query for   returns results for Paris, France. Use   to constrain the search to specific countries, or to a desired area with a coordinate or region.

## See Also

- [interface GeocoderLookupOptions](geocoderlookupoptions.md)
  Options that constrain geocoder lookup results to a specific area or a specific language.
- [reverseLookup(coordinate, callback, options)](geocoder/reverselookup.md)
  Converts a geographic coordinate to an address.
- [interface GeocoderReverseLookupOptions](geocoderreverselookupoptions.md)
  An option that constrains reverse lookup results to a specific language.
- [interface GeocoderResponse](geocoderresponse.md)
  The response from a geocoder lookup or reverse lookup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/geocoder/lookup)*