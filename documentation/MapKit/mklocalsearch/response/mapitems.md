# mapItems

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

An array of map items representing the search results.

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
var mapItems: [MKMapItem] { get }
```

```objc
@property (nonatomic, readonly) NSArray<MKMapItem *> * mapItems;
```

## Discussion

This property contains an array of [`MKMapItem`](../../mkmapitem.md) objects, each of which represents a returned search result. You can use these objects to retrieve information about the search result, such as the name of the point of interest, the address, the geographic location, and so on.

## See Also

### Related Documentation
- [Location and Maps Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)
### Getting the search results
- [var boundingRegion: MKCoordinateRegion](./boundingregion.md)
  The map region that encloses the returned search results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklocalsearch/response/mapitems)*