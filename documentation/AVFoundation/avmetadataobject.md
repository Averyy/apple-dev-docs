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

### Inspecting the metadata
- [var bounds: CGRect](avmetadataobject/bounds.md)
  The bounding rectangle associated with the metadata.
- [var duration: CMTime](avmetadataobject/duration.md)
  The duration of the media associated with this metadata object.
- [var time: CMTime](avmetadataobject/time.md)
  The media time value associated with the metadata object.
- [var type: AVMetadataObject.ObjectType](avmetadataobject/type.md)
  The type of metadata that this object provides.
- [AVMetadataObject.ObjectType](avmetadataobject/objecttype.md)
  Constants that identify metadata object types.
- [var isFixedFocus: Bool](avmetadataobject/isfixedfocus.md)
  A BOOL indicating whether this metadata object represents a fixed focus.
- [var cinematicVideoFocusMode: AVCaptureDevice.CinematicVideoFocusMode](avmetadataobject/cinematicvideofocusmode.md)
  The current focus mode when an object is detected during a Cinematic Video recording.
- [var groupID: Int](avmetadataobject/groupid.md)
  An identifier associated with a metadata object used to group it with other metadata objects belonging to a common parent.
- [var objectID: Int](avmetadataobject/objectid.md)
  A unique identifier for each detected object type (face, body, hands, heads and salient objects) in a collection.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [AVMetadataBodyObject](avmetadatabodyobject.md)
- [AVMetadataCatHeadObject](avmetadatacatheadobject.md)
- [AVMetadataDogHeadObject](avmetadatadogheadobject.md)
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
- [Metadata types](metadata-types.md)
  Inspect the supported metadata object types that the framework supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataobject)*