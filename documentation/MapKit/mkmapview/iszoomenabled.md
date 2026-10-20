# isZoomEnabled

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

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
var isZoomEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isZoomEnabled) BOOL zoomEnabled;
```

#### Discussion

This property controls only user interactions with the map. If you set the value of this property to [`false`](../../Swift/false.md), you may still change the zoom level programmatically by changing the value in the [`region`](./region.md) property.

The default value of this property is [`true`](../../Swift/true.md).

## See Also

### Accessing map properties
- [enum MKMapType](../mkmaptype.md)
  The type of map to display.
- [var isScrollEnabled: Bool](./isscrollenabled.md)
  A Boolean value that determines whether the user may scroll around the map.
- [var isPitchEnabled: Bool](./ispitchenabled.md)
  A Boolean value that indicates whether the map uses the camera’s pitch information.
- [var isRotateEnabled: Bool](./isrotateenabled.md)
  A Boolean value that indicates whether the map uses the camera’s heading information.
- [var mapType: MKMapType](./maptype.md)
  The type of data the map view displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/iszoomenabled)*