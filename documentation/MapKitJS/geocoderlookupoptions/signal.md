# signal

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Interface Property

A signal object allowing you to cancel the request.

**Availability**:
- MapKit JS 6.0+

## Declaration

```
signal?: AbortSignal;
```

## Discussion

Pass an `AbortSignal` from an `AbortController` to allow the controller to cancel a pending geocoder lookup request. When the controller aborts, the promise it returns rejects with a `DOMException` whose `name` is `"AbortError"`.

## See Also

### Options
- [coordinate](./coordinate.md)
  Coordinates for constraining the lookup results.
- [language](./language.md)
  The language to use when displaying the lookup results.
- [limitToCountries](./limittocountries.md)
  A list of countries for constraining the lookup results.
- [region](./region.md)
  A region for constraining lookup results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/geocoderlookupoptions/signal)*