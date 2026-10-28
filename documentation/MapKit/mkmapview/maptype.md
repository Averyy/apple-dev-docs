# mapType

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The type of data the map view displays.

**Availability**:
- iOS 3.0+ - Deprecated in 27.2
- iPadOS 3.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.9+ - Deprecated in 27.2
- tvOS 9.2+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use the map view’s [`preferredConfiguration`](./preferredconfiguration.md) property with an [`MKMapConfiguration`](../mkmapconfiguration.md) subclass to specify how the framework presents the map instead.

## Declaration

```swift
var mapType: MKMapType { get set }
```

```objc
@property (nonatomic) MKMapType mapType;
```

## Discussion

Changing the value in this property may cause the receiver to begin loading new map content. For example, changing from [`MKMapType.standard`](../mkmaptype/standard.md) to [`MKMapType.satellite`](../mkmaptype/satellite.md) might cause it to begin loading the satellite imagery for the map. If the map needs new data, however, it loads asynchronously and MapKit sends appropriate messages to the receiver’s delegate indicating the status of the operation.

## See Also

### Related Documentation
- [Location and Maps Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)
### Accessing map properties
- [enum MKMapType](../mkmaptype.md)
  The type of map to display.
- [var isZoomEnabled: Bool](./iszoomenabled.md)
  A Boolean value that determines whether the user may use pinch gestures to zoom in and out of the map.
- [var isScrollEnabled: Bool](./isscrollenabled.md)
  A Boolean value that determines whether the user may scroll around the map.
- [var isPitchEnabled: Bool](./ispitchenabled.md)
  A Boolean value that indicates whether the map uses the camera’s pitch information.
- [var isRotateEnabled: Bool](./isrotateenabled.md)
  A Boolean value that indicates whether the map uses the camera’s heading information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/maptype)*