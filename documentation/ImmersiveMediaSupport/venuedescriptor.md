# VenueDescriptor

**Framework**: Immersive Media Support  
**Kind**: class

The Apple Immersive Media Venue Descriptor is a collection of static metadata necessary for every Apple Immersive Video.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
final actor VenueDescriptor
```

#### Overview

This descriptor contains information about the venue in which this movie was captured. This information includes camera definitions such as the lens calibration information, as well as data required for the rendering of the video captured by the cameras.

## Topics

### Creating a venue descriptor
- [init(device: (any MTLDevice)?)](venuedescriptor/init(device:).md)
  Creates an empty `VenueDescriptor`, useful when creating a new `VenueDescriptor` in code (other than loading from an AIME file).
- [convenience init(aimeURL: URL, device: (any MTLDevice)?) async throws](venuedescriptor/init(aimeurl:device:).md)
  Initializes a `VenueDescriptor` instance from an AIME file.
### Configuring cameras
- [var cameras: [ImmersiveCamera]](venuedescriptor/cameras.md)
  Property contains information about all the ImmersiveCameras contained in this `VenueDescriptor`.
- [func addCamera(ImmersiveCamera) throws](venuedescriptor/addcamera(_:).md)
  Adds a new `ImmersiveCamera` definition to this `VenueDescriptor`.
- [func removeCamera(id: String) throws](venuedescriptor/removecamera(id:).md)
  Removes an `ImmersiveCamera` definition from this `VenueDescriptor`.
- [func cameraViewModel(for: String) -> ImmersiveCameraViewModel?](venuedescriptor/cameraviewmodel(for:).md)
  Returns the camera view model for the given immersive camera identifier.
### Saving a venue descriptor data
- [func save(to: URL) throws](venuedescriptor/save(to:).md)
  Generates an AIME file at the specified location
- [var aimeData: Data?](venuedescriptor/aimedata.md)
  Property holding the complete static metadata needed for the immersive media playback.
### Accessing the executor
- [var unownedExecutor: UnownedSerialExecutor](venuedescriptor/unownedexecutor.md)
  Retrieve the executor for this actor as an optimized, unowned reference.
### Initializers
- [init(aimeData: Data, device: (any MTLDevice)?) async throws](venuedescriptor/init(aimedata:device:).md)
  Initializes an `VenueDescriptor` instance from memory.
### Default Implementations
- [Actor Implementations](venuedescriptor/actor-implementations.md)

## Relationships

### Conforms To
- [Actor](../Swift/Actor.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct ImmersiveCamera](immersivecamera.md)
  A structure that holds the required information for an immersive media camera to process and render video frames.
- [struct ImmersiveCameraCalibration](immersivecameracalibration.md)
  A structure that represents immersive media camera calibration data.
- [enum ImmersiveCameraMask](immersivecameramask.md)
  A structure that holds the camera mask type information and its relevant mask name.
- [struct ImmersiveDynamicMask](immersivedynamicmask.md)
  A type that holds the information required to dynamically generate an immersive media mask at load time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/venuedescriptor)*