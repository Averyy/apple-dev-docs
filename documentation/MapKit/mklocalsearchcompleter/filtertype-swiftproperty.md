# filterType

**Framework**: MapKit  
**Kind**: property

The filter options for the search results.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- macOS 10.11.4+
- tvOS 9.2+

## Declaration

```swift
var filterType: MKLocalSearchCompleter.FilterType { get set }
```

#### Discussion

Use this property to determine whether you want completions that represent points-of-interest or whether completions might yield additional relevant query strings.

## See Also

- [var addressFilter: MKAddressFilter?](mklocalsearchcompleter/addressfilter.md)
  A filter that lists which address options to include or exclude in search results.
- [var queryFragment: String](mklocalsearchcompleter/queryfragment.md)
  The search string that you want completions for.
- [var region: MKCoordinateRegion](mklocalsearchcompleter/region.md)
  The region that defines the geographic scope of the search.
- [var regionPriority: MKLocalSearchRegionPriority](mklocalsearchcompleter/regionpriority.md)
  A value that indicates the importance of the configured region.
- [var resultTypes: MKLocalSearchCompleter.ResultType](mklocalsearchcompleter/resulttypes.md)
  The types of search completions to include.
- [var pointOfInterestFilter: MKPointOfInterestFilter?](mklocalsearchcompleter/pointofinterestfilter.md)
  A filter that lists point of interest categories to include or exclude in the search.
- [MKLocalSearchCompleter.FilterType](mklocalsearchcompleter/filtertype-swift.enum.md)
  Constants indicating the types of search completions to return.
- [MKLocalSearchCompleter.ResultType](mklocalsearchcompleter/resulttype.md)
  Options that indicate types of search completions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklocalsearchcompleter/filtertype-swift.property)*