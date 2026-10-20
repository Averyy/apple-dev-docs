# getsUserLocation

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Interface Property

A Boolean value that indicates whether to limit the results to the user’s location, according to the web browser.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
getsUserLocation?: boolean;
```

#### Discussion

If you set this value to `true`, the request queries the browser for the user’s location to deliver relevant local results. The default value is `false`.

This value may not have an effect on some services.

## See Also

### Search Initialization
- [coordinate](../searchconstructoroptions/coordinate.md)
  A map coordinate that provides a hint for the geographic area to search.
- [language](./language.md)
  A language identifier that determines the language for the service results text.
- [region](../searchconstructoroptions/region.md)
  A map region that provides a hint for the geographic area to search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/serviceconstructoroptions/getsuserlocation)*