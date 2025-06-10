# duration

**Framework**: AVFoundation  
**Kind**: property

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

#### Discussion

For metadata originating from a sample buffer ([`CMSampleBuffer`](https://developer.apple.com/documentation/CoreMedia/CMSampleBuffer)), the duration reflects the duration of the sample buffer. If there is no valid duration value associated with the metadata, this property should contain [`invalid`](https://developer.apple.com/documentation/CoreMedia/CMTime/invalid).

## See Also

- [var time: CMTime](avmetadataobject/time.md)
  The media time value associated with the metadata object.
- [var bounds: CGRect](avmetadataobject/bounds.md)
  The bounding rectangle associated with the metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataobject/duration)*