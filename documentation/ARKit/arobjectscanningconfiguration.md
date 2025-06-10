# ARObjectScanningConfiguration

**Framework**: ARKit  
**Kind**: class

A configuration that recognizes objects and collects high-fidelity data about specific objects using the rear-facing camera.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class ARObjectScanningConfiguration
```

#### Overview

To create an app that recognizes objects in the physical environment, first you scan them during development using `ARObjectScanningConfiguration`. After you’ve scanned an object, call [`createReferenceObject(transform:center:extent:completionHandler:)`](arsession/createreferenceobject(transform:center:extent:completionhandler:).md) to turn it into an [`ARReferenceObject`](arreferenceobject.md) that you can use to detect it again at run-time. When users run your app, you ask ARKit to look for your scanned obects by running a world tracking configuration and assigning reference objects to its [`detectionObjects`](arworldtrackingconfiguration/detectionobjects.md) property.

> ❗ **Important**:  `ARObjectScanningConfiguration` is for use only in development scenarios. Because the high-fidelity spatial mapping required by object scanning has a high performance and energy cost, many ARKit features are disabled that aren’t required for object scanning.

## Topics

### Creating a Configuration
- [init()](arobjectscanningconfiguration/init.md)
  Initializes a new object scanning configuration.
### Enabling Plane Detection
- [var planeDetection: ARWorldTrackingConfiguration.PlaneDetection](arobjectscanningconfiguration/planedetection.md)
  A value specifying whether and how the session attempts to automatically detect flat surfaces in the camera-captured image.
- [ARWorldTrackingConfiguration.PlaneDetection](arworldtrackingconfiguration/planedetection-swift.struct.md)
  Options for whether and how the framework detects flat surfaces in captured images.
### Managing Device Camera Behavior
- [var isAutoFocusEnabled: Bool](arobjectscanningconfiguration/isautofocusenabled.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arobjectscanningconfiguration)*