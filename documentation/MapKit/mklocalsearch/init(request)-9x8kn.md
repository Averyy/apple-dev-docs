# init(request:)

**Framework**: MapKit  
**Kind**: init  
**Role**: Initializer

Creates and returns a search object for fetching points of interest.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init(request: MKLocalPointsOfInterestRequest)
```

```objc
- (instancetype) initWithPointsOfInterestRequest:(MKLocalPointsOfInterestRequest *) request;
```

## Parameters

- `request`: The search parameters to fetch points of interest.

## See Also

### Creating a search request
- [init(request: MKLocalSearch.Request)](./init%28request%29-12tf0.md)
  Creates and returns a search object with the specified parameters.
- [MKLocalSearch.Request](./request.md)
  The parameters to use when searching for points of interest on the map.
- [MKLocalSearch.ResultType](./resulttype.md)
  Options that indicate types of search results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklocalsearch/init(request:)-9x8kn)*