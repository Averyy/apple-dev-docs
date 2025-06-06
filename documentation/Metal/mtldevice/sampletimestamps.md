# sampleTimestamps()

**Framework**: Metal  
**Kind**: method

Captures and returns a CPU timestamp and a GPU timestamp from the same moment in time.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
func sampleTimestamps() -> (cpu: MTLTimestamp, gpu: MTLTimestamp)
```

## Mentions

- [Converting GPU Timestamps into CPU Time](converting-gpu-timestamps-into-cpu-time.md)
- [Converting a GPU’s Counter Data into a Readable Format](converting-a-gpus-counter-data-into-a-readable-format.md)

#### Return Value

A tuple that contains the CPU and GPU timestamps.

#### Discussion

For an example of how and when to use corresponding timestamps from the CPU and GPU, see [`Converting GPU Timestamps into CPU Time`](converting-gpu-timestamps-into-cpu-time.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/sampletimestamps())*