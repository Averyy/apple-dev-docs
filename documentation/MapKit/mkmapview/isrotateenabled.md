# isRotateEnabled

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the map uses the camera’s heading information.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- visionOS 1.0+

## Declaration

```swift
var isRotateEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isRotateEnabled) BOOL rotateEnabled;
```

#### Discussion

When this property is [`true`](../../Swift/true.md) and the framework associates a valid camera with the map, the map uses the camera’s heading angle to rotate the plane of the map around its center point. When this property is [`false`](../../Swift/false.md), the map view ignores the camera’s heading angle and the map orients so that the map view situates true north at the top.

## See Also

### Accessing map properties
- [enum MKMapType](../mkmaptype.md)
  The type of map to display.
- [var isZoomEnabled: Bool](./iszoomenabled.md)
  A Boolean value that determines whether the user may use pinch gestures to zoom in and out of the map.
- [var isScrollEnabled: Bool](./isscrollenabled.md)
  A Boolean value that determines whether the user may scroll around the map.
- [var isPitchEnabled: Bool](./ispitchenabled.md)
  A Boolean value that indicates whether the map uses the camera’s pitch information.
- [var mapType: MKMapType](./maptype.md)
  The type of data the map view displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/isrotateenabled)*