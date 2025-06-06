# pointOfInterestFilter

**Framework**: MapKit  
**Kind**: property

A filter that lists point of interest categories to include or exclude in the search.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var pointOfInterestFilter: MKPointOfInterestFilter? { get set }
```

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
- [var filterType: MKLocalSearchCompleter.FilterType](mklocalsearchcompleter/filtertype-swift.property.md)
  The filter options for the search results.
- [MKLocalSearchCompleter.FilterType](mklocalsearchcompleter/filtertype-swift.enum.md)
  Constants indicating the types of search completions to return.
- [MKLocalSearchCompleter.ResultType](mklocalsearchcompleter/resulttype.md)
  Options that indicate types of search completions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklocalsearchcompleter/pointofinterestfilter)*