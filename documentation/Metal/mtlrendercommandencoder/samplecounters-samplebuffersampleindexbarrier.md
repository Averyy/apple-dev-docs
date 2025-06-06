# sampleCounters(sampleBuffer:sampleIndex:barrier:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command that samples hardware counters during the render pass and stores the data into a counter sample buffer.

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

## Parameters

- `sampleBuffer`: An   instance that stores the GPU hardware data.
- `sampleIndex`: An index within   the command stores the data to.
- `barrier`: Either way, the   parameter for the command has no impact on sampling commands from other passes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/samplecounters(samplebuffer:sampleindex:barrier:))*