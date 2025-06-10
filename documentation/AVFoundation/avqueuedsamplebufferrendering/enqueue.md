# enqueue(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Required**: Yes

Sends a sample buffer to the queue for rendering.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func enqueue(_ sampleBuffer: CMSampleBuffer)
```

#### Discussion

For video data, the sample buffer is processed according to the attachments it contains. If it has a true value for its [`kCMSampleAttachmentKey_DoNotDisplay`](https://developer.apple.com/documentation/CoreMedia/kCMSampleAttachmentKey_DoNotDisplay) attachment, the frame is decoded but not displayed. If it has a `true` value for its [`kCMSampleAttachmentKey_DisplayImmediately`](https://developer.apple.com/documentation/CoreMedia/kCMSampleAttachmentKey_DisplayImmediately) attachment, the frame is displayed as soon as possible, regardless of its presentation timestamp. Otherwise, the frame is displayed according to its presentation timestamp, relative to the timebase.

To schedule the removal of previous images at a specific timestamp, enqueue a marker sample buffer that doesn’t contain any samples, with the [`kCMSampleBufferAttachmentKey_EmptyMedia`](https://developer.apple.com/documentation/CoreMedia/kCMSampleBufferAttachmentKey_EmptyMedia) attachment set to [`kCFBooleanTrue`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanTrue).

> ❗ **Important**:  Attachments with the `kCMSampleAttachmentKey_` prefix must be set using [`CMSampleBufferGetSampleAttachmentsArray(_:createIfNecessary:)`](https://developer.apple.com/documentation/CoreMedia/CMSampleBufferGetSampleAttachmentsArray(_:createIfNecessary:)) and [`CFDictionarySetValue(_:_:_:)`](https://developer.apple.com/documentation/CoreFoundation/CFDictionarySetValue(_:_:_:)).  Attachments with the `kCMSampleBufferAttachmentKey_` prefix must be set via [`CMSetAttachment(_:key:value:attachmentMode:)`](https://developer.apple.com/documentation/CoreMedia/CMSetAttachment(_:key:value:attachmentMode:)).

## Parameters

- `sampleBuffer`: The sample buffer to be enqueued.

## See Also

- [var isReadyForMoreMediaData: Bool](avqueuedsamplebufferrendering/isreadyformoremediadata.md)
  A Boolean value that indicates whether the receiver is able to accept more sample buffers.
- [func requestMediaDataWhenReady(on: dispatch_queue_t, using: () -> Void)](avqueuedsamplebufferrendering/requestmediadatawhenready(on:using:).md)
  Tells the target to invoke a client-supplied block in order to gather sample buffers for playback.
- [func stopRequestingMediaData()](avqueuedsamplebufferrendering/stoprequestingmediadata.md)
  Cancels any current [`requestMediaDataWhenReady(on:using:)`](avqueuedsamplebufferrendering/requestmediadatawhenready(on:using:).md) call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avqueuedsamplebufferrendering/enqueue(_:))*