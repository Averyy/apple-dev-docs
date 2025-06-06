# MapProxy

**Framework**: MapKit  
**Kind**: struct

A proxy for accessing sizing information about a given map view.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
struct MapProxy
```

## Topics

### Creating a camera proxy
- [func camera(framing: MKCoordinateRegion) -> MapCamera](mapproxy/camera(framing:)-1asl2.md)
  Creates a camera in the context of the map that frames the given coordinate region.
- [func camera(framing: MKMapRect) -> MapCamera](mapproxy/camera(framing:)-uxov.md)
  Creates a camera in the context of the map that frames the given map rectangle.
- [func camera(framing: MKMapItem, allowPitch: Bool) -> MapCamera](mapproxy/camera(framing:allowpitch:).md)
  Creates a camera in the context of the map that frames the given map item.
### Converting between coordinate spaces
- [func convert(CLLocationCoordinate2D, to: some CoordinateSpaceProtocol) -> CGPoint?](mapproxy/convert(_:to:).md)
  Converts a map coordinate to a point in the specified coordinate space.
- [func convert(CGPoint, from: some CoordinateSpaceProtocol) -> CLLocationCoordinate2D?](mapproxy/convert(_:from:).md)
  Converts a point in the specified coordinate space to a map coordinate.

## See Also

- [struct DefaultUserAnnotationContent](defaultuserannotationcontent.md)
  A structure that represents the view to show at the user’s location on the map.
- [struct AnyMapContent](anymapcontent.md)
  A structure you use to change the type of content MapKit uses in a map view.
- [struct EmptyMapContent](emptymapcontent.md)
  A map content element that doesn’t contain any content.
- [struct MapReader](mapreader.md)
  A container view that defines its contents as a function of information about the first contained map.
- [struct TupleMapContent](tuplemapcontent.md)
  A view created from a Swift tuple of map content values.
- [struct MapSelectableContentView](mapselectablecontentview.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapproxy)*