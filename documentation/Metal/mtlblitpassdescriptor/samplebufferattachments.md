# sampleBufferAttachments

**Framework**: Metal  
**Kind**: property

An array of counter sample buffer attachments that you configure for a blit pass.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var sampleBufferAttachments: MTLBlitPassSampleBufferAttachmentDescriptorArray { get }
```

#### Discussion

See [`Sampling GPU Data into Counter Sample Buffers`](sampling-gpu-data-into-counter-sample-buffers.md) for more context about configuring this property. That article is one of a series of articles in [`GPU Counters and Counter Sample Buffers`](gpu-counters-and-counter-sample-buffers.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblitpassdescriptor/samplebufferattachments)*