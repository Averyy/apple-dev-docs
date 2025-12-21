# bounds

**Framework**: AVFoundation  
**Kind**: property

The bounding rectangle associated with the metadata.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 14.0+
- macOS 10.10+
- tvOS 9.0+

## Declaration

```swift
var bounds: CGRect { get }
```

#### Discussion

The bounding rectangle is specified relative to the picture or video of the corresponding media. The rectangle’s origin is always specified in the top-left corner, and the x and y axis extend down and to the right.

If the metadata has no bounding rectangle, the value of this property should be [`CGRectZero`](https://developer.apple.com/documentation/CoreGraphics/CGRectZero).

For video content, the bounding rectangle may be expressed using scalar values in the range 0.0 to 1.0. Scalar values remain meaningful even when the original video has been scaled down.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataobject/bounds)*