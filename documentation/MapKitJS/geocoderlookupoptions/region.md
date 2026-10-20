# region

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Interface Property

A region for constraining lookup results.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
region?: CoordinateRegionData;
```

#### Discussion

Tell the geocoder to return results in this region. For example, constrain the geocoder to return results in the region currently displayed by the map with `{ region: map.region }`.

## See Also

### Options
- [coordinate](./coordinate.md)
  Coordinates for constraining the lookup results.
- [language](./language.md)
  The language to use when displaying the lookup results.
- [limitToCountries](./limittocountries.md)
  A list of countries for constraining the lookup results.
- [signal](./signal.md)
  A signal object allowing you to cancel the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/geocoderlookupoptions/region)*