# AVMetadataObject

**Framework**: AVFoundation  
**Kind**: class

The abstract superclass for objects provided by a metadata capture output.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 14.0+
- macOS 10.10+
- tvOS 9.0+

## Declaration

```swift
class AVMetadataObject
```

#### Overview

The `AVMetadataObject` class is an abstract class that defines the basic properties associated with a piece of metadata. These attributes reflect information either about the metadata itself or the media from which the metadata originated. Subclasses are responsible for providing appropriate values for each of the relevant properties.

You shouldn’t subclass `AVMetadataObject` directly. Instead, you use one of the defined subclasses provided by the AVFoundation framework. Similarly, you don’t create instances of this class yourself but use an [`AVCaptureMetadataOutput`](avcapturemetadataoutput.md) object to retrieve them from the captured data.

## Topics

### Getting the Type of Metadata
- [var type: AVMetadataObject.ObjectType](avmetadataobject/type.md)
  The type of metadata that this object provides.
- [AVMetadataObject.ObjectType](avmetadataobject/objecttype.md)
  Constants that identify metadata object types.
### Getting the Media-Related Attributes
- [var time: CMTime](avmetadataobject/time.md)
  The media time value associated with the metadata object.
- [var duration: CMTime](avmetadataobject/duration.md)
  The duration of the media associated with this metadata object.
- [var bounds: CGRect](avmetadataobject/bounds.md)
  The bounding rectangle associated with the metadata.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [AVMetadataBodyObject](avmetadatabodyobject.md)
- [AVMetadataFaceObject](avmetadatafaceobject.md)
- [AVMetadataMachineReadableCodeObject](avmetadatamachinereadablecodeobject.md)
- [AVMetadataSalientObject](avmetadatasalientobject.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVCaptureMetadataInput](avcapturemetadatainput.md)
  A capture input for providing timed metadata to a capture session.
- [class AVCaptureMetadataOutput](avcapturemetadataoutput.md)
  A capture output for processing timed metadata produced by a capture session.
- [Metadata Types](metadata-types.md)
  Inspect the supported metadata object types that the framework supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataobject)*