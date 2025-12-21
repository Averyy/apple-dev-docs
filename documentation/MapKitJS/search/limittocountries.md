# limitToCountries

**Framework**: MapKit JS  
**Kind**: property

A string that constrains search results to be within the provided countries.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
get limitToCountries(): string | null;
set limitToCountries(value: string | null);
```

#### Discussion

The string is a comma-separated list of two-digit ISO 3166-2 country and region codes. For example, to limit search results to Germany, Belgium, and France specify `de,be,fr`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/search/limittocountries)*