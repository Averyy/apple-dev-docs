# type

**Framework**: AVFoundation  
**Kind**: property

The type of metadata that this object provides.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 14.0+
- macOS 10.10+
- tvOS 9.0+

## Declaration

```swift
var type: AVMetadataObject.ObjectType { get }
```

## See Also

- [var bounds: CGRect](avmetadataobject/bounds.md)
  The bounding rectangle associated with the metadata.
- [var duration: CMTime](avmetadataobject/duration.md)
  The duration of the media associated with this metadata object.
- [var time: CMTime](avmetadataobject/time.md)
  The media time value associated with the metadata object.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataobject/type)*