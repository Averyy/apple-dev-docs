# droppedFrameReasonInfo

**Framework**: Core Media  
**Kind**: property

Indicates additional information regarding the dropped video frame.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
static let droppedFrameReasonInfo: CVAttachmentKeyDefinition<CMSampleBufferAttachmentKeyDefinitions.ShouldPropagate, CMDroppedFrameReason.Info>
```

#### Discussion

Sample buffers with this attachment contain no image or data buffer. They mark a dropped video frame. If present, this attachment provides additional information about the reason described by the [`droppedFrameReason`](cmsamplebufferattachmentkeydefinitions/droppedframereason.md) key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebufferattachmentkeydefinitions/droppedframereasoninfo)*