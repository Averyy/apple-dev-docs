# MKLocalSearch.Response

**Framework**: MapKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface MKLocalSearchResponse : NSObject
```

## Overview

You don’t create instances of this class directly. After initiating a map search using an [`MKLocalSearch`](../mklocalsearch.md) object, MapKit passes an instance of this class to your completion handler.

## Topics

### Getting the search results
- [var mapItems: [MKMapItem]](./response/mapitems.md)
  An array of map items representing the search results.
- [var boundingRegion: MKCoordinateRegion](./response/boundingregion.md)
  The map region that encloses the returned search results.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklocalsearch/response)*