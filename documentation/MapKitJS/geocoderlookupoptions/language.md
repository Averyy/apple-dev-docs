# language

**Framework**: MapKit JS  
**Kind**: property

The language to use when displaying the lookup results.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
attribute string language;
```

#### Discussion

Tell the geocoder to return results in this language. For example, setting the option `{ language: 'fr-CA' }` tells the server to send results localized to Canadian French. If you set it, this option overrides the language you provide in the [`mapkit.Geocoder`](mapkit.geocoder/mapkit.geocoder.md) constructor.

## See Also

- [coordinate](geocoderlookupoptions/coordinate.md)
  Coordinates for constraining the lookup results.
- [limitToCountries](geocoderlookupoptions/limittocountries.md)
  A list of countries for constraining the lookup results.
- [region](geocoderlookupoptions/region.md)
  A region for constraining lookup results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/geocoderlookupoptions/language)*