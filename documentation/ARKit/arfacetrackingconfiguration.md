# ARFaceTrackingConfiguration

**Framework**: Arkit  
**Kind**: class

A configuration that tracks facial movement and expressions using the front camera.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class ARFaceTrackingConfiguration
```

## Mentions

- [Verifying Device Support and User Permission](verifying-device-support-and-user-permission.md)
- [Choosing Which Camera Feed to Augment](choosing-which-camera-feed-to-augment.md)

#### Overview

A face-tracking configuration detects faces within 3 meters of the device’s front camera. When ARKit detects a face, it creates an [`ARFaceAnchor`](arfaceanchor.md) object that provides information about a person’s facial position, orientation, topology, and expressions.

Face tracking supports devices with Apple Neural Engine in iOS 14 and iPadOS 14 and requires a device with a TrueDepth camera on iOS 13 and iPadOS 13 and earlier. To determine whether the device supports face tracking, call [`isSupported`](arconfiguration/issupported.md) on [`ARFaceTrackingConfiguration`](arfacetrackingconfiguration.md) before attempting to use this configuration.

When you enable the [`isLightEstimationEnabled`](arconfiguration/islightestimationenabled.md) setting, a face-tracking configuration estimates directional and environmental lighting (an [`ARDirectionalLightEstimate`](ardirectionallightestimate.md) object) by referring to the detected face as a light probe.

> **Note**:  Because face tracking provides your app with personal facial information, your app must include a privacy policy describing to users how you intend to use face tracking and face data. For details, see the [`Apple Developer Program License Agreement`](https://developer.apple.comhttps://developer.apple.com/terms/).

## Topics

### Creating a Configuration
- [init()](arfacetrackingconfiguration/init.md)
  Creates a new face-tracking configuration.
### Enabling World Tracking
- [class var supportsWorldTracking: Bool](arfacetrackingconfiguration/supportsworldtracking.md)
  A Boolean value that indicates whether the iOS device supports tracking the user’s facial features in a world-tracking session.
- [var isWorldTrackingEnabled: Bool](arfacetrackingconfiguration/isworldtrackingenabled.md)
  A Boolean value that instructs a session to provide the app with the device’s six degrees of freedom pose during a face-tracking session.
### Tracking Multiple Faces
- [var maximumNumberOfTrackedFaces: Int](arfacetrackingconfiguration/maximumnumberoftrackedfaces.md)
  The number of faces to track during the session.
- [class var supportedNumberOfTrackedFaces: Int](arfacetrackingconfiguration/supportednumberoftrackedfaces.md)
  The maximum number of faces that the framework can track.

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

- [class ARBodyTrackingConfiguration](arbodytrackingconfiguration.md)
  A configuration that tracks human body poses, planar surfaces, and images using the rear-facing camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ARKit/arfacetrackingconfiguration)*