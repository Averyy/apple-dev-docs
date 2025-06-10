# enqueue(_:)

**Framework**: AVFoundation  
**Kind**: method

Sends a sample buffer for display.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
func enqueue(_ sampleBuffer: CMSampleBuffer)
```

#### Discussion

Apple discourages the use of this symbol in iOS 17, tvOS 17, and macOS 14 and later. Use [`enqueue(_:)`](avqueuedsamplebufferrendering/enqueue(_:).md) on the [`sampleBufferRenderer`](avsamplebufferdisplaylayer/samplebufferrenderer.md) instead.

If `sampleBuffer` has the [`kCMSampleAttachmentKey_DoNotDisplay`](https://developer.apple.com/documentation/CoreMedia/kCMSampleAttachmentKey_DoNotDisplay) attachment set to [`kCFBooleanTrue`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanTrue), the frame will be decoded but not displayed.

If `sampleBuffer` has the [`kCMSampleAttachmentKey_DisplayImmediately`](https://developer.apple.com/documentation/CoreMedia/kCMSampleAttachmentKey_DisplayImmediately) attachment set to [`kCFBooleanTrue`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanTrue), the decoded image will be displayed as soon as possible, replacing all previously enqueued images regardless of their timestamps.

Otherwise, the decoded image will be displayed at the `sampleBuffer` output presentation timestamp, as interpreted by the [`controlTimebase`](avsamplebufferdisplaylayer/controltimebase.md) property (or the `mach_absolute_time` timeline if there is no control timebase).

To schedule the removal of previous images at a specific timestamp, enqueue a marker sample buffer containing no samples, with the [`kCMSampleBufferAttachmentKey_EmptyMedia`](https://developer.apple.com/documentation/CoreMedia/kCMSampleBufferAttachmentKey_EmptyMedia) attachment set to [`kCFBooleanTrue`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanTrue).

> ❗ **Important**:  Attachments with the `kCMSampleAttachmentKey_*` prefix must be set via [`CMSampleBufferGetSampleAttachmentsArray(_:createIfNecessary:)`](https://developer.apple.com/documentation/CoreMedia/CMSampleBufferGetSampleAttachmentsArray(_:createIfNecessary:)) and [`CFDictionarySetValue(_:_:_:)`](https://developer.apple.com/documentation/CoreFoundation/CFDictionarySetValue(_:_:_:)). Attachments with the `kCMSampleBufferAttachmentKey_*` prefix must be set via [`CMSetAttachment(_:key:value:attachmentMode:)`](https://developer.apple.com/documentation/CoreMedia/CMSetAttachment(_:key:value:attachmentMode:)).

## Parameters

- `sampleBuffer`: The sample buffer to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/enqueue(_:))*