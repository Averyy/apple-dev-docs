# cameraZoomRange

**Framework**: MapKit  
**Kind**: property

The zoom range to apply to the map view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
@MainActor var cameraZoomRange: MKMapView.CameraZoomRange! { get set }
```

## See Also

- [func setCameraBoundary(MKMapView.CameraBoundary?, animated: Bool)](mkmapview/setcameraboundary(_:animated:).md)
  Sets the camera boundary for the map view, specifying whether to use animation.
- [var cameraBoundary: MKMapView.CameraBoundary?](mkmapview/cameraboundary-swift.property.md)
  The boundary of the area within which the map view’s center needs to remain.
- [func setCameraZoomRange(MKMapView.CameraZoomRange?, animated: Bool)](mkmapview/setcamerazoomrange(_:animated:).md)
  Sets the camera zoom range for the map view, specifying whether to use animation.
- [MKMapView.CameraBoundary](mkmapview/cameraboundary-swift.class.md)
  A boundary of an area within which the map’s center needs to remain.
- [MKMapView.CameraZoomRange](mkmapview/camerazoomrange-swift.class.md)
  A camera zoom range that limits the distances to which the user can zoom.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/camerazoomrange-swift.property)*