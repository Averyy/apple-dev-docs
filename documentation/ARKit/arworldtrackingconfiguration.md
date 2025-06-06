# ARWorldTrackingConfiguration

**Framework**: ARKit  
**Kind**: class

A configuration that tracks the position of a device in relation to objects in the environment.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class ARWorldTrackingConfiguration
```

## Mentions

- [Choosing Which Camera Feed to Augment](choosing-which-camera-feed-to-augment.md)

#### Overview

The [`ARWorldTrackingConfiguration`](arworldtrackingconfiguration.md) class tracks the device’s movement with six degrees of freedom (6DOF): the three rotation axes (roll, pitch, and yaw), and three translation axes (movement in x, y, and z).

This kind of tracking can create immersive AR experiences: A virtual object can appear to stay in the same place relative to the real world, even as the user tilts the device to look above or below the object, or moves the device around to see the object’s sides and back.

![Three illustrated variations of an iPhone running an app that displays an AR experience using the rear camera. The physical environment is depicted with a couch, in front of which, the app displays a virtual character. In the left picture, the iPhone views the couch straight on with the virtual character centered onscreen. In the middle picture, the device is rotated 30 degrees about the y-axis to the right, and the right-most portion of the couch and virtual character are visible onscreen only. In the right picture, the device is translated slightly to the left, and the left-most portions of the couch and virtual character are visible onscreen only.](https://docs-assets.developer.apple.com/published/8f5d9e55ef212af5eaf82adb0731cc5c/media-2923906%402x.png)

World-tracking sessions also provide several ways for your app to recognize or interact with elements of the real-world scene visible to the camera:

- Find real-world horizontal or vertical surfaces with [`planeDetection`](arworldtrackingconfiguration/planedetection-swift.property.md). Add the surfaces to the session as [`ARPlaneAnchor`](arplaneanchor.md) objects.
- Recognize and track the movement of 2D images with [`detectionImages`](arworldtrackingconfiguration/detectionimages.md). Add 2D images to the scene as [`ARImageAnchor`](arimageanchor.md) objects.
- Recognize 3D objects with [`detectionObjects`](arworldtrackingconfiguration/detectionobjects.md). Add 3D objects to the scene as [`ARObjectAnchor`](arobjectanchor.md) objects.
- Find the 3D positions of real-world features that correspond to a touch point on the device’s screen with ray casting.

## Topics

### Creating a Configuration
- [init()](arworldtrackingconfiguration/init.md)
  Initializes a new world-tracking configuration.
- [var initialWorldMap: ARWorldMap?](arworldtrackingconfiguration/initialworldmap.md)
  The state from a previous AR session to attempt to resume with this session configuration.
### Tracking Surfaces
- [var planeDetection: ARWorldTrackingConfiguration.PlaneDetection](arworldtrackingconfiguration/planedetection-swift.property.md)
  The configuration’s plane detection options.
- [ARWorldTrackingConfiguration.PlaneDetection](arworldtrackingconfiguration/planedetection-swift.struct.md)
  Options for whether and how the framework detects flat surfaces in captured images.
- [var sceneReconstruction: ARConfiguration.SceneReconstruction](arworldtrackingconfiguration/scenereconstruction.md)
  A flag that enables scene reconstruction.
- [class func supportsSceneReconstruction(ARConfiguration.SceneReconstruction) -> Bool](arworldtrackingconfiguration/supportsscenereconstruction(_:).md)
  Checks if the device supports scene reconstruction.
### Detecting or Tracking Images
- [var detectionImages: Set<ARReferenceImage>!](arworldtrackingconfiguration/detectionimages.md)
  A set of images that ARKit searches for in the user’s environment.
- [var maximumNumberOfTrackedImages: Int](arworldtrackingconfiguration/maximumnumberoftrackedimages.md)
  The number of image anchors to monitor closely for position and orientation updates.
- [var automaticImageScaleEstimationEnabled: Bool](arworldtrackingconfiguration/automaticimagescaleestimationenabled.md)
  A flag that instructs the framework to estimate and set the scale of a detected or tracked image on your behalf.
### Detecting 3D Objects
- [var detectionObjects: Set<ARReferenceObject>](arworldtrackingconfiguration/detectionobjects.md)
  A set of 3D objects that the framework attempts to detect in the user’s environment.
### Tracking the User’s Face
- [var userFaceTrackingEnabled: Bool](arworldtrackingconfiguration/userfacetrackingenabled.md)
  A flag that determines whether ARKit tracks the user’s face in a world-tracking session.
- [class var supportsUserFaceTracking: Bool](arworldtrackingconfiguration/supportsuserfacetracking.md)
  A Boolean value that tells you whether the iOS device supports tracking the user’s face during a world-tracking session.
### Creating Realistic Reflections
- [var environmentTexturing: ARWorldTrackingConfiguration.EnvironmentTexturing](arworldtrackingconfiguration/environmenttexturing-swift.property.md)
  An option that determines how the framework generates environment textures.
- [ARWorldTrackingConfiguration.EnvironmentTexturing](arworldtrackingconfiguration/environmenttexturing-swift.enum.md)
  The available environment texturing options for world tracking.
- [class AREnvironmentProbeAnchor](arenvironmentprobeanchor.md)
  An object that provides environmental lighting information for a specific area of space in a world-tracking AR session.
- [var wantsHDREnvironmentTextures: Bool](arworldtrackingconfiguration/wantshdrenvironmenttextures.md)
  A flag that instructs the framework to create environment textures in HDR format.
### Managing Device Camera Behavior
- [var isAutoFocusEnabled: Bool](arworldtrackingconfiguration/isautofocusenabled.md)
  A Boolean value that determines whether the device camera uses fixed focus or autofocus behavior.
### Enabling Collaboration
- [var isCollaborationEnabled: Bool](arworldtrackingconfiguration/iscollaborationenabled.md)
  A flag that opts you in to a peer-to-peer multiuser AR experience.
### Accessing App Clip Codes
- [Interacting with App Clip Codes in AR](../AppClip/interacting-with-app-clip-codes-in-ar.md)
  Display content and provide services in an AR experience with App Clip Codes.
- [class var supportsAppClipCodeTracking: Bool](arworldtrackingconfiguration/supportsappclipcodetracking.md)
  A flag that indicates if the device tracks App Clip Codes.
- [var appClipCodeTrackingEnabled: Bool](arworldtrackingconfiguration/appclipcodetrackingenabled.md)
  A Boolean value that indicates if the framework searches the physical environment for App Clip Codes.
- [class ARAppClipCodeAnchor](arappclipcodeanchor.md)
  An anchor that tracks the position and orientation of an App Clip Code in the physical environment.

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
- [class ARGeoTrackingConfiguration](argeotrackingconfiguration.md)
  A configuration that tracks locations with GPS, map data, and a device’s compass.
- [class AROrientationTrackingConfiguration](arorientationtrackingconfiguration.md)
  A configuration that tracks only the device’s orientation using the rear-facing camera.
- [class ARPositionalTrackingConfiguration](arpositionaltrackingconfiguration.md)
  A configuration that tracks only the device’s position in 3D space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arworldtrackingconfiguration)*