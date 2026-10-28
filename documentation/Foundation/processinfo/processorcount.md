# processorCount

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The number of processing cores available on the computer.

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
var processorCount: Int { get }
```

```objc
@property (readonly) NSUInteger processorCount;
```

## Discussion

This property value is equal to the result of entering the command `sysctl -n hw.ncpu` on the current system.

## See Also

### Getting computer information
- [var activeProcessorCount: Int](./activeprocessorcount.md)
  The number of active processing cores available on the computer.
- [var physicalMemory: UInt64](./physicalmemory.md)
  The amount of physical memory on the computer in bytes.
- [func isDeviceCertified(for: NSDeviceCertification) -> Bool](./isdevicecertified%28for%29.md)
  Indicates whether the device supports the requested performance tier.
- [func hasPerformanceProfile(NSProcessPerformanceProfile) -> Bool](./hasperformanceprofile%28_%29.md)
  Indicates whether an app is running under a known performance profile.
- [var systemUptime: TimeInterval](./systemuptime.md)
  The amount of time the system has been awake since the last time it was restarted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/processinfo/processorcount)*