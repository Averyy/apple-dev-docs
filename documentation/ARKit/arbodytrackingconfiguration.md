# ARBodyTrackingConfiguration

**Framework**: ARKit  
**Kind**: class

A configuration that tracks human body poses, planar surfaces, and images using the rear-facing camera.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class ARBodyTrackingConfiguration
```

#### Overview

When ARKit identifies a person in the rear camera’s feed, it calls [`session(_:didAdd:)`](arsessiondelegate/session(_:didadd:).md), passing an [`ARBodyAnchor`](arbodyanchor.md) you can use to track the body’s movement.

When you enable plane detection and image detection, you can use a body anchor to display a virtual character and set the character on a surface or image that you choose.

By default, [`frameSemantics`](arconfiguration/framesemantics-swift.property.md) includes [`bodyDetection`](arconfiguration/framesemantics-swift.struct/bodydetection.md), which gives you access to the joint positions of a person that ARKit detects in the camera feed via the frame’s [`detectedBody`](arframe/detectedbody.md).

## Topics

### Creating a Configuration
- [init()](arbodytrackingconfiguration/init.md)
  Creates a new body tracking configuration.
- [var initialWorldMap: ARWorldMap?](arbodytrackingconfiguration/initialworldmap.md)
  The state from a previous AR session to attempt to resume with this session configuration.
### Estimating Body Scale
- [var automaticSkeletonScaleEstimationEnabled: Bool](arbodytrackingconfiguration/automaticskeletonscaleestimationenabled.md)
  A flag that determines whether ARKit estimates the height of a body that it’s tracking.
### Enabling Auto Focus
- [var isAutoFocusEnabled: Bool](arbodytrackingconfiguration/isautofocusenabled.md)
  A Boolean value that determines whether the device camera uses fixed focus or autofocus behavior.
### Enabling Plane Detection
- [var planeDetection: ARWorldTrackingConfiguration.PlaneDetection](arbodytrackingconfiguration/planedetection.md)
  A value specifying whether and how the session attempts to automatically detect flat surfaces in the camera-captured image.
- [ARWorldTrackingConfiguration.PlaneDetection](arworldtrackingconfiguration/planedetection-swift.struct.md)
  Options for whether and how the framework detects flat surfaces in captured images.
### Enabling Image Tracking
- [var automaticImageScaleEstimationEnabled: Bool](arbodytrackingconfiguration/automaticimagescaleestimationenabled.md)
  A flag that instructs ARKit to estimate and set the scale of a tracked image on your behalf.
- [var detectionImages: Set<ARReferenceImage>](arbodytrackingconfiguration/detectionimages.md)
  A set of images that ARKit searches for in the user’s environment.
- [var maximumNumberOfTrackedImages: Int](arbodytrackingconfiguration/maximumnumberoftrackedimages.md)
  The number of image anchors to monitor closely for position and orientation updates.
### Adding Realistic Reflections
- [var wantsHDREnvironmentTextures: Bool](arbodytrackingconfiguration/wantshdrenvironmenttextures.md)
  A flag that instructs ARKit to create environment textures in HDR format.
- [var environmentTexturing: ARWorldTrackingConfiguration.EnvironmentTexturing](arbodytrackingconfiguration/environmenttexturing.md)
  The behavior ARKit uses for generating environment textures.
### Accessing App Clip Codes
- [Interacting with App Clip Codes in AR](../AppClip/interacting-with-app-clip-codes-in-ar.md)
  Display content and provide services in an AR experience with App Clip Codes.
- [class var supportsAppClipCodeTracking: Bool](arbodytrackingconfiguration/supportsappclipcodetracking.md)
  A flag that indicates if the device tracks App Clip Codes.
- [var appClipCodeTrackingEnabled: Bool](arbodytrackingconfiguration/appclipcodetrackingenabled.md)
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

- [class ARFaceTrackingConfiguration](arfacetrackingconfiguration.md)
  A configuration that tracks facial movement and expressions using the front camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arbodytrackingconfiguration)*