# language

**Framework**: MapKit JS  
**Kind**: property

A language ID that determines the language for the search results text.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
attribute string language;
```

#### Discussion

If you set a language ID, the search returns addresses in the selected language, if available, such as, `fr-CA` or `en-GB`. If you don’t provide a language ID, the search object uses the language ID the system provides to the [`init`](mapkit/init.md) call.

## See Also

- [coordinate](searchconstructoroptions/coordinate.md)
  A map coordinate that provides a hint for the geographic area to search.
- [getsUserLocation](searchconstructoroptions/getsuserlocation.md)
  A Boolean value that indicates whether to limit the search results to the user’s location, according to the web browser.
- [region](searchconstructoroptions/region.md)
  A map region that provides a hint for the geographic area to search.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/searchconstructoroptions/language)*