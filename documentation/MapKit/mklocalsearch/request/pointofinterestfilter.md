# pointOfInterestFilter

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

A filter that lists point-of-interest categories to include or exclude in search results.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@NSCopying
var pointOfInterestFilter: MKPointOfInterestFilter? { get set }
```

```objc
@property (nonatomic, copy, nullable) MKPointOfInterestFilter * pointOfInterestFilter;
```

## See Also

### Configuring the search parameters
- [var addressFilter: MKAddressFilter?](./addressfilter.md)
  A filter that lists which address options to include or exclude in search results.
- [var naturalLanguageQuery: String?](./naturallanguagequery.md)
  A string containing the desired search item.
- [var region: MKCoordinateRegion](./region.md)
  A map region that provides a hint as to where to search.
- [static var physicalFeature: MKLocalSearch.ResultType](../resulttype/physicalfeature.md)
  A value that indicates that search results include physical features.
- [var regionPriority: MKLocalSearchRegionPriority](./regionpriority.md)
  A value that indicates the importance of the configured region.
- [var resultTypes: MKLocalSearch.ResultType](./resulttypes.md)
  The types of items to include in the search results.
- [MKLocalSearch.Request.ResultType](./resulttype.md)
  Options that indicate types of search results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklocalsearch/request/pointofinterestfilter)*