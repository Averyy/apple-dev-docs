# time

**Framework**: AVFoundation  
**Kind**: property

The media time value associated with the metadata object.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 14.0+
- macOS 10.10+
- tvOS 9.0+

## Declaration

```swift
var time: CMTime { get }
```

#### Discussion

For captured media, this property represents the time when the metadata was captured. For metadata originating from a sample buffer ([`CMSampleBuffer`](https://developer.apple.com/documentation/CoreMedia/CMSampleBuffer)), the time is the sample buffer’s presentation time. If there is no valid time value associated with the metadata, this property should contain [`invalid`](https://developer.apple.com/documentation/CoreMedia/CMTime/invalid).

## See Also

- [var duration: CMTime](avmetadataobject/duration.md)
  The duration of the media associated with this metadata object.
- [var bounds: CGRect](avmetadataobject/bounds.md)
  The bounding rectangle associated with the metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataobject/time)*