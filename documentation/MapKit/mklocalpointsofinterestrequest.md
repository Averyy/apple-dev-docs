# MKLocalPointsOfInterestRequest

**Framework**: MapKit  
**Kind**: class

A structured request to use when searching for points of interest.

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
class MKLocalPointsOfInterestRequest
```

#### Overview

You create an [`MKLocalPointsOfInterestRequest`](mklocalpointsofinterestrequest.md) to fetch points of interest within a rectangular bounding box or circular area.

To leverage the phone’s viewport to request points of interest, create a request with a rectangular bounding box using an [`MKCoordinateRegion`](mkcoordinateregion.md). The request fetches points of interest within the rectangular region.

To retrieve points of interest nearby or “around the user,” create a request with a circular area defined by doc://com.apple.documentation/documentation/corelocation/cllocationcoordinate2d and a doc://com.apple.documentation/documentation/corelocation/cllocationdistance in meters. The fetch returns points of interest up to the maximum distance defined by [`maxRadius`](mklocalpointsofinterestrequest/maxradius.md).

You may optionally specifying an [`MKPointOfInterestFilter`](mkpointofinterestfilter.md) describing categories to include or exclude. The default behavior of the fetch returns all points of interest.

## Topics

### Creating a point of interest request
- [init(center: CLLocationCoordinate2D, radius: CLLocationDistance)](mklocalpointsofinterestrequest/init(center:radius:).md)
  Creates a points of interest search request centered on the provided coordinate with the provided radius.
- [init(coordinateRegion: MKCoordinateRegion)](mklocalpointsofinterestrequest/init(coordinateregion:).md)
  Creates a points of interest search request based on existing region.
### Configuring the request parameters
- [var region: MKCoordinateRegion](mklocalpointsofinterestrequest/region.md)
  The region of the bounding box of the request provided or the derived bounding box of the circle created by the radius.
- [var coordinate: CLLocationCoordinate2D](mklocalpointsofinterestrequest/coordinate.md)
  The center of the point of request as latitude and longitude.
- [var radius: CLLocationDistance](mklocalpointsofinterestrequest/radius.md)
  The distance provided in meters or the longest distance derived from the center point to the region’s bounding box.
- [var pointOfInterestFilter: MKPointOfInterestFilter?](mklocalpointsofinterestrequest/pointofinterestfilter.md)
  A filter that lists points of interest categories to include or exclude.
### Getting the maximum radius
- [class let maxRadius: CLLocationDistance](mklocalpointsofinterestrequest/maxradius.md)
  The maximum distance respected for fetching points of interest from the center of the region.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Interacting with nearby points of interest](interacting-with-nearby-points-of-interest.md)
  Provide automatic search completions for a partial search query, search the map for relevant locations nearby, and retrieve details for selected points of interest.
- [enum MKLocalSearchRegionPriority](mklocalsearchregionpriority.md)
  A value that indicates the importance of the configured region.
- [MKLocalSearch.ResultType](mklocalsearch/resulttype.md)
  Options that indicate types of search results.
- [class MKLocalSearch](mklocalsearch.md)
  A utility object for initiating map-based searches and processing the results.
- [MKAddressFilter.Options](mkaddressfilter/options.md)
  A structure that contains options for filtering results in a search.
- [class MKAddressFilter](mkaddressfilter.md)
  An object that filters which address options to include or exclude in search results.
- [MKLocalSearchCompleter.ResultType](mklocalsearchcompleter/resulttype.md)
  Options that indicate types of search completions.
- [class MKLocalSearchCompleter](mklocalsearchcompleter.md)
  A utility object for generating a list of completion strings based on a partial search string that you provide.
- [class MKLocalSearchCompletion](mklocalsearchcompletion.md)
  A fully formed string that completes a partial string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklocalpointsofinterestrequest)*