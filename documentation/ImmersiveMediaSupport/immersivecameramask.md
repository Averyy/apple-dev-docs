# ImmersiveCameraMask

**Framework**: Immersive Media Support  
**Kind**: enum

A structure that holds the camera mask type information and its relevant mask name.

**Availability**:
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
- [struct ImmersiveCameraCalibration](immersivecameracalibration.md)
  A structure that represents immersive media camera calibration data.
- [struct ImmersiveDynamicMask](immersivedynamicmask.md)
  A type that holds the information required to dynamically generate an immersive media mask at load time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivecameramask)*