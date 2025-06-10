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
- [class AccessoryTrackingProvider](accessorytrackingprovider.md)
  Provides the real time position of accessories in the user’s environment.
- [class CameraRegionProvider](cameraregionprovider.md)
  A camera region provider. An enterprise license is required to use the CameraRegionProvider. The provider will not deliver any data without it. The app must include the following entitlement: `com.apple.developer.arkit.camera-region.allow`
- [class SharedCoordinateSpaceProvider](sharedcoordinatespaceprovider.md)
  Provides ability to establish a shared coordinate space among multiple participants.
- [class StereoPropertiesProvider](stereopropertiesprovider.md)
  The StereoPropertiesProvider serves the latest viewpoint properties on the device.
### Protocols
- [protocol OS_ar_accessories](os_ar_accessories.md)
- [protocol OS_ar_accessory](os_ar_accessory.md)
- [protocol OS_ar_accessory_anchor](os_ar_accessory_anchor.md)
- [protocol OS_ar_accessory_anchors](os_ar_accessory_anchors.md)
- [protocol OS_ar_accessory_tracking_configuration](os_ar_accessory_tracking_configuration.md)
- [protocol OS_ar_accessory_tracking_provider](os_ar_accessory_tracking_provider.md)
- [protocol OS_ar_camera_frame_samples](os_ar_camera_frame_samples.md)
- [protocol OS_ar_camera_region_anchor](os_ar_camera_region_anchor.md)
- [protocol OS_ar_camera_region_anchors](os_ar_camera_region_anchors.md)
- [protocol OS_ar_camera_region_configuration](os_ar_camera_region_configuration.md)
- [protocol OS_ar_camera_region_provider](os_ar_camera_region_provider.md)
- [protocol OS_ar_coordinate_space_data](os_ar_coordinate_space_data.md)
- [protocol OS_ar_device](os_ar_device.md)
- [protocol OS_ar_shared_coordinate_space_configuration](os_ar_shared_coordinate_space_configuration.md)
- [protocol OS_ar_shared_coordinate_space_provider](os_ar_shared_coordinate_space_provider.md)
- [protocol OS_ar_stereo_properties_configuration](os_ar_stereo_properties_configuration.md)
- [protocol OS_ar_stereo_properties_provider](os_ar_stereo_properties_provider.md)
- [protocol OS_ar_strings](os_ar_strings.md)
- [protocol OS_ar_viewpoint_properties](os_ar_viewpoint_properties.md)
### Structures
- [struct ARKitCoordinateSpace](arkitcoordinatespace.md)
  An object which represents an ARKit coordinate space.
- [struct Accessory](accessory.md)
  Represents an accessory to be tracked.
- [struct AccessoryAnchor](accessoryanchor.md)
  Represents a tracked accessory.
- [struct CameraRegionAnchor](cameraregionanchor.md)
  Represents a camera region anchor.
- [struct ViewpointProperties](viewpointproperties.md)
  The ViewpointProperties is a record of render camera transforms at some particular time.
### Type Aliases
- [typealias ar_device_t](ar_device_t.md)
### Enumerations
- [enum SurfaceClassification](surfaceclassification.md)
  A value describing the classification of a surface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ARKit)*