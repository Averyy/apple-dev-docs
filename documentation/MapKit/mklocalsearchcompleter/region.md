# region

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The region that defines the geographic scope of the search.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- macOS 10.11.4+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var region: MKCoordinateRegion { get set }
```

```objc
@property (nonatomic, assign) MKCoordinateRegion region;
```

## Discussion

Use this property to limit search results to the specified geographic area. The default value of this property is a region that spans the entire world.

## See Also

### Specifying the query attributes
- [var addressFilter: MKAddressFilter?](./addressfilter.md)
  A filter that lists which address options to include or exclude in search results.
- [var queryFragment: String](./queryfragment.md)
  The search string that you want completions for.
- [var regionPriority: MKLocalSearchRegionPriority](./regionpriority.md)
  A value that indicates the importance of the configured region.
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

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklocalsearchcompleter/region)*