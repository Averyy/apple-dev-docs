# exceptionType

**Framework**: MetricKit  
**Kind**: property

The Mach exception type of the crash.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
var exceptionType: NSNumber? { get }
```

#### Discussion

Mach exception types are in the `usr/include/mach/exception_types.h` file in the SDK.

## See Also

- [var exceptionCode: NSNumber?](mxcrashdiagnostic/exceptioncode.md)
  The encoded processor-specific information for the crash.
- [var signal: NSNumber?](mxcrashdiagnostic/signal.md)
  The signal associated with the crash.
- [var exceptionReason: MXCrashDiagnosticObjectiveCExceptionReason?](mxcrashdiagnostic/exceptionreason.md)
- [var terminationReason: String?](mxcrashdiagnostic/terminationreason.md)
  The reason the app was terminated as a human-readable string.
- [var virtualMemoryRegionInfo: String?](mxcrashdiagnostic/virtualmemoryregioninfo.md)
  Information about the region of memory an app accessed incorrectly, resulting in a bad-access crash.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxcrashdiagnostic/exceptiontype)*