# lookup

**Framework**: MapKit JS  
**Kind**: method

Converts an address to geographic coordinates.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
number lookup(
	string place,
	function callback,
	optional GeocoderLookupOptions options
);
```

#### Return Value

This method returns a request ID, which is an integer that you can pass to [`cancel`](mapkit.geocoder/cancel.md) to stop a pending request.

#### Discussion

Geocoding converts a human-readable address to latitude and longitude coordinates. You can use [`mapkit.Geocoder`](mapkit.geocoder/mapkit.geocoder.md) to look up coordinates for a city, landmark, or address.

## Parameters

- `place`: A case-insensitive string MapKit JS converts to geographic coordinates, such as: “ ”, “ ”, “ ”. Delimiter characters are optional.
- `callback`: MapKit JS returns geocoding results asynchronously through a callback function. MapKit JS invokes the callback function with two arguments,   on failure and   on success.
- `options`: The geocoder returns the most relevant results for a query. For example, a query for   returns results for Paris, France. Use   to constrain the search to specific countries, or to a desired area with a coordinate or region.

## See Also

- [GeocoderLookupOptions](geocoderlookupoptions.md)
  Options that constrain geocoder lookup results to a specific area or a specific language.
- [reverseLookup](mapkit.geocoder/reverselookup.md)
  Converts a geographic coordinate to an address.
- [GeocoderReverseLookupOptions](geocoderreverselookupoptions.md)
  An option that constrains reverse lookup results to a specific language.
- [GeocoderResponse](geocoderresponse.md)
  The response from a geocoder lookup or reverse lookup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.geocoder/lookup)*