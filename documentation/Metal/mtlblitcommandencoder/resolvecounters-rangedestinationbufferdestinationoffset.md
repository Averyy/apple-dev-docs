# resolveCounters(_:range:destinationBuffer:destinationOffset:)

**Framework**: Metal  
**Kind**: method

Encodes a command that resolves the data from the samples in a sample counter buffer and stores the results into a buffer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
func resolveCounters(_ sampleBuffer: any MTLCounterSampleBuffer, range: Range<Int>, destinationBuffer: any MTLBuffer, destinationOffset: Int)
```

## Mentions

- [Converting a GPU’s Counter Data into a Readable Format](converting-a-gpus-counter-data-into-a-readable-format.md)

#### Discussion

For an example of how and when to use this method, see [`Converting a GPU’s Counter Data into a Readable Format`](converting-a-gpus-counter-data-into-a-readable-format.md).

> **Note**:  The GPU stores [`MTLCounterErrorValue`](mtlcountererrorvalue.md) in `destinationBuffer` each time it encounters an error resolving a sample.

 The GPU stores [`MTLCounterErrorValue`](mtlcountererrorvalue.md) in `destinationBuffer` each time it encounters an error resolving a sample.

## Parameters

- `sampleBuffer`: A counter sample buffer source that contains the sample data.
- `range`: A range that indicates which of the buffer’s samples the command resolves.
- `destinationBuffer`: A destination buffer where the command stores the data it resolves.
- `destinationOffset`: A starting offset, in bytes, within   where the blit pass writes the first byte of the data it resolves.

## See Also

- [func sampleCounters(sampleBuffer: any MTLCounterSampleBuffer, sampleIndex: Int, barrier: Bool)](mtlblitcommandencoder/samplecounters(samplebuffer:sampleindex:barrier:).md)
  Encodes a command that samples the GPU’s hardware counters during a blit pass and stores the data in a counter sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/resolvecounters(_:range:destinationbuffer:destinationoffset:))*