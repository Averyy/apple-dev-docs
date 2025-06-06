# results

**Framework**: MapKit JS  
**Kind**: property

An array of places that returns from a geocoder lookup or reverse lookup.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
attribute Place[] results;
```

#### Discussion

An object the system parses from the geocoder JSON response, which contains an array of places. Each [`Place`](place.md) has several properties.

If there’s no response, [`results`](geocoderresponse/results.md) is an empty array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/geocoderresponse/results)*