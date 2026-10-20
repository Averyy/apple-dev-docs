# type

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) AVMetadataObjectType type;
```

## See Also

### Inspecting the metadata
- [var bounds: CGRect](./bounds.md)
  The bounding rectangle associated with the metadata.
- [var duration: CMTime](./duration.md)
  The duration of the media associated with this metadata object.
- [var time: CMTime](./time.md)
  The media time value associated with the metadata object.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataobject/type)*