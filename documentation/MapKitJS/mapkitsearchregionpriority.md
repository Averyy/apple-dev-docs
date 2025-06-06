# mapkit.Search.RegionPriority

**Framework**: MapKit JS  
**Kind**: enum

A value that indicates the importance of the configured region.

**Availability**:
- MapKit JS 5.78.1+

## Declaration

```swift
interface mapkit.Search.RegionPriority {
	const string Default;
	const string Required;
};
```

## Topics

### Setting the region priority
- [Default](mapkit.search.regionpriority/default.md)
  A value indicating that the results can originate from outside the specified region.
- [Required](mapkit.search.regionpriority/required.md)
  A value indicating that no results can originate from outside the specified region.

## See Also

- [mapkit.AddressCategory](mapkit.addresscategory.md)
  The categories of address components that users can search for with an address filter.
- [mapkit.AddressFilter](mapkit.addressfilter.md)
  An object that filters which address options to include or exclude in search results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.search.regionpriority)*