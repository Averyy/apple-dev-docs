# coordinate

**Framework**: MapKit JS  
**Kind**: property

Coordinates for constraining the lookup results.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
coordinate?: Coordinate;
```

#### Discussion

Tell the geocoder to return results around this coordinate. For example, constrain the geocoder to return results around the coordinate 37.37, -122.04 with `{ coordinate: new mapkit.Coordinate(37.37, -122.04) }`.

## See Also

- [language](geocoderlookupoptions/language.md)
  The language to use when displaying the lookup results.
- [limitToCountries](geocoderlookupoptions/limittocountries.md)
  A list of countries for constraining the lookup results.
- [region](geocoderlookupoptions/region.md)
  A region for constraining lookup results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/geocoderlookupoptions/coordinate)*