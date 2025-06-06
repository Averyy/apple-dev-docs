# terminationReason

**Framework**: MetricKit  
**Kind**: property

The reason the app was terminated as a human-readable string.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
var terminationReason: String? { get }
```

## See Also

- [var exceptionType: NSNumber?](mxcrashdiagnostic/exceptiontype.md)
  The Mach exception type of the crash.
- [var exceptionCode: NSNumber?](mxcrashdiagnostic/exceptioncode.md)
  The encoded processor-specific information for the crash.
- [var signal: NSNumber?](mxcrashdiagnostic/signal.md)
  The signal associated with the crash.
- [var exceptionReason: MXCrashDiagnosticObjectiveCExceptionReason?](mxcrashdiagnostic/exceptionreason.md)
- [var virtualMemoryRegionInfo: String?](mxcrashdiagnostic/virtualmemoryregioninfo.md)
  Information about the region of memory an app accessed incorrectly, resulting in a bad-access crash.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxcrashdiagnostic/terminationreason)*