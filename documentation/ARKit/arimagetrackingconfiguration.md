# ARImageTrackingConfiguration

**Framework**: ARKit  
**Kind**: class

A configuration that tracks known images using the rear-facing camera.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class ARImageTrackingConfiguration
```

#### Overview

All AR configurations establish a correspondence between the real world the device inhabits and a virtual 3D coordinate space where you can model content. When your app displays that content together with a live camera image, the user experiences the illusion that your virtual content is part of the real world.

With [`ARImageTrackingConfiguration`](arimagetrackingconfiguration.md), ARKit establishes a 3D space not by tracking the motion of the device relative to the world, but solely by detecting and tracking the motion of known 2D images in view of the camera. [`ARWorldTrackingConfiguration`](arworldtrackingconfiguration.md) can also detect images, but each configuration has its own strengths:

- World tracking has a higher performance cost than image-only tracking, so your session can reliably track more images at once with [`ARImageTrackingConfiguration`](arimagetrackingconfiguration.md).
- Image-only tracking lets you anchor virtual content to known images only when those images are in view of the camera. World tracking with image detection lets you use known images to add virtual content to the 3D world, and continues to track the position of that content in world space even after the image is no longer in view.
- World tracking works best in a stable, nonmoving environment. You can use image-only tracking to add virtual content to known images in more situations—for example, an advertisement inside a moving subway car.

When an image-tracking configuration detects known images, it tracks their movement with six degrees of freedom (6DOF): specifically, the three rotation axes (roll, pitch, and yaw), and three translation axes (movement in x, y, and z).

To use [`ARImageTrackingConfiguration`](arimagetrackingconfiguration.md), define ARReferenceImage objects (either at runtime or by bundling them in your Xcode asset catalog) and assign them to the configuration’s [`trackingImages`](arimagetrackingconfiguration/trackingimages.md) property. Then, as with any AR configuration, pass the configuration to your session’s [`run(_:options:)`](arsession/run(_:options:).md) method.

## Topics

### Creating a Configuration
- [init()](arimagetrackingconfiguration/init.md)
  Initializes a new image-tracking configuration.
### Choosing Images to Track
- [var trackingImages: Set<ARReferenceImage>](arimagetrackingconfiguration/trackingimages.md)
  A set of images that ARKit searches for and tracks in the user’s environment.
- [var maximumNumberOfTrackedImages: Int](arimagetrackingconfiguration/maximumnumberoftrackedimages.md)
  The number of image anchors to monitor closely for position and orientation updates.
### Managing Device Camera Behavior
- [var isAutoFocusEnabled: Bool](arimagetrackingconfiguration/isautofocusenabled.md)
  A Boolean value that determines whether the device camera uses fixed focus or autofocus behavior.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arimagetrackingconfiguration)*