# exceptionType

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The name of the Mach exception that terminated the app.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
let exceptionType: Int?
```

## See Also

### Exception details
- [let exceptionCode: UInt64?](./exceptioncode.md)
  Processor specific information about the exception.
- [let signal: Int?](./signal.md)
  The signal associated with this crash.
- [let exceptionReason: CrashDiagnostic.ObjectiveCExceptionReason?](./exceptionreason.md)
  The exception reason for an uncaught ObjC exception.
- [let virtualMemoryRegionInfo: String?](./virtualmemoryregioninfo.md)
  Details about memory that the app incorrectly accessed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/crashdiagnostic/exceptiontype)*