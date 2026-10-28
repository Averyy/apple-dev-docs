# sampleTimestamps:gpuTimestamp:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Captures and returns a CPU timestamp and a GPU timestamp from the same moment in time.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```objc
- (void) sampleTimestamps:(MTLTimestamp *) cpuTimestamp gpuTimestamp:(MTLTimestamp *) gpuTimestamp;
```

## Mentions

- [Converting GPU timestamps into CPU time](../converting-gpu-timestamps-into-cpu-time.md)

## Discussion

For an example of how and when to use corresponding timestamps from the CPU and GPU, see [Converting GPU timestamps into CPU time](../converting-gpu-timestamps-into-cpu-time.md).

## Parameters

- `cpuTimestamp`: A pointer the method uses to save a timestamp from the CPU.
- `gpuTimestamp`: A pointer the method uses to save a timestamp from the GPU the device instance represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/sampletimestamps:gputimestamp:)*