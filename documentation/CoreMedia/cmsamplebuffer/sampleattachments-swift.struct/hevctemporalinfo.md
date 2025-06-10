# hevcTemporalInfo

**Framework**: Core Media  
**Kind**: property

Indicates a video frame’s level within a hierarchical frame dependency structure.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
var hevcTemporalInfo: CMSampleBuffer.HEVCTemporalInfo? { get set }
```

#### Discussion

When present, the temporal level attachments among a group of video frames provide information about where inter-frame dependencies may and may not exist.

This attachment is read from and written to media files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/sampleattachments-swift.struct/hevctemporalinfo)*