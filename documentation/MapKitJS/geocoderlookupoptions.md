# GeocoderLookupOptions

**Framework**: MapKit JS  
**Kind**: struct

Options that constrain geocoder lookup results to a specific area or a specific language.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
interface GeocoderLookupOptions
```

#### Overview

Configure [`GeocoderLookupOptions`](geocoderlookupoptions.md) when performing a [`lookup(place, callback, options)`](geocoder/lookup.md) to constrain geocoder results to a specific area or return results in a specific language.

## Topics

### Options
- [coordinate](geocoderlookupoptions/coordinate.md)
  Coordinates for constraining the lookup results.
- [language](geocoderlookupoptions/language.md)
  The language to use when displaying the lookup results.
- [limitToCountries](geocoderlookupoptions/limittocountries.md)
  A list of countries for constraining the lookup results.
- [region](geocoderlookupoptions/region.md)
  A region for constraining lookup results.

## See Also

- [lookup(place, callback, options)](geocoder/lookup.md)
  Converts an address to geographic coordinates.
- [reverseLookup(coordinate, callback, options)](geocoder/reverselookup.md)
  Converts a geographic coordinate to an address.
- [interface GeocoderReverseLookupOptions](geocoderreverselookupoptions.md)
  An option that constrains reverse lookup results to a specific language.
- [interface GeocoderResponse](geocoderresponse.md)
  The response from a geocoder lookup or reverse lookup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/geocoderlookupoptions)*