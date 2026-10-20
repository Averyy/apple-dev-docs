# isPitchEnabled

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the map uses the camera’s pitch information.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- visionOS 1.0+

## Declaration

```swift
var isPitchEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isPitchEnabled) BOOL pitchEnabled;
```

#### Discussion

When this property is [`true`](../../Swift/true.md) and the framework associates a valid camera with the map, the map view uses the camera’s pitch angle to tilt the plane of the map. When this property is [`false`](../../Swift/false.md), the map ignores the camera’s pitch angle and the map displays as if the user is looking straight down onto it.

In an app, be sure to check the value of this property to determine whether a map can support 3D.

## See Also

### Accessing map properties
- [enum MKMapType](../mkmaptype.md)
  The type of map to display.
- [var isZoomEnabled: Bool](./iszoomenabled.md)
  A Boolean value that determines whether the user may use pinch gestures to zoom in and out of the map.
- [var isScrollEnabled: Bool](./isscrollenabled.md)
  A Boolean value that determines whether the user may scroll around the map.
- [var isRotateEnabled: Bool](./isrotateenabled.md)
  A Boolean value that indicates whether the map uses the camera’s heading information.
- [var mapType: MKMapType](./maptype.md)
  The type of data the map view displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/ispitchenabled)*