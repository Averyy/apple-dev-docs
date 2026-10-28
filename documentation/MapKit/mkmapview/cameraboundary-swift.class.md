# MKMapView.CameraBoundary

**Framework**: MapKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface MKMapCameraBoundary : NSObject
```

## Overview

The constraints of the camera boundary restrict the center point of your map.

## Topics

### Creating a camera boundary
- [init?(coder: NSCoder)](./cameraboundary-swift.class/init%28coder%29.md)
  Creates a camera boundary using the provided coder.
- [init?(coordinateRegion: MKCoordinateRegion)](./cameraboundary-swift.class/init%28coordinateregion%29.md)
  Creates a camera boundary using the provided coordinate region.
- [init?(mapRect: MKMapRect)](./cameraboundary-swift.class/init%28maprect%29.md)
  Creates a camera boundary using the provided map rectangle.
### Accessing the boundary
- [var mapRect: MKMapRect](./cameraboundary-swift.class/maprect.md)
  The map rectangle that describes the camera boundary.
- [var region: MKCoordinateRegion](./cameraboundary-swift.class/region.md)
  The coordinate region that describes the camera boundary.

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
- [MKMapView.CameraZoomRange](./camerazoomrange-swift.class.md)
  A camera zoom range that limits the distances to which the user can zoom.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/cameraboundary-swift.class)*