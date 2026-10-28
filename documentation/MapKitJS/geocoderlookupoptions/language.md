# language

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Interface Property

The language to use when displaying the lookup results.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
language?: string;
```

## Discussion

Tell the geocoder to return results in this language. For example, setting the option `{ language: 'fr-CA' }` tells the server to send results localized to Canadian French. If you set it, this option overrides the language you provide in the [`Geocoder`](../geocoder.md) constructor.

## See Also

### Options
- [coordinate](./coordinate.md)
  Coordinates for constraining the lookup results.
- [limitToCountries](./limittocountries.md)
  A list of countries for constraining the lookup results.
- [region](./region.md)
  A region for constraining lookup results.
- [signal](./signal.md)
  A signal object allowing you to cancel the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/geocoderlookupoptions/language)*