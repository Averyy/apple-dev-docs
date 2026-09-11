# gradualDecoderRefresh

**Framework**: Core Media  
**Kind**: property

Indicates the decoder refresh count.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
static let gradualDecoderRefresh: CVAttachmentKeyDefinition<CMSampleBufferAttachmentKeyDefinitions.ShouldPropagate, Int16>
```

#### Discussion

Sample buffers with this attachment may be used to identify the audio decoder refresh count.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebufferattachmentkeydefinitions/gradualdecoderrefresh)*