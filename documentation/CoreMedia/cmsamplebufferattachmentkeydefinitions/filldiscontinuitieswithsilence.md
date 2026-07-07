# fillDiscontinuitiesWithSilence

**Framework**: Core Media  
**Kind**: property

Fill the difference between discontiguous sample buffers with silence.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
static let fillDiscontinuitiesWithSilence: CVAttachmentKeyDefinitionWithDefault<CMSampleBufferAttachmentKeyDefinitions.ShouldPropagate, Bool>
```

#### Discussion

If a sample buffer enters a buffer queue and the presentation time stamp between the previous buffer and the buffer with this attachment are discontiguous, handle the discontinuity by generating silence for the time difference. The getter returns the default value of false if this attachment is not present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebufferattachmentkeydefinitions/filldiscontinuitieswithsilence)*