# enqueue(_:)

**Framework**: AVFoundation  
**Kind**: method

Sends a sample buffer in order to render its contents.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func enqueue(_ sampleBuffer: CMSampleBuffer)
```

#### Discussion

Video-specific notes:

If sampleBuffer has the kCMSampleAttachmentKey_DoNotDisplay attachment set to kCFBooleanTrue, the frame will be decoded but not displayed. Otherwise, if sampleBuffer has the kCMSampleAttachmentKey_DisplayImmediately attachment set to kCFBooleanTrue, the decoded image will be displayed as soon as possible, replacing all previously enqueued images regardless of their timestamps. Otherwise, the decoded image will be displayed at sampleBuffer’s output presentation timestamp, as interpreted by the timebase.

To schedule the removal of previous images at a specific timestamp, enqueue a marker sample buffer containing no samples, with the kCMSampleBufferAttachmentKey_EmptyMedia attachment set to kCFBooleanTrue.

IMPORTANT NOTE: attachments with the kCMSampleAttachmentKey_ prefix must be set via CMSampleBufferGetSampleAttachmentsArray and CFDictionarySetValue. Attachments with the kCMSampleBufferAttachmentKey_ prefix must be set via CMSetAttachment.

The combination of either a non-NULL controlTimebase or an AVSampleBufferRenderSynchronizer with the use of kCMSampleAttachmentKey_DisplayImmediately as an attachment to the CMSampleBuffers that are enqueued for display is not recommended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer/enqueue(_:))*