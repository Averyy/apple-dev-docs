# isZoomEnabled

**Framework**: MapKit  
**Kind**: property

A Boolean value that determines whether the user may use pinch gestures to zoom in and out of the map.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isZoomEnabled: Bool { get set }
```

#### Discussion

This property controls only user interactions with the map. If you set the value of this property to [`false`](https://developer.apple.com/documentation/swift/false), you may still change the zoom level programmatically by changing the value in the [`region`](mkmapview/region.md) property.

The default value of this property is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [enum MKMapType](mkmaptype.md)
  The type of map to display.
- [var isScrollEnabled: Bool](mkmapview/isscrollenabled.md)
  A Boolean value that determines whether the user may scroll around the map.
- [var isPitchEnabled: Bool](mkmapview/ispitchenabled.md)
  A Boolean value that indicates whether the map uses the camera’s pitch information.
- [var isRotateEnabled: Bool](mkmapview/isrotateenabled.md)
  A Boolean value that indicates whether the map uses the camera’s heading information.
- [var mapType: MKMapType](mkmapview/maptype.md)
  The type of data the map view displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/iszoomenabled)*