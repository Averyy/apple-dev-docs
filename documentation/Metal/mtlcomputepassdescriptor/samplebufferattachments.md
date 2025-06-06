# sampleBufferAttachments

**Framework**: Metal  
**Kind**: property

The sample buffers that the compute pass can access.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var sampleBufferAttachments: MTLComputePassSampleBufferAttachmentDescriptorArray { get }
```

## Mentions

- [Sampling GPU Data into Counter Sample Buffers](sampling-gpu-data-into-counter-sample-buffers.md)

#### Discussion

The GPU uses sample buffers to record performance information. See [`GPU Counters and Counter Sample Buffers`](gpu-counters-and-counter-sample-buffers.md), [`Sampling GPU Data into Counter Sample Buffers`](sampling-gpu-data-into-counter-sample-buffers.md), and [`MTLCounter`](mtlcounter.md) for more information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputepassdescriptor/samplebufferattachments)*