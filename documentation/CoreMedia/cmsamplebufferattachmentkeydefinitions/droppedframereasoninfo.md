# droppedFrameReasonInfo

**Framework**: Core Media  
**Kind**: property

Indicates additional information regarding the dropped video frame.

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
static let droppedFrameReasonInfo: CVAttachmentKeyDefinition<CMSampleBufferAttachmentKeyDefinitions.ShouldPropagate, CMDroppedFrameReason.Info>
```

#### Discussion

Sample buffers with this attachment contain no image or data buffer. They mark a dropped video frame. If present, this attachment provides additional information about the reason described by the [`droppedFrameReason`](cmsamplebufferattachmentkeydefinitions/droppedframereason.md) key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebufferattachmentkeydefinitions/droppedframereasoninfo)*