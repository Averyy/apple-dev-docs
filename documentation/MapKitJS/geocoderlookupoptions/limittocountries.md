# limitToCountries

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Interface Property

A list of countries for constraining the lookup results.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
limitToCountries?: string;
```

## Discussion

This property tells the geocoder to return results within a list of countries. Specify countries in the list using two-letter ISO country codes. For example, constrain the geocoder to return results in Australia and New Zealand with `{ limitToCountries: "AU, NZ" }`.

## See Also

### Options
- [coordinate](./coordinate.md)
  Coordinates for constraining the lookup results.
- [language](./language.md)
  The language to use when displaying the lookup results.
- [region](./region.md)
  A region for constraining lookup results.
- [signal](./signal.md)
  A signal object allowing you to cancel the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/geocoderlookupoptions/limittocountries)*