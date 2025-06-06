# isRotateEnabled

**Framework**: MapKit  
**Kind**: property

A Boolean value that indicates whether the map uses the camera’s heading information.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isRotateEnabled: Bool { get set }
```

#### Discussion

When this property is [`true`](https://developer.apple.com/documentation/swift/true) and the framework associates a valid camera with the map, the map uses the camera’s heading angle to rotate the plane of the map around its center point. When this property is [`false`](https://developer.apple.com/documentation/swift/false), the map view ignores the camera’s heading angle and the map orients so that the map view situates true north at the top.

## See Also

- [enum MKMapType](mkmaptype.md)
  The type of map to display.
- [var isZoomEnabled: Bool](mkmapview/iszoomenabled.md)
  A Boolean value that determines whether the user may use pinch gestures to zoom in and out of the map.
- [var isScrollEnabled: Bool](mkmapview/isscrollenabled.md)
  A Boolean value that determines whether the user may scroll around the map.
- [var isPitchEnabled: Bool](mkmapview/ispitchenabled.md)
  A Boolean value that indicates whether the map uses the camera’s pitch information.
- [var mapType: MKMapType](mkmapview/maptype.md)
  The type of data the map view displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/isrotateenabled)*