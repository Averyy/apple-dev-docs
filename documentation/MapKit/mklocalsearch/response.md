# MKLocalSearch.Response

**Framework**: MapKit  
**Kind**: class

The results from a map-based search.

**Availability**:
- iOS 6.1+
- iPadOS 6.1+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
class Response
```

#### Overview

You don’t create instances of this class directly. After initiating a map search using an [`MKLocalSearch`](mklocalsearch.md) object, MapKit passes an instance of this class to your completion handler.

## Topics

### Getting the search results
- [var mapItems: [MKMapItem]](mklocalsearch/response/mapitems.md)
  An array of map items representing the search results.
- [var boundingRegion: MKCoordinateRegion](mklocalsearch/response/boundingregion.md)
  The map region that encloses the returned search results.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklocalsearch/response)*