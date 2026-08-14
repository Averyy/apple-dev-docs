# ImmersiveImageMask

**Framework**: Immersive Media Support  
**Kind**: class

An object that holds all the information needed to load immersive media masks from image data or from a file.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final class ImmersiveImageMask
```

#### Overview

An image file containing the alpha values is used to generate the image mask.

## Topics

### Initializers
- [init(name: String, maskData: Data?)](immersiveimagemask/init(name:maskdata:).md)
- [init(name: String, maskURL: URL)](immersiveimagemask/init(name:maskurl:).md)
### Instance Properties
- [let maskData: Data?](immersiveimagemask/maskdata.md)
- [let name: String](immersiveimagemask/name.md)

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [actor VenueDescriptor](venuedescriptor.md)
  The Apple Immersive Media Venue Descriptor is a collection of static metadata necessary for every Apple Immersive Video.
- [struct ImmersiveCamera](immersivecamera.md)
  A structure that holds the required information for an immersive media camera to process and render video frames.
- [struct ImmersiveCameraLensDefinition](immersivecameralensdefinition.md)
  This type holds the ILPD lens configuration parameters to generate a camera calibration type instance.
- [struct ImmersiveCameraCalibration](immersivecameracalibration.md)
  A structure that represents immersive media camera calibration data.
- [enum ImmersiveCameraMask](immersivecameramask.md)
  A structure that holds the camera mask type information and its relevant mask name.
- [struct ImmersiveDynamicMask](immersivedynamicmask.md)
  A type that holds the information required to dynamically generate an immersive media mask at load time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersiveimagemask)*