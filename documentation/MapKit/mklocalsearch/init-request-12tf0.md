# init(request:)

**Framework**: MapKit  
**Kind**: init

Creates and returns a search object with the specified parameters.

**Availability**:
- iOS 6.1+
- iPadOS 6.1+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
init(request: MKLocalSearch.Request)
```

#### Return Value

An initialized search object.

#### Discussion

This method stores a copy of the object in the `request` parameter. So, the object ignores any changes you make to your request object after calling this method.

## Parameters

- `request`: The search request information. This parameter can’t be  .

## See Also

- [Location and Maps Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)
- [init(request: MKLocalPointsOfInterestRequest)](mklocalsearch/init(request:)-9x8kn.md)
  Creates and returns a search object for fetching points of interest.
- [MKLocalSearch.Request](mklocalsearch/request.md)
  The parameters to use when searching for points of interest on the map.
- [MKLocalSearch.ResultType](mklocalsearch/resulttype.md)
  Options that indicate types of search results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklocalsearch/init(request:)-12tf0)*