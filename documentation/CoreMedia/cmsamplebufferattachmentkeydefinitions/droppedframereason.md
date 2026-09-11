# droppedFrameReason

**Framework**: Core Media  
**Kind**: property

Indicates the reason the current video frame was dropped.

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
static let droppedFrameReason: CVAttachmentKeyDefinition<CMSampleBufferAttachmentKeyDefinitions.ShouldPropagate, CMDroppedFrameReason>
```

#### Discussion

Sample buffers with this attachment contain no image or data buffer. They mark a dropped video frame. This attachment identifies the reason the frame was dropped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebufferattachmentkeydefinitions/droppedframereason)*