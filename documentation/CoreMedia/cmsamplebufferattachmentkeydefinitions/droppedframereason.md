# droppedFrameReason

**Framework**: Core Media  
**Kind**: property

Indicates the reason the current video frame was dropped.

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
static let droppedFrameReason: CVAttachmentKeyDefinition<CMSampleBufferAttachmentKeyDefinitions.ShouldPropagate, CMDroppedFrameReason>
```

#### Discussion

Sample buffers with this attachment contain no image or data buffer. They mark a dropped video frame. This attachment identifies the reason the frame was dropped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebufferattachmentkeydefinitions/droppedframereason)*