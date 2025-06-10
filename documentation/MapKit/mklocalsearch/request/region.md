# region

**Framework**: MapKit  
**Kind**: property

A map region that provides a hint as to where to search.

**Availability**:
- iOS 6.1+
- iPadOS 6.1+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
var region: MKCoordinateRegion { get set }
```

#### Discussion

You can use this parameter to narrow the list of search results to those inside or close to the specified region. Specifying a region doesn’t ensure that the results are all inside the region. It’s merely a hint to the search engine.

## See Also

- [var addressFilter: MKAddressFilter?](mklocalsearch/request/addressfilter.md)
  A filter that lists which address options to include or exclude in search results.
- [var naturalLanguageQuery: String?](mklocalsearch/request/naturallanguagequery.md)
  A string containing the desired search item.
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

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklocalsearch/request/region)*