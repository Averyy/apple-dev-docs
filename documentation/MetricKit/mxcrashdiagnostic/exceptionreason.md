# exceptionReason

**Framework**: MetricKit  
**Kind**: property

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var exceptionReason: MXCrashDiagnosticObjectiveCExceptionReason? { get }
```

## See Also

- [var exceptionType: NSNumber?](mxcrashdiagnostic/exceptiontype.md)
  The Mach exception type of the crash.
- [var exceptionCode: NSNumber?](mxcrashdiagnostic/exceptioncode.md)
  The encoded processor-specific information for the crash.
- [var signal: NSNumber?](mxcrashdiagnostic/signal.md)
  The signal associated with the crash.
- [var terminationReason: String?](mxcrashdiagnostic/terminationreason.md)
  The reason the app was terminated as a human-readable string.
- [var virtualMemoryRegionInfo: String?](mxcrashdiagnostic/virtualmemoryregioninfo.md)
  Information about the region of memory an app accessed incorrectly, resulting in a bad-access crash.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxcrashdiagnostic/exceptionreason)*