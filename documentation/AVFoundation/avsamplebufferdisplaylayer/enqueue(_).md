# enqueue(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Sends a sample buffer for display.

**Availability**:
- iOS 8.0+ - Deprecated in 18.0
- iPadOS 8.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.8+ - Deprecated in 15.0
- tvOS 10.2+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use sampleBufferRenderer's enqueueSampleBuffer: instead

## Declaration

```swift
func enqueue(_ sampleBuffer: CMSampleBuffer)
```

```objc
- (void) enqueueSampleBuffer:(CMSampleBufferRef) sampleBuffer;
```

## Discussion

Apple discourages the use of this symbol in iOS 17, tvOS 17, and macOS 14 and later. Use [`enqueue(_:)`](../avqueuedsamplebufferrendering/enqueue%28_%29.md) on the [`sampleBufferRenderer`](./samplebufferrenderer.md) instead.

If `sampleBuffer` has the [`kCMSampleAttachmentKey_DoNotDisplay`](../../CoreMedia/kcmsampleattachmentkey_donotdisplay.md) attachment set to [`kCFBooleanTrue`](../../CoreFoundation/kcfbooleantrue.md), the frame will be decoded but not displayed.

If `sampleBuffer` has the [`kCMSampleAttachmentKey_DisplayImmediately`](../../CoreMedia/kcmsampleattachmentkey_displayimmediately.md) attachment set to [`kCFBooleanTrue`](../../CoreFoundation/kcfbooleantrue.md), the decoded image will be displayed as soon as possible, replacing all previously enqueued images regardless of their timestamps.

Otherwise, the decoded image will be displayed at the `sampleBuffer` output presentation timestamp, as interpreted by the [`controlTimebase`](./controltimebase.md) property (or the `mach_absolute_time` timeline if there is no control timebase).

To schedule the removal of previous images at a specific timestamp, enqueue a marker sample buffer containing no samples, with the [`kCMSampleBufferAttachmentKey_EmptyMedia`](../../CoreMedia/kcmsamplebufferattachmentkey_emptymedia.md) attachment set to [`kCFBooleanTrue`](../../CoreFoundation/kcfbooleantrue.md).

> ❗ **Important**:  Attachments with the `kCMSampleAttachmentKey_*` prefix must be set via [`CMSampleBufferGetSampleAttachmentsArray(_:createIfNecessary:)`](../../CoreMedia/cmsamplebuffergetsampleattachmentsarray%28_,createifnecessary%29.md) and [`CFDictionarySetValue(_:_:_:)`](../../CoreFoundation/cfdictionarysetvalue%28_,_,_%29.md). Attachments with the `kCMSampleBufferAttachmentKey_*` prefix must be set via [`CMSetAttachment(_:key:value:attachmentMode:)`](../../CoreMedia/cmsetattachment%28_,key,value,attachmentmode%29.md).

## Parameters

- `sampleBuffer`: The sample buffer to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/enqueue(_:))*