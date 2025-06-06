# naturalLanguageQuery

**Framework**: MapKit  
**Kind**: property

A string containing the desired search item.

**Availability**:
- iOS 6.1+
- iPadOS 6.1+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
var naturalLanguageQuery: String? { get set }
```

#### Discussion

You specify this parameter as a string describing the map-based item you want to look for. The text is equivalent to what the user would type in a search field in the Maps app. For example, the text might contain all or part of an address or it might contain the name of a point of interest.

## See Also

- [var addressFilter: MKAddressFilter?](mklocalsearch/request/addressfilter.md)
  A filter that lists which address options to include or exclude in search results.
- [var region: MKCoordinateRegion](mklocalsearch/request/region.md)
  A map region that provides a hint as to where to search.
- [static var physicalFeature: MKLocalSearch.ResultType](mklocalsearch/resulttype/physicalfeature.md)
  A value that indicates that search results include physical features.
- [var pointOfInterestFilter: MKPointOfInterestFilter?](mklocalsearch/request/pointofinterestfilter.md)
  A filter that lists point-of-interest categories to include or exclude in search results.
- [var regionPriority: MKLocalSearchRegionPriority](mklocalsearch/request/regionpriority.md)
  A value that indicates the importance of the configured region.
- [var resultTypes: MKLocalSearch.ResultType](mklocalsearch/request/resulttypes.md)
  The types of items to include in the search results.
- [MKLocalSearch.Request.ResultType](mklocalsearch/request/resulttype.md)
  Options that indicate types of search results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklocalsearch/request/naturallanguagequery)*