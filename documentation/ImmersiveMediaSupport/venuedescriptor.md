# VenueDescriptor

**Framework**: Immersive Media Support  
**Kind**: class  
**Role**: Class

The Apple Immersive Media Venue Descriptor is a collection of static metadata necessary for every Apple Immersive Video.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final actor VenueDescriptor
```

## Overview

This type contains information that includes camera definitions such as the lens calibration information, as well as data necessary for the rendering of the video frames.

## Topics

### Creating a venue descriptor
- [init(device: (any MTLDevice)?)](./venuedescriptor/init%28device%29.md)
  Creates an empty venue descriptor instance.
- [convenience init(aimeURL: URL, device: (any MTLDevice)?) async throws](./venuedescriptor/init%28aimeurl,device%29.md)
  Creates a venue descriptor instance from an AIME file.
### Configuring cameras
- [var cameras: [ImmersiveCamera]](./venuedescriptor/cameras.md)
  An array of all the immersive cameras contained in the venue descriptor (both original and dynamic).
- [func addCamera(ImmersiveCamera) throws](./venuedescriptor/addcamera%28_%29.md)
  Adds a new immersive camera definition to the venue descriptor.
- [func removeCamera(id: String) throws](./venuedescriptor/removecamera%28id%29.md)
  Removes an immersive camera definition from the venue descriptor.
- [func cameraViewModel(for: String) -> ImmersiveCameraViewModel?](./venuedescriptor/cameraviewmodel%28for%29.md)
  Returns the camera view model for the given immersive camera identifier.
### Saving a venue descriptor data
- [func save(to: URL) throws](./venuedescriptor/save%28to%29.md)
  Generates an AIME file at the specified location.
- [var aimeData: Data?](./venuedescriptor/aimedata.md)
  Property holding the complete static metadata needed for the immersive media playback.
### Initializers
- [init(aimeData: Data, device: (any MTLDevice)?) async throws](./venuedescriptor/init%28aimedata,device%29.md)
  Creates a venue descriptor instance from memory.

## Relationships

### Conforms To
- [Actor](../Swift/actor.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Camera metadata
- [struct ImmersiveCamera](./immersivecamera.md)
  A structure that holds the required information for an immersive media camera to process and render video frames.
- [struct ImmersiveCameraLensDefinition](./immersivecameralensdefinition.md)
  This type holds the ILPD lens configuration parameters to generate a camera calibration type instance.
- [struct ImmersiveCameraCalibration](./immersivecameracalibration.md)
  A structure that represents immersive media camera calibration data.
- [enum ImmersiveCameraMask](./immersivecameramask.md)
  A structure that holds the camera mask type information and its relevant mask name.
- [struct ImmersiveDynamicMask](./immersivedynamicmask.md)
  A type that holds the information required to dynamically generate an immersive media mask at load time.
- [class ImmersiveImageMask](./immersiveimagemask.md)
  An object that holds all the information needed to load immersive media masks from image data or from a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/venuedescriptor)*