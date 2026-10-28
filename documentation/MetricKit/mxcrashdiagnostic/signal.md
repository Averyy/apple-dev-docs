# signal

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The signal associated with the crash.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.0
- macOS 12.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`signal`](../crashdiagnostic/signal.md) instead.

## Declaration

```swift
var signal: NSNumber? { get }
```

```objc
@property (strong, readonly, nullable) NSNumber * signal;
```

## Discussion

Processor-specific information is in the `usr/include/sys/signal.h` file in the SDK.

## See Also

### Viewing exception details
- [var exceptionType: NSNumber?](./exceptiontype.md)
  The Mach exception type of the crash.
- [var exceptionCode: NSNumber?](./exceptioncode.md)
  The encoded processor-specific information for the crash.
- [var exceptionReason: MXCrashDiagnosticObjectiveCExceptionReason?](./exceptionreason.md)
- [var terminationReason: String?](./terminationreason.md)
  The reason the app was terminated as a human-readable string.
- [var virtualMemoryRegionInfo: String?](./virtualmemoryregioninfo.md)
  Information about the region of memory an app accessed incorrectly, resulting in a bad-access crash.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxcrashdiagnostic/signal)*