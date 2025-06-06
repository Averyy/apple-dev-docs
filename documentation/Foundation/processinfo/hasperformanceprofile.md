# hasPerformanceProfile(_:)

**Framework**: Foundation  
**Kind**: method

Indicates whether an app is running under a known performance profile.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func hasPerformanceProfile(_ performanceProfile: NSProcessPerformanceProfile) -> Bool
```

#### Return Value

True if the system is running under the given performance profile. If the profile isn’t [`sustained`](https://developer.apple.com/documentation/Metal/NSProcessPerformanceProfile/sustained), the app might cause the device to throttle under a heavy workload.

## Parameters

- `performanceProfile`: The desired performance profile. Choose between:   and  .

## See Also

- [var processorCount: Int](processinfo/processorcount.md)
  The number of processing cores available on the computer.
- [var activeProcessorCount: Int](processinfo/activeprocessorcount.md)
  The number of active processing cores available on the computer.
- [var physicalMemory: UInt64](processinfo/physicalmemory.md)
  The amount of physical memory on the computer in bytes.
- [func isDeviceCertified(for: NSDeviceCertification) -> Bool](processinfo/isdevicecertified(for:).md)
  Indicates whether the device supports the requested performance tier.
- [var systemUptime: TimeInterval](processinfo/systemuptime.md)
  The amount of time the system has been awake since the last time it was restarted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/processinfo/hasperformanceprofile(_:))*