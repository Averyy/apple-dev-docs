# region

**Framework**: MapKit JS  
**Kind**: property

A map region that provides a hint for the geographic area to search.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
region?: CoordinateRegion;
```

#### Discussion

This property specifies a region of a map in which to search. In a map application, this is typically the region displayed in the map.

```javascript
{ region: map.region }
```

## See Also

- [coordinate](searchconstructoroptions/coordinate.md)
  A map coordinate that provides a hint for the geographic area to search.
- [getsUserLocation](serviceconstructoroptions/getsuserlocation.md)
  A Boolean value that indicates whether to limit the results to the user’s location, according to the web browser.
- [language](serviceconstructoroptions/language.md)
  A language identifier that determines the language for the service results text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/searchconstructoroptions/region)*