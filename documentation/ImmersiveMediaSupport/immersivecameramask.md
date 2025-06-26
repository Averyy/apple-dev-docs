# ImmersiveCameraMask

**Framework**: Immersive Media Support  
**Kind**: enum

A structure that holds the camera mask type information and its relevant mask name.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
enum ImmersiveCameraMask
```

## Topics

### Initializers
- [init(from: any Decoder) throws](immersivecameramask/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Methods
- [func encode(to: any Encoder) throws](immersivecameramask/encode(to:).md)
  Encodes this value into the given encoder.
### Enumeration Cases
- [case dynamic(ImmersiveDynamicMask)](immersivecameramask/dynamic(_:).md)
  A value defining a mask generated dynamically based on control points, see [`ImmersiveDynamicMask`](immersivedynamicmask.md) for details.
- [case image(ImmersiveImageMask)](immersivecameramask/image(_:).md)
  A value defining a mask generated based on an image, see [`ImmersiveImageMask`](immersiveimagemask.md) for details.

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