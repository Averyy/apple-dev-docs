# exceptionReason

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 17.0+ - Deprecated in 27.2
- iPadOS 17.0+ - Deprecated in 27.2
- Mac Catalyst 17.0+ - Deprecated in 27.0
- macOS 14.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`exceptionReason`](../crashdiagnostic/exceptionreason.md) instead.

## Declaration

```swift
var exceptionReason: MXCrashDiagnosticObjectiveCExceptionReason? { get }
```

```objc
@property (strong, readonly, nullable) MXCrashDiagnosticObjectiveCExceptionReason * exceptionReason;
```

## See Also

### Viewing exception details
- [var exceptionType: NSNumber?](./exceptiontype.md)
  The Mach exception type of the crash.
- [var exceptionCode: NSNumber?](./exceptioncode.md)
  The encoded processor-specific information for the crash.
- [var signal: NSNumber?](./signal.md)
  The signal associated with the crash.
- [var terminationReason: String?](./terminationreason.md)
  The reason the app was terminated as a human-readable string.
- [var virtualMemoryRegionInfo: String?](./virtualmemoryregioninfo.md)
  Information about the region of memory an app accessed incorrectly, resulting in a bad-access crash.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxcrashdiagnostic/exceptionreason)*