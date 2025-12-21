# objectID

**Framework**: AVFoundation  
**Kind**: property

A unique identifier for each detected object type (face, body, hands, heads and salient objects) in a collection.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var objectID: Int { get }
```

#### Discussion

Defaults to a value of -1 when invalid or not available. When used in conjunction with an [`AVCaptureMetadataOutput`](avcapturemetadataoutput.md), each newly detected object that enters the scene is assigned a unique identifier. [`objectID`](avmetadataobject/objectid.md)s are never re-used as objects leave the picture and new ones enter. Objects that leave the picture and then re-enter are assigned a new [`objectID`](avmetadataobject/objectid.md).

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataobject/objectid)*