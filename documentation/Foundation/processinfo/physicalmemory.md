# physicalMemory

**Framework**: Foundation  
**Kind**: property

The amount of physical memory on the computer in bytes.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var physicalMemory: UInt64 { get }
```

## See Also

- [var processorCount: Int](processinfo/processorcount.md)
  The number of processing cores available on the computer.
- [var activeProcessorCount: Int](processinfo/activeprocessorcount.md)
  The number of active processing cores available on the computer.
- [func isDeviceCertified(for: NSDeviceCertification) -> Bool](processinfo/isdevicecertified(for:).md)
  Indicates whether the device supports the requested performance tier.
- [func hasPerformanceProfile(NSProcessPerformanceProfile) -> Bool](processinfo/hasperformanceprofile(_:).md)
  Indicates whether an app is running under a known performance profile.
- [var systemUptime: TimeInterval](processinfo/systemuptime.md)
  The amount of time the system has been awake since the last time it was restarted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/processinfo/physicalmemory)*