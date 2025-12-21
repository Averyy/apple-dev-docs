# region

**Framework**: MapKit JS  
**Kind**: property

A region for constraining lookup results.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
region?: CoordinateRegion;
```

#### Discussion

Tell the geocoder to return results in this region. For example, constrain the geocoder to return results in the region currently displayed by the map with `{ region: map.region }`.

## See Also

- [coordinate](geocoderlookupoptions/coordinate.md)
  Coordinates for constraining the lookup results.
- [language](geocoderlookupoptions/language.md)
  The language to use when displaying the lookup results.
- [limitToCountries](geocoderlookupoptions/limittocountries.md)
  A list of countries for constraining the lookup results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/geocoderlookupoptions/region)*