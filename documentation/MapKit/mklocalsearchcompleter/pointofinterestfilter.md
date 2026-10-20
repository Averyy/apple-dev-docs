# pointOfInterestFilter

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

A filter that lists point of interest categories to include or exclude in the search.

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

### Specifying the query attributes
- [var addressFilter: MKAddressFilter?](./addressfilter.md)
  A filter that lists which address options to include or exclude in search results.
- [var queryFragment: String](./queryfragment.md)
  The search string that you want completions for.
- [var region: MKCoordinateRegion](./region.md)
  The region that defines the geographic scope of the search.
- [var regionPriority: MKLocalSearchRegionPriority](./regionpriority.md)
  A value that indicates the importance of the configured region.
- [var resultTypes: MKLocalSearchCompleter.ResultType](./resulttypes.md)
  The types of search completions to include.
- [var filterType: MKLocalSearchCompleter.FilterType](./filtertype-swift.property.md)
  The filter options for the search results.
- [MKLocalSearchCompleter.FilterType](./filtertype-swift.enum.md)
  Constants indicating the types of search completions to return.
- [MKLocalSearchCompleter.ResultType](./resulttype.md)
  Options that indicate types of search completions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklocalsearchcompleter/pointofinterestfilter)*