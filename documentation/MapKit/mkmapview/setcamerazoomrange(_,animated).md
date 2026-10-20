# setCameraZoomRange(_:animated:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Sets the camera zoom range for the map view, specifying whether to use animation.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func setCameraZoomRange(_ cameraZoomRange: MKMapView.CameraZoomRange?, animated: Bool)
```

```objc
- (void) setCameraZoomRange:(MKMapCameraZoomRange *) cameraZoomRange animated:(BOOL) animated;
```

## Parameters

- `cameraZoomRange`: The [`MKMapView.CameraZoomRange`](./camerazoomrange-swift.class.md).
- `animated`: A Boolean value that indicates whether the framework animates the transition of the map view to the new zoom range.

## See Also

### Constraining the map view
- [func setCameraBoundary(MKMapView.CameraBoundary?, animated: Bool)](./setcameraboundary%28_,animated%29.md)
  Sets the camera boundary for the map view, specifying whether to use animation.
- [var cameraBoundary: MKMapView.CameraBoundary?](./cameraboundary-swift.property.md)
  The boundary of the area within which the map view’s center needs to remain.
- [var cameraZoomRange: MKMapView.CameraZoomRange!](./camerazoomrange-swift.property.md)
  The zoom range to apply to the map view.
- [MKMapView.CameraBoundary](./cameraboundary-swift.class.md)
  A boundary of an area within which the map’s center needs to remain.
- [MKMapView.CameraZoomRange](./camerazoomrange-swift.class.md)
  A camera zoom range that limits the distances to which the user can zoom.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/setcamerazoomrange(_:animated:))*