# boundingRegion

**Framework**: MapKit  
**Kind**: property

The map region that encloses the returned search results.

**Availability**:
- iOS 6.1+
- iPadOS 6.1+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
var boundingRegion: MKCoordinateRegion { get }
```

#### Discussion

The returned region is the smallest bounding box that encloses all of the map items. If there’s only one search result, the size of the region may be `(0, 0)`.

## See Also

- [var mapItems: [MKMapItem]](mklocalsearch/response/mapitems.md)
  An array of map items representing the search results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklocalsearch/response/boundingregion)*