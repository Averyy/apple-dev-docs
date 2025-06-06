# AVMetadataFaceObject

**Framework**: AVFoundation  
**Kind**: class

Face information detected by a metadata capture output.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 14.0+
- macOS 10.10+
- tvOS 9.0+

## Declaration

```swift
class AVMetadataFaceObject
```

## Mentions

- [Configuring Camera Capture to Collect a Portrait Effects Matte](configuring-camera-capture-to-collect-a-portrait-effects-matte.md)

#### Overview

The `AVMetadataFaceObject` class is a concrete subclass of [`AVMetadataObject`](avmetadataobject.md) that defines the features of a single detected face. You can retrieve instances of this class from the output of an [`AVCaptureMetadataOutput`](avcapturemetadataoutput.md) object on devices that support face detection.

## Topics

### Getting the Face Identifier
- [var faceID: Int](avmetadatafaceobject/faceid.md)
  The unique ID for this face metadata object.
### Accessing the Face Detection Data
- [var hasRollAngle: Bool](avmetadatafaceobject/hasrollangle.md)
  A Boolean value indicating whether there is a valid roll angle associated with the face.
- [var rollAngle: CGFloat](avmetadatafaceobject/rollangle.md)
  The roll angle of the face specified in degrees.
- [var hasYawAngle: Bool](avmetadatafaceobject/hasyawangle.md)
  A Boolean value indicating whether there is a valid yaw angle associated with the face.
- [var yawAngle: CGFloat](avmetadatafaceobject/yawangle.md)
  The yaw angle of the face specified in degrees.
### Constants
- [Face Metadata Type](face-metadata-type.md)
  A metadata type string for face detection metadata.

## Relationships

### Inherits From
- [AVMetadataObject](avmetadataobject.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadatafaceobject)*