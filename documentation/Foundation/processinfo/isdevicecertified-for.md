# isDeviceCertified(for:)

**Framework**: Foundation  
**Kind**: method

Indicates whether the device supports the requested performance tier.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func isDeviceCertified(for performanceTier: NSDeviceCertification) -> Bool
```

#### Return Value

`True` if the device meets the requirements for the given performance tier.

## Parameters

- `performanceTier`: The desired system performance tier.   is the only performance tier.

## See Also

- [var processorCount: Int](processinfo/processorcount.md)
  The number of processing cores available on the computer.
- [var activeProcessorCount: Int](processinfo/activeprocessorcount.md)
  The number of active processing cores available on the computer.
- [var physicalMemory: UInt64](processinfo/physicalmemory.md)
  The amount of physical memory on the computer in bytes.
- [func hasPerformanceProfile(NSProcessPerformanceProfile) -> Bool](processinfo/hasperformanceprofile(_:).md)
  Indicates whether an app is running under a known performance profile.
- [var systemUptime: TimeInterval](processinfo/systemuptime.md)
  The amount of time the system has been awake since the last time it was restarted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/processinfo/isdevicecertified(for:))*