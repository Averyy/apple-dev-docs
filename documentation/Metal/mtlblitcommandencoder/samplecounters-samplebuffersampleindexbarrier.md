# sampleCounters(sampleBuffer:sampleIndex:barrier:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command that samples the GPU’s hardware counters during a blit pass and stores the data in a counter sample buffer.

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

- [Sampling GPU Data into Counter Sample Buffers](sampling-gpu-data-into-counter-sample-buffers.md)

#### Discussion

Inserting a barrier ensures that any work you encode with this encoder is complete before the GPU samples the hardware counters. If you don’t insert a barrier, the GPU can sample the counters concurrently with other commands you encode with this encoder. Using a barrier can help the counter results be more predictable and repeatable, but it may adversely affect your app’s runtime performance.

> **Note**:  The GPU doesn’t isolate this sampling command from any commands that come from another encoder, with or without a barrier.

## Parameters

- `sampleBuffer`: A counter sample buffer where the command stores the sample data.
- `sampleIndex`: A location within   where the command stores the sample data.
- `barrier`: A Boolean value that indicates whether the command inserts a barrier before taking the sample.

## See Also

- [func resolveCounters(any MTLCounterSampleBuffer, range: Range<Int>, destinationBuffer: any MTLBuffer, destinationOffset: Int)](mtlblitcommandencoder/resolvecounters(_:range:destinationbuffer:destinationoffset:).md)
  Encodes a command that resolves the data from the samples in a sample counter buffer and stores the results into a buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/samplecounters(samplebuffer:sampleindex:barrier:))*