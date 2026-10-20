# MKMapView.CameraZoomRange

**Framework**: MapKit  
**Kind**: class  
**Role**: Class

A camera zoom range that limits the distances to which the user can zoom.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class CameraZoomRange
```

```objc
@interface MKMapCameraZoomRange : NSObject
```

#### Overview

Create a camera zoom range to limit the distance to which the user can zoom. After you create the camera zoom range, you can apply it to multiple map views. If you don’t create a camera zoom range, your map view allows the user to zoom to MapKit’s capabilities.

## Topics

### Creating a camera zoom range
- [init?(minCenterCoordinateDistance: CLLocationDistance, maxCenterCoordinateDistance: CLLocationDistance)](./camerazoomrange-swift.class/init%28mincentercoordinatedistance,maxcentercoordinatedistance%29.md)
  Create a camera zoom range by specifying a minimum and maximum distance from your map view’s center coordinates, measured in meters.
- [convenience init?(minCenterCoordinateDistance: CLLocationDistance)](./camerazoomrange-swift.class/init%28mincentercoordinatedistance%29.md)
  Create a camera zoom range by specifying the minimum distance from your map view’s center coordinate, measured in meters.
- [convenience init?(maxCenterCoordinateDistance: CLLocationDistance)](./camerazoomrange-swift.class/init%28maxcentercoordinatedistance%29.md)
  Create a camera zoom range by specifying the maximum distance from your map view’s center coordinate, measured in meters.
- [let MKMapCameraZoomDefault: CLLocationDistance](../mkmapcamerazoomdefault.md)
  A constant value used to represent the default value for zooming in or out on a map.
### Accessing zoom range values
- [var maxCenterCoordinateDistance: CLLocationDistance](./camerazoomrange-swift.class/maxcentercoordinatedistance.md)
  The maximum distance of the camera to the center of the map, measured in meters.
- [var minCenterCoordinateDistance: CLLocationDistance](./camerazoomrange-swift.class/mincentercoordinatedistance.md)
  The minimum distance of the camera to the center of the map, measured in meters.
### Initializers
- [init?(coder: NSCoder)](./camerazoomrange-swift.class/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSCoding](../../Foundation/nscoding.md)
- [NSCopying](../../Foundation/nscopying.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../../Foundation/nssecurecoding.md)

## See Also

### Constraining the map view
- [func setCameraBoundary(MKMapView.CameraBoundary?, animated: Bool)](./setcameraboundary%28_,animated%29.md)
  Sets the camera boundary for the map view, specifying whether to use animation.
- [var cameraBoundary: MKMapView.CameraBoundary?](./cameraboundary-swift.property.md)
  The boundary of the area within which the map view’s center needs to remain.
- [func setCameraZoomRange(MKMapView.CameraZoomRange?, animated: Bool)](./setcamerazoomrange%28_,animated%29.md)
  Sets the camera zoom range for the map view, specifying whether to use animation.
- [var cameraZoomRange: MKMapView.CameraZoomRange!](./camerazoomrange-swift.property.md)
  The zoom range to apply to the map view.
- [MKMapView.CameraBoundary](./cameraboundary-swift.class.md)
  A boundary of an area within which the map’s center needs to remain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/camerazoomrange-swift.class)*