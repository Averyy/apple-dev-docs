# virtualMemoryRegionInfo

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

Information about the region of memory an app accessed incorrectly, resulting in a bad-access crash.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.0
- macOS 12.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`virtualMemoryRegionInfo`](../crashdiagnostic/virtualmemoryregioninfo.md) instead.

## Declaration

```swift
var virtualMemoryRegionInfo: String? { get }
```

```objc
@property (strong, readonly, nullable) NSString * virtualMemoryRegionInfo;
```

## See Also

### Viewing exception details
- [var exceptionType: NSNumber?](./exceptiontype.md)
  The Mach exception type of the crash.
- [var exceptionCode: NSNumber?](./exceptioncode.md)
  The encoded processor-specific information for the crash.
- [var signal: NSNumber?](./signal.md)
  The signal associated with the crash.
- [var exceptionReason: MXCrashDiagnosticObjectiveCExceptionReason?](./exceptionreason.md)
- [var terminationReason: String?](./terminationreason.md)
  The reason the app was terminated as a human-readable string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxcrashdiagnostic/virtualmemoryregioninfo)*