# AVCaptureMetadataInput

**Framework**: AVFoundation  
**Kind**: class

A capture input for providing timed metadata to a capture session.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
class AVCaptureMetadataInput
```

#### Overview

This class provides input to an [`AVCaptureSession`](avcapturesession.md). An instance of [`AVCaptureMetadataInput`](avcapturemetadatainput.md) can present one and only one [`AVCaptureInput.Port`](avcaptureinput/port.md) connected to an [`AVCaptureMovieFileOutput`](avcapturemoviefileoutput.md). Provide metadata through the input port by conforming to a [`CMFormatDescription`](https://developer.apple.com/documentation/CoreMedia/CMFormatDescription) and supplying [`AVMetadataItem`](avmetadataitem.md) objects in an [`AVTimedMetadataGroup`](avtimedmetadatagroup.md).

## Topics

### Creating metadata input
- [init(formatDescription: CMMetadataFormatDescription, clock: CMClock)](avcapturemetadatainput/init(formatdescription:clock:).md)
  Creates capture metadata input to provide timed groups to a capture session.
### Providing metadata
- [func append(AVTimedMetadataGroup) throws](avcapturemetadatainput/append(_:).md)
  Provides metadata to the capture session.

## Relationships

### Inherits From
- [AVCaptureInput](avcaptureinput.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVCaptureMetadataOutput](avcapturemetadataoutput.md)
  A capture output for processing timed metadata produced by a capture session.
- [class AVMetadataObject](avmetadataobject.md)
  The abstract superclass for objects provided by a metadata capture output.
- [Metadata types](metadata-types.md)
  Inspect the supported metadata object types that the framework supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturemetadatainput)*