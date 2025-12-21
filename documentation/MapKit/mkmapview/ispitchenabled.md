# isPitchEnabled

**Framework**: MapKit  
**Kind**: property

A Boolean value that indicates whether the map uses the camera’s pitch information.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isPitchEnabled: Bool { get set }
```

#### Discussion

When this property is [`true`](https://developer.apple.com/documentation/Swift/true) and the framework associates a valid camera with the map, the map view uses the camera’s pitch angle to tilt the plane of the map. When this property is [`false`](https://developer.apple.com/documentation/Swift/false), the map ignores the camera’s pitch angle and the map displays as if the user is looking straight down onto it.

In an app, be sure to check the value of this property to determine whether a map can support 3D.

## See Also

- [enum MKMapType](mkmaptype.md)
  The type of map to display.
- [var isZoomEnabled: Bool](mkmapview/iszoomenabled.md)
  A Boolean value that determines whether the user may use pinch gestures to zoom in and out of the map.
- [var isScrollEnabled: Bool](mkmapview/isscrollenabled.md)
  A Boolean value that determines whether the user may scroll around the map.
- [var isRotateEnabled: Bool](mkmapview/isrotateenabled.md)
  A Boolean value that indicates whether the map uses the camera’s heading information.
- [var mapType: MKMapType](mkmapview/maptype.md)
  The type of data the map view displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/ispitchenabled)*