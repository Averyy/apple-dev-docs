# regionPriority

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

A value that indicates the importance of the configured region.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var regionPriority: MKLocalSearchRegionPriority { get set }
```

```objc
@property (nonatomic, assign) MKLocalSearchRegionPriority regionPriority;
```

## See Also

### Specifying the query attributes
- [var addressFilter: MKAddressFilter?](./addressfilter.md)
  A filter that lists which address options to include or exclude in search results.
- [var queryFragment: String](./queryfragment.md)
  The search string that you want completions for.
- [var region: MKCoordinateRegion](./region.md)
  The region that defines the geographic scope of the search.
- [var resultTypes: MKLocalSearchCompleter.ResultType](./resulttypes.md)
  The types of search completions to include.
- [var pointOfInterestFilter: MKPointOfInterestFilter?](./pointofinterestfilter.md)
  A filter that lists point of interest categories to include or exclude in the search.
- [var filterType: MKLocalSearchCompleter.FilterType](./filtertype-swift.property.md)
  The filter options for the search results.
- [MKLocalSearchCompleter.FilterType](./filtertype-swift.enum.md)
  Constants indicating the types of search completions to return.
- [MKLocalSearchCompleter.ResultType](./resulttype.md)
  Options that indicate types of search completions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklocalsearchcompleter/regionpriority)*