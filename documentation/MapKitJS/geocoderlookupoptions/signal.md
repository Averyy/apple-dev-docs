# signal

**Framework**: MapKit JS  
**Kind**: property

A signal object allowing you to cancel the request.

**Availability**:
- MapKit JS 6.0+

## Declaration

```swift
signal?: AbortSignal;
```

#### Discussion

Pass an `AbortSignal` from an `AbortController` to allow the controller to cancel a pending geocoder lookup request. When the controller aborts, the promise it returns rejects with a `DOMException` whose `name` is `"AbortError"`.

## See Also

- [coordinate](geocoderlookupoptions/coordinate.md)
  Coordinates for constraining the lookup results.
- [language](geocoderlookupoptions/language.md)
  The language to use when displaying the lookup results.
- [limitToCountries](geocoderlookupoptions/limittocountries.md)
  A list of countries for constraining the lookup results.
- [region](geocoderlookupoptions/region.md)
  A region for constraining lookup results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/geocoderlookupoptions/signal)*