# mapType

**Framework**: MapKit  
**Kind**: property

The type of data the map view displays.

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
var mapType: MKMapType { get set }
```

#### Discussion

Changing the value in this property may cause the receiver to begin loading new map content. For example, changing from [`MKMapType.standard`](mkmaptype/standard.md) to [`MKMapType.satellite`](mkmaptype/satellite.md) might cause it to begin loading the satellite imagery for the map. If the map needs new data, however, it loads asynchronously and MapKit sends appropriate messages to the receiver’s delegate indicating the status of the operation.

## See Also

- [Location and Maps Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)
- [enum MKMapType](mkmaptype.md)
  The type of map to display.
- [var isZoomEnabled: Bool](mkmapview/iszoomenabled.md)
  A Boolean value that determines whether the user may use pinch gestures to zoom in and out of the map.
- [var isScrollEnabled: Bool](mkmapview/isscrollenabled.md)
  A Boolean value that determines whether the user may scroll around the map.
- [var isPitchEnabled: Bool](mkmapview/ispitchenabled.md)
  A Boolean value that indicates whether the map uses the camera’s pitch information.
- [var isRotateEnabled: Bool](mkmapview/isrotateenabled.md)
  A Boolean value that indicates whether the map uses the camera’s heading information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/maptype)*