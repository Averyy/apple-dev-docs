# coordinate

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Interface Property

Coordinates for constraining the lookup results.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
coordinate?: CoordinateData;
```

#### Discussion

Tell the geocoder to return results around this coordinate. For example, constrain the geocoder to return results around the coordinate 37.37, -122.04 with `{ coordinate: new mapkit.Coordinate(37.37, -122.04) }`.

## See Also

### Options
- [language](./language.md)
  The language to use when displaying the lookup results.
- [limitToCountries](./limittocountries.md)
  A list of countries for constraining the lookup results.
- [region](./region.md)
  A region for constraining lookup results.
- [signal](./signal.md)
  A signal object allowing you to cancel the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/geocoderlookupoptions/coordinate)*