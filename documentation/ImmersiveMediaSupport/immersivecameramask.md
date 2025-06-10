# ImmersiveCameraMask

**Framework**: Immersive Media Support  
**Kind**: struct

A structure that holds the camera mask type information and its relevant mask name.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct ImmersiveCameraMask
```

## Topics

### Initializers
- [init(dynamicMaskName: String)](immersivecameramask/init(dynamicmaskname:).md)
  Initializes a mask using a dynamic mask.
- [init(filename: String)](immersivecameramask/init(filename:).md)
  Initializes a mask using an image file.
- [init(from: any Decoder) throws](immersivecameramask/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Methods
- [func encode(to: any Encoder) throws](immersivecameramask/encode(to:).md)
  Encodes this value into the given encoder.
### Enumerations
- [ImmersiveCameraMask.MaskType](immersivecameramask/masktype.md)
  Represents the type of the immersive media mask.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [actor VenueDescriptor](venuedescriptor.md)
  The Apple Immersive Media Venue Descriptor is a collection of static metadata necessary with every Apple Immersive Video.
- [struct ImmersiveCamera](immersivecamera.md)
  A structure that holds the required information for an immersive media camera to process and render video frames.
- [struct ImmersiveCameraCalibration](immersivecameracalibration.md)
  A structure that represents immersive media camera calibration data.
- [struct ImmersiveDynamicMask](immersivedynamicmask.md)
  A type that holds the information required to dynamically generate an immersive media mask at load time.
- [struct ImmersiveLensDefinition](immersivelensdefinition.md)
  This type holds the ILPD Meirives lens configuration parameters using which a camera calibration type instance can be generated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivecameramask)*