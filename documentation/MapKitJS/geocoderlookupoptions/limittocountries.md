# limitToCountries

**Framework**: MapKit JS  
**Kind**: property

A list of countries for constraining the lookup results.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
attribute string limitToCountries;
```

#### Discussion

This property tells the geocoder to return results within a list of countries. Specify countries in the list using two-letter ISO country codes. For example, constrain the geocoder to return results in Australia and New Zealand with `{ limitToCountries: "AU, NZ" }`.

## See Also

- [coordinate](geocoderlookupoptions/coordinate.md)
  Coordinates for constraining the lookup results.
- [language](geocoderlookupoptions/language.md)
  The language to use when displaying the lookup results.
- [region](geocoderlookupoptions/region.md)
  A region for constraining lookup results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/geocoderlookupoptions/limittocountries)*