# DirectionsAvoid

**Framework**: Apple Maps Server API  
**Kind**: typealias

A list of the features you can request to avoid when calculating directions.

**Availability**:
- Apple Maps Server API 1.2+

## Declaration

```swift
string DirectionsAvoid
```

#### Possible Values

- **Tolls**: When you set `avoid=Tolls`, routes without tolls are higher up in the list of returned routes. Note that even when you set `avoid=Tolls`, the routes the server returns may contain tolls (if no reasonable toll-free routes exist). Ensure you check the value of `routes[i].hasTolls` in the response to verify toll assumptions.

## See Also

- [type CountryCode](countrycode.md)
  A string that represents a two-letter country code.
- [type Lang](lang.md)
  A string that represents a standard tag for identifying languages.
- [type PoiCategory](poicategory.md)
  A string that describes a specific point of interest (POI) category.
- [type SearchLocation](searchlocation.md)
  A string that describes a geographic location in the form of longitude and latitude.
- [type SearchRegion](searchregion.md)
  A string that describes a region to search in terms of its upper-right and lower-left corners as a pair of geographic points.
- [type UserLocation](userlocation.md)
  A string that describes the user’s location in terms of longitude and latitude.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemapsserverapi/directionsavoid)*