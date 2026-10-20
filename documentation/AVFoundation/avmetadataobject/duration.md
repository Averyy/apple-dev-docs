# duration

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The duration of the media associated with this metadata object.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 14.0+
- macOS 10.10+
- tvOS 9.0+

## Declaration

```swift
var duration: CMTime { get }
```

```objc
@property (readonly) CMTime duration;
```

#### Discussion

For metadata originating from a sample buffer ([`CMSampleBuffer`](../../CoreMedia/cmsamplebuffer.md)), the duration reflects the duration of the sample buffer. If there is no valid duration value associated with the metadata, this property should contain [`invalid`](../../CoreMedia/cmtime/invalid.md).

## See Also

### Inspecting the metadata
- [var bounds: CGRect](./bounds.md)
  The bounding rectangle associated with the metadata.
- [var time: CMTime](./time.md)
  The media time value associated with the metadata object.
- [var type: AVMetadataObject.ObjectType](./type.md)
  The type of metadata that this object provides.
- [AVMetadataObject.ObjectType](./objecttype.md)
  Constants that identify metadata object types.
- [var isFixedFocus: Bool](./isfixedfocus.md)
  A BOOL indicating whether this metadata object represents a fixed focus.
- [var cinematicVideoFocusMode: AVCaptureDevice.CinematicVideoFocusMode](./cinematicvideofocusmode.md)
  The current focus mode when an object is detected during a Cinematic Video recording.
- [var groupID: Int](./groupid.md)
  An identifier associated with a metadata object used to group it with other metadata objects belonging to a common parent.
- [var objectID: Int](./objectid.md)
  A unique identifier for each detected object type (face, body, hands, heads, salient objects and focus-tracked objects) in a collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataobject/duration)*