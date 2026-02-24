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

- [Converting GPU timestamps into CPU time](converting-gpu-timestamps-into-cpu-time.md)
- [Converting a GPU’s counter data into a readable format](converting-a-gpus-counter-data-into-a-readable-format.md)

#### Return Value

A tuple that contains the CPU and GPU timestamps.

- **`cpu`**: A timestamp from the CPU.
- **`gpu`**: A timestamp from the GPU the device instance represents.

#### Discussion

For an example of how and when to use corresponding timestamps from the CPU and GPU, see [`Converting GPU timestamps into CPU time`](converting-gpu-timestamps-into-cpu-time.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/sampletimestamps())*