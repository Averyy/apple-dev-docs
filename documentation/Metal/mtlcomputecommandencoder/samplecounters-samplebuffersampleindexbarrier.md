# sampleCounters(sampleBuffer:sampleIndex:barrier:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command to sample hardware counters, providing performance information.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func sampleCounters(sampleBuffer: any MTLCounterSampleBuffer, sampleIndex: Int, barrier: Bool)
```

## Mentions

- [Sampling GPU data into counter sample buffers](sampling-gpu-data-into-counter-sample-buffers.md)

#### Discussion

> ❗ **Important**:  To use a sample buffer, it needs to be part of the [`sampleBufferAttachments`](mtlcomputepassdescriptor/samplebufferattachments.md) on the compute pass descriptor.

See [`GPU counters and counter sample buffers`](gpu-counters-and-counter-sample-buffers.md), [`Sampling GPU data into counter sample buffers`](sampling-gpu-data-into-counter-sample-buffers.md), and [`MTLCounter`](mtlcounter.md) for more information.

## Parameters

- `sampleBuffer`: An   instance that stores the GPU hardware data.
- `sampleIndex`: An index within   the command stores the data to.
- `barrier`: The   parameter for the command has no impact on sampling commands from other passes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/samplecounters(samplebuffer:sampleindex:barrier:))*