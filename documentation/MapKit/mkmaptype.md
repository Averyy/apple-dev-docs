# MKMapType

**Framework**: MapKit  
**Kind**: enum

The type of map to display.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
enum MKMapType
```

## Topics

### Constants
- [MKMapType.standard](mkmaptype/standard.md)
  A street map that shows the position of all roads and some road names.
- [MKMapType.satellite](mkmaptype/satellite.md)
  Satellite imagery of the area.
- [MKMapType.hybrid](mkmaptype/hybrid.md)
  A satellite image of the area with road and road name information layered on top.
- [MKMapType.satelliteFlyover](mkmaptype/satelliteflyover.md)
  A satellite image of the area with flyover data where available.
- [MKMapType.hybridFlyover](mkmaptype/hybridflyover.md)
  A hybrid satellite image with flyover data where available.
- [MKMapType.mutedStandard](mkmaptype/mutedstandard.md)
  A street map where MapKit emphasizes your data over the underlying map details.
### Initializers
- [init?(rawValue: UInt)](mkmaptype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var isZoomEnabled: Bool](mkmapview/iszoomenabled.md)
  A Boolean value that determines whether the user may use pinch gestures to zoom in and out of the map.
- [var isScrollEnabled: Bool](mkmapview/isscrollenabled.md)
  A Boolean value that determines whether the user may scroll around the map.
- [var isPitchEnabled: Bool](mkmapview/ispitchenabled.md)
  A Boolean value that indicates whether the map uses the camera’s pitch information.
- [var isRotateEnabled: Bool](mkmapview/isrotateenabled.md)
  A Boolean value that indicates whether the map uses the camera’s heading information.
- [var mapType: MKMapType](mkmapview/maptype.md)
  The type of data the map view displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmaptype)*