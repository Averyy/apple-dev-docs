# GeocoderResponse

**Framework**: MapKit JS  
**Kind**: struct

The response from a geocoder lookup or reverse lookup.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
dictionary GeocoderResponse {
	Place[] results;
};
```

## Mentions

- [MapKit JS 5](mapkit-js-5.md)

#### Overview

The `data` parameter of the [`lookup`](mapkit.geocoder/lookup.md) or [`reverseLookup`](mapkit.geocoder/reverselookup.md) callback function contains the geocoder response. MapKit JS parses the `data` object from the geocoder JSON response, which contains an array of [`Place`](place.md) objects.

If there’s no response, [`results`](geocoderresponse/results.md) is an empty array.

## Topics

### Response
- [results](geocoderresponse/results.md)
  An array of places that returns from a geocoder lookup or reverse lookup.

## See Also

- [lookup](mapkit.geocoder/lookup.md)
  Converts an address to geographic coordinates.
- [GeocoderLookupOptions](geocoderlookupoptions.md)
  Options that constrain geocoder lookup results to a specific area or a specific language.
- [reverseLookup](mapkit.geocoder/reverselookup.md)
  Converts a geographic coordinate to an address.
- [GeocoderReverseLookupOptions](geocoderreverselookupoptions.md)
  An option that constrains reverse lookup results to a specific language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/geocoderresponse)*