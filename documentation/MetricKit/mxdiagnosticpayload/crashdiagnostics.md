# crashDiagnostics

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The diagnostic reports for app crashes during the reporting period.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.0
- macOS 12.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`DiagnosticResult.crash(_:)`](../diagnosticresult/crash%28_%29.md) instead.

## Declaration

```swift
var crashDiagnostics: [MXCrashDiagnostic]? { get }
```

```objc
@property (strong, readonly, nullable) NSArray<MXCrashDiagnostic *> * crashDiagnostics;
```

## See Also

### Reading performance metrics
- [var cpuExceptionDiagnostics: [MXCPUExceptionDiagnostic]?](./cpuexceptiondiagnostics.md)
  The diagnostic reports for fatal and nonfatal CPU exceptions for the app during the reporting period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxdiagnosticpayload/crashdiagnostics)*