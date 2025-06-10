# ARGeoTrackingConfiguration

**Framework**: ARKit  
**Kind**: class

A configuration that tracks locations with GPS, map data, and a device’s compass.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class ARGeoTrackingConfiguration
```

#### Overview

This configuration creates location anchors ([`ARGeoAnchor`](argeoanchor.md)) that specify a particular latitude, longitude, and optionally, altitude to enable an app to track geographic areas of interest in an AR experience.

> ❗ **Important**:  The [`isSupported`](arconfiguration/issupported.md) property returns [`true`](https://developer.apple.com/documentation/swift/true) for this class on iOS 14 & iPadOS 14 devices that have an A12 chip or later and cellular (GPS) capability. Geotracking is available in specific geographic locations. To determine availability at the user’s location at runtime, call [`checkAvailability(completionHandler:)`](argeotrackingconfiguration/checkavailability(completionhandler:).md).

Geotracking occurs exclusively outdoors. If a geotracking app navigates users between waypoints, your app needs to handle any events along a route. The user must have an internet connection, and you can provide them information about data usage, as described in [`ARGeoAnchor`](argeoanchor.md).

##### Encourage User Safety

To keep your users’ focus on the road while traveling, discourage them from looking at the device when in motion, such as while riding a bike. Keep users informed when navigating through unfamiliar territory. For instance, you can recommend they steer clear of private property, or remind them to check their device’s battery level before beginning a long route.

##### Refine the Users Position with Imagery

To place location anchors with precision, geotracking requires a better understanding of the user’s geographic location than is possible with GPS alone. Based on the user’s GPS coordinates, ARKit downloads imagery that depicts the physical environment in that area. Apple collects this  in advance by capturing photos of the view from the street and recording the geographic position at each photo. By comparing the device’s current camera image with this imagery, the session matches the user’s precise geographic location with the scene’s local coordinates. For information about the user’s position in local space, see [`transform`](arcamera/transform.md).

Localization imagery captures views from public streets and routes accessible by car, but doesn’t include images of gated or pedestrian-only areas.

Geotracking sessions use localization imagery in the [`ARGeoTrackingStatus.State.localizing`](argeotrackingstatus/state-swift.enum/localizing.md) state.

##### Supported Areas and Cities

Localization imagery is available for specific areas in over 20 countries, including many metropolitan areas in Australia, Europe, Japan, and North America. To check availability in a particular location, see the [`checkAvailability(completionHandler:)`](argeotrackingconfiguration/checkavailability(completionhandler:).md) function.

> 💡 **Tip**:  You can share an experience of geotracking with developers who live outside an area that supports it. Record a session in your app in an area that supports localization imagery for developers to create and test their geotracking app. For more information, see [`Recording and Replaying AR Session Data`](recording-and-replaying-ar-session-data.md).

## Topics

### Creating a configuration
- [init()](argeotrackingconfiguration/init.md)
  Initializes a new geotracking configuration.
### Checking availability
- [class func checkAvailability(completionHandler: (Bool, (any Error)?) -> Void)](argeotrackingconfiguration/checkavailability(completionhandler:).md)
  Determines if geotracking supports the user’s current location.
- [class func checkAvailability(at: CLLocationCoordinate2D, completionHandler: (Bool, (any Error)?) -> Void)](argeotrackingconfiguration/checkavailability(at:completionhandler:).md)
  Determines if geotracking supports a particular location.
### Tracking surfaces
- [var planeDetection: ARWorldTrackingConfiguration.PlaneDetection](argeotrackingconfiguration/planedetection.md)
  A value that specifies whether and how the session automatically attempts to detect flat surfaces in the camera-captured image.
- [ARWorldTrackingConfiguration.PlaneDetection](arworldtrackingconfiguration/planedetection-swift.struct.md)
  Options for whether and how the framework detects flat surfaces in captured images.
### Detecting or tracking images
- [var detectionImages: Set<ARReferenceImage>!](argeotrackingconfiguration/detectionimages.md)
  A set of images that ARKit searches for in the user’s environment.
- [var maximumNumberOfTrackedImages: Int](argeotrackingconfiguration/maximumnumberoftrackedimages.md)
  The number of image anchors to monitor closely for position and orientation updates.
- [var automaticImageScaleEstimationEnabled: Bool](argeotrackingconfiguration/automaticimagescaleestimationenabled.md)
  A flag that instructs the framework to estimate and set the scale of a detected or tracked image on your behalf.
### Detecting real-world objects
- [var detectionObjects: Set<ARReferenceObject>](argeotrackingconfiguration/detectionobjects.md)
  A set of 3D objects that the framework attempts to detect in the user’s environment.
### Creating realistic reflections
- [var environmentTexturing: ARWorldTrackingConfiguration.EnvironmentTexturing](argeotrackingconfiguration/environmenttexturing.md)
  An option that determines how the framework generates environment textures.
- [ARWorldTrackingConfiguration.EnvironmentTexturing](arworldtrackingconfiguration/environmenttexturing-swift.enum.md)
  The available environment texturing options for world tracking.
- [class AREnvironmentProbeAnchor](arenvironmentprobeanchor.md)
  An object that provides environmental lighting information for a specific area of space in a world-tracking AR session.
- [var wantsHDREnvironmentTextures: Bool](argeotrackingconfiguration/wantshdrenvironmenttextures.md)
  A flag that instructs the framework to create environment textures in HDR format.
### Accessing app clip codes
- [Interacting with App Clip Codes in AR](../AppClip/interacting-with-app-clip-codes-in-ar.md)
  Display content and provide services in an AR experience with App Clip Codes.
- [class var supportsAppClipCodeTracking: Bool](argeotrackingconfiguration/supportsappclipcodetracking.md)
  A flag that indicates if the device tracks App Clip Codes.
- [var appClipCodeTrackingEnabled: Bool](argeotrackingconfiguration/appclipcodetrackingenabled.md)
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
- [class ARWorldTrackingConfiguration](arworldtrackingconfiguration.md)
  A configuration that tracks the position of a device in relation to objects in the environment.
- [class AROrientationTrackingConfiguration](arorientationtrackingconfiguration.md)
  A configuration that tracks only the device’s orientation using the rear-facing camera.
- [class ARPositionalTrackingConfiguration](arpositionaltrackingconfiguration.md)
  A configuration that tracks only the device’s position in 3D space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeotrackingconfiguration)*