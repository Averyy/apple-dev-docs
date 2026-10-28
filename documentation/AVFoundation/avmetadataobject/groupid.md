# groupID

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

An identifier associated with a metadata object used to group it with other metadata objects belonging to a common parent.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var groupID: Int { get }
```

```objc
@property (readonly) NSInteger groupID;
```

## Discussion

When presented with a collection of [`AVMetadataObject`](../avmetadataobject.md) instances of different types, you may use the objects’ [`groupID`](./groupid.md) to combine them into groups. For example, a human body and face belonging to the same person have the same [`groupID`](./groupid.md).  If an object’s [`groupID`](./groupid.md) property is set to -1, it is invalid. When set to a value of >=0, it is unique across all object groups.

## See Also

### Inspecting the metadata
- [var bounds: CGRect](./bounds.md)
  The bounding rectangle associated with the metadata.
- [var duration: CMTime](./duration.md)
  The duration of the media associated with this metadata object.
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
- [var objectID: Int](./objectid.md)
  A unique identifier for each detected object type (face, body, hands, heads, salient objects and focus-tracked objects) in a collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataobject/groupid)*