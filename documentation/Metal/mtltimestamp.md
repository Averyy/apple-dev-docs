# MTLTimestamp

**Framework**: Metal  
**Kind**: typealias

The number of nanoseconds for a point in absolute time or Mach absolute time.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias MTLTimestamp = UInt64
```

#### Discussion

The type of absolute time a Metal timestamp uses can vary with a system’s configuration, but it’s consistent for a configuration.

## See Also

- [Converting GPU Timestamps into CPU Time](converting-gpu-timestamps-into-cpu-time.md)
  Correlate GPU events with CPU timelines by calculating the CPU time equivalents for GPU timestamps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltimestamp)*