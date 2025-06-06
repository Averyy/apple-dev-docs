# MKMapView.CameraBoundary

**Framework**: MapKit  
**Kind**: class

A boundary of an area within which the map’s center needs to remain.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class CameraBoundary
```

#### Overview

The constraints of the camera boundary restrict the center point of your map.

## Topics

### Creating a camera boundary
- [init?(coder: NSCoder)](mkmapview/cameraboundary-swift.class/init(coder:).md)
  Creates a camera boundary using the provided coder.
- [init?(coordinateRegion: MKCoordinateRegion)](mkmapview/cameraboundary-swift.class/init(coordinateregion:).md)
  Creates a camera boundary using the provided coordinate region.
- [init?(mapRect: MKMapRect)](mkmapview/cameraboundary-swift.class/init(maprect:).md)
  Creates a camera boundary using the provided map rectangle.
### Accessing the boundary
- [var mapRect: MKMapRect](mkmapview/cameraboundary-swift.class/maprect.md)
  The map rectangle that describes the camera boundary.
- [var region: MKCoordinateRegion](mkmapview/cameraboundary-swift.class/region.md)
  The coordinate region that describes the camera boundary.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [func setCameraBoundary(MKMapView.CameraBoundary?, animated: Bool)](mkmapview/setcameraboundary(_:animated:).md)
  Sets the camera boundary for the map view, specifying whether to use animation.
- [var cameraBoundary: MKMapView.CameraBoundary?](mkmapview/cameraboundary-swift.property.md)
  The boundary of the area within which the map view’s center needs to remain.
- [func setCameraZoomRange(MKMapView.CameraZoomRange?, animated: Bool)](mkmapview/setcamerazoomrange(_:animated:).md)
  Sets the camera zoom range for the map view, specifying whether to use animation.
- [var cameraZoomRange: MKMapView.CameraZoomRange!](mkmapview/camerazoomrange-swift.property.md)
  The zoom range to apply to the map view.
- [MKMapView.CameraZoomRange](mkmapview/camerazoomrange-swift.class.md)
  A camera zoom range that limits the distances to which the user can zoom.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/cameraboundary-swift.class)*