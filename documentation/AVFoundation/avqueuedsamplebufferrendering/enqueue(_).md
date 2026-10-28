# enqueue(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sends a sample buffer to the queue for rendering.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.13+ - Deprecated in 27.0
- tvOS 11.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

## Declaration

```swift
func enqueue(_ sampleBuffer: CMSampleBuffer)
```

```objc
- (void) enqueueSampleBuffer:(CMSampleBufferRef) sampleBuffer;
```

## Discussion

For video data, the sample buffer is processed according to the attachments it contains. If it has a true value for its [`kCMSampleAttachmentKey_DoNotDisplay`](../../CoreMedia/kcmsampleattachmentkey_donotdisplay.md) attachment, the frame is decoded but not displayed. If it has a `true` value for its [`kCMSampleAttachmentKey_DisplayImmediately`](../../CoreMedia/kcmsampleattachmentkey_displayimmediately.md) attachment, the frame is displayed as soon as possible, regardless of its presentation timestamp. Otherwise, the frame is displayed according to its presentation timestamp, relative to the timebase.

To schedule the removal of previous images at a specific timestamp, enqueue a marker sample buffer that doesn’t contain any samples, with the [`kCMSampleBufferAttachmentKey_EmptyMedia`](../../CoreMedia/kcmsamplebufferattachmentkey_emptymedia.md) attachment set to [`kCFBooleanTrue`](../../CoreFoundation/kcfbooleantrue.md).

> ❗ **Important**:  Attachments with the `kCMSampleAttachmentKey_` prefix must be set using [`CMSampleBufferGetSampleAttachmentsArray(_:createIfNecessary:)`](../../CoreMedia/cmsamplebuffergetsampleattachmentsarray%28_,createifnecessary%29.md) and [`CFDictionarySetValue(_:_:_:)`](../../CoreFoundation/cfdictionarysetvalue%28_,_,_%29.md).  Attachments with the `kCMSampleBufferAttachmentKey_` prefix must be set via [`CMSetAttachment(_:key:value:attachmentMode:)`](../../CoreMedia/cmsetattachment%28_,key,value,attachmentmode%29.md).

## Parameters

- `sampleBuffer`: The sample buffer to be enqueued.

## See Also

### Requesting media
- [var isReadyForMoreMediaData: Bool](./isreadyformoremediadata.md)
  A Boolean value that indicates whether the receiver is able to accept more sample buffers.
- [func requestMediaDataWhenReady(on: dispatch_queue_t, using: () -> Void)](./requestmediadatawhenready%28on,using%29.md)
  Tells the target to invoke a client-supplied block in order to gather sample buffers for playback.
- [func stopRequestingMediaData()](./stoprequestingmediadata%28%29.md)
  Cancels any current [`requestMediaDataWhenReady(on:using:)`](./requestmediadatawhenready%28on,using%29.md) call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avqueuedsamplebufferrendering/enqueue(_:))*