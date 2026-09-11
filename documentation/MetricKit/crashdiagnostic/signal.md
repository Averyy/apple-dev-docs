# signal

**Framework**: MetricKit  
**Kind**: property

The signal associated with this crash.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
let signal: Int?
```

## See Also

- [let exceptionType: Int?](crashdiagnostic/exceptiontype.md)
  The name of the Mach exception that terminated the app.
- [let exceptionCode: UInt64?](crashdiagnostic/exceptioncode.md)
  Processor specific information about the exception.
- [let exceptionReason: CrashDiagnostic.ObjectiveCExceptionReason?](crashdiagnostic/exceptionreason.md)
  The exception reason for an uncaught ObjC exception.
- [let virtualMemoryRegionInfo: String?](crashdiagnostic/virtualmemoryregioninfo.md)
  Details about memory that the app incorrectly accessed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/crashdiagnostic/signal)*