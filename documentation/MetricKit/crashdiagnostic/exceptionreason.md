# exceptionReason

**Framework**: MetricKit  
**Kind**: property

The exception reason for an uncaught ObjC exception.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
let exceptionReason: CrashDiagnostic.ObjectiveCExceptionReason?
```

## See Also

- [let exceptionType: Int?](crashdiagnostic/exceptiontype.md)
  The name of the Mach exception that terminated the app.
- [let exceptionCode: UInt64?](crashdiagnostic/exceptioncode.md)
  Processor specific information about the exception.
- [let signal: Int?](crashdiagnostic/signal.md)
  The signal associated with this crash.
- [let virtualMemoryRegionInfo: String?](crashdiagnostic/virtualmemoryregioninfo.md)
  Details about memory that the app incorrectly accessed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/crashdiagnostic/exceptionreason)*