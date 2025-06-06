# ARKit

**Framework**: ARKit  
**Kind**: module

Integrate hardware sensing features to produce augmented reality apps and games.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Mentions

- [Validating a Model for Motion Capture](validating-a-model-for-motion-capture.md)
- [Recording and Replaying AR Session Data](recording-and-replaying-ar-session-data.md)

#### Overview

 (AR) describes user experiences that add 2D or 3D elements to the live view from a device’s sensors in a way that makes those elements appear to inhabit the real world. ARKit combines device motion tracking, world tracking, scene understanding, and display conveniences to simplify building an AR experience.

![An illustration showing a robot and a futuristic greenhouse.](https://docs-assets.developer.apple.com/published/a5209042ade8072b9689305fab0840a9/arkit-hero%402x.png)

## Topics

### visionOS
- [Setting up access to ARKit data](../visionOS/setting-up-access-to-arkit-data.md)
  Check whether your app can use ARKit and respect people’s privacy.
- [class ARKitSession](arkitsession.md)
  The main entry point for receiving data from ARKit.
- [protocol DataProvider](dataprovider.md)
  A source of live data from ARKit.
- [protocol Anchor](anchor.md)
  The identity, location, and orientation of an object in world space.
- [ARKit in visionOS](arkit-in-visionos.md)
  Create immersive augmented reality experiences.
- [ARKit in visionOS C API](arkit-in-visionos-c-api.md)
  Integrate ARKit with low-level libraries and functionality.
### iOS
- [Verifying Device Support and User Permission](verifying-device-support-and-user-permission.md)
  Check whether your app can use ARKit and respect user privacy at runtime.
- [class ARSession](arsession.md)
  The object that manages the major tasks associated with every AR experience, such as motion tracking, camera passthrough, and image analysis.
- [class ARAnchor](aranchor.md)
  An object that specifies the position and orientation of an item in the physical environment.
- [ARKit in iOS](arkit-in-ios.md)
  Integrate iOS device camera and motion features to produce augmented reality experiences in your app or game.
### Classes
- [class StereoPropertiesProvider](stereopropertiesprovider.md)
  The StereoPropertiesProvider serves the latest viewpoint properties on the device.
### Protocols
- [protocol OS_ar_stereo_properties_configuration](os_ar_stereo_properties_configuration.md)
- [protocol OS_ar_stereo_properties_provider](os_ar_stereo_properties_provider.md)
- [protocol OS_ar_viewpoint_properties](os_ar_viewpoint_properties.md)
### Structures
- [struct ViewpointProperties](viewpointproperties.md)
  The ViewpointProperties is a record of render camera transforms at some particular time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ARKit)*