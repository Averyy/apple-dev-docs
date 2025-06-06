# ARPositionalTrackingConfiguration

**Framework**: ARKit  
**Kind**: class

A configuration that tracks only the device’s position in 3D space.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class ARPositionalTrackingConfiguration
```

#### Overview

Enables 6 degrees of freedom tracking of the iOS device by running the camera at lowest possible resolution and frame rate. Use this configuration when you don’t need to parse the camera feed, such as for example, virtual reality scenarios.

## Topics

### Creating a Configuration
- [init()](arpositionaltrackingconfiguration/init.md)
  Creates a new positional tracking configuration.
- [var initialWorldMap: ARWorldMap?](arpositionaltrackingconfiguration/initialworldmap.md)
  The state from a previous AR session to attempt to resume with this session configuration.
### Detecting Real-World Surfaces
- [var planeDetection: ARWorldTrackingConfiguration.PlaneDetection](arpositionaltrackingconfiguration/planedetection.md)
  A value that specifies if and how the session automatically attempts to detect flat surfaces in the camera-captured image.

## Relationships

### Inherits From
- [ARConfiguration](arconfiguration.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Understanding World Tracking](understanding-world-tracking.md)
  Discover features and best practices for building rear-camera AR experiences.
- [class ARWorldTrackingConfiguration](arworldtrackingconfiguration.md)
  A configuration that tracks the position of a device in relation to objects in the environment.
- [class ARGeoTrackingConfiguration](argeotrackingconfiguration.md)
  A configuration that tracks locations with GPS, map data, and a device’s compass.
- [class AROrientationTrackingConfiguration](arorientationtrackingconfiguration.md)
  A configuration that tracks only the device’s orientation using the rear-facing camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arpositionaltrackingconfiguration)*