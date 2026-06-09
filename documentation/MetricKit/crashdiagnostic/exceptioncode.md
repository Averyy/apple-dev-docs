# exceptionCode

**Framework**: MetricKit  
**Kind**: property

Processor specific information about the exception.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
let exceptionCode: UInt64?
```

#### Discussion

Encoded into one or more 64-bit hexadecimal numbers.

## See Also

- [let exceptionType: Int?](crashdiagnostic/exceptiontype.md)
  The name of the Mach exception that terminated the app.
- [let signal: Int?](crashdiagnostic/signal.md)
  The signal associated with this crash.
- [let exceptionReason: CrashDiagnostic.ObjectiveCExceptionReason?](crashdiagnostic/exceptionreason.md)
  The exception reason for an uncaught ObjC exception.
- [let virtualMemoryRegionInfo: String?](crashdiagnostic/virtualmemoryregioninfo.md)
  Details about memory that the app incorrectly accessed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/crashdiagnostic/exceptioncode)*