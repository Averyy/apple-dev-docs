# ImmersiveCameraMask

**Framework**: Immersive Media Support  
**Kind**: enum

A structure that holds the camera mask type information and its relevant mask name.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum ImmersiveCameraMask
```

## Topics

### Enumeration Cases
- [case dynamic(ImmersiveDynamicMask)](immersivecameramask/dynamic(_:).md)
  A value that defines a control points based dynamically generated mask.
- [case image(ImmersiveImageMask)](immersivecameramask/image(_:).md)
  A value that defines an image based mask.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [actor VenueDescriptor](venuedescriptor.md)
  The Apple Immersive Media Venue Descriptor is a collection of static metadata necessary for every Apple Immersive Video.
- [struct ImmersiveCamera](immersivecamera.md)
  A structure that holds the required information for an immersive media camera to process and render video frames.
- [struct ImmersiveCameraLensDefinition](immersivecameralensdefinition.md)
  This type holds the ILPD lens configuration parameters to generate a camera calibration type instance.
- [struct ImmersiveCameraCalibration](immersivecameracalibration.md)
  A structure that represents immersive media camera calibration data.
- [struct ImmersiveDynamicMask](immersivedynamicmask.md)
  A type that holds the information required to dynamically generate an immersive media mask at load time.
- [class ImmersiveImageMask](immersiveimagemask.md)
  An object that holds all the information needed to load immersive media masks from image data or from a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivecameramask)*