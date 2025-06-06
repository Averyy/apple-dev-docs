# sampleCounters(sampleBuffer:sampleIndex:barrier:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command to sample hardware counters at this point in the acceleration structure pass and store the samples into a counter sample buffer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func sampleCounters(sampleBuffer: any MTLCounterSampleBuffer, sampleIndex: Int, barrier: Bool)
```

## Mentions

- [Sampling GPU Data into Counter Sample Buffers](sampling-gpu-data-into-counter-sample-buffers.md)

#### Discussion

Inserting a barrier ensures that any work you encoded with this encoder is complete before the GPU samples the hardware counters. If you don’t insert a barrier, the GPU can sample the counters concurrently with other commands encoded by this encoder. Using a barrier leads to more repeatable counter results but can negatively impact performance.

Regardless of whether you set a barrier, the GPU doesn’t isolate the sampling from work encoded by other encoders.

## Parameters

- `sampleBuffer`: The sample buffer to sample into.
- `sampleIndex`: The index in the counter buffer to write the sample.
- `barrier`: A Boolean value that states whether to insert a barrier before taking the sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructurecommandencoder/samplecounters(samplebuffer:sampleindex:barrier:))*