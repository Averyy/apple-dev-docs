# cpuExceptionDiagnostics

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The diagnostic reports for fatal and nonfatal CPU exceptions for the app during the reporting period.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.0
- macOS 12.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`DiagnosticResult.cpuException(_:)`](../diagnosticresult/cpuexception%28_%29.md) instead.

## Declaration

```swift
var cpuExceptionDiagnostics: [MXCPUExceptionDiagnostic]? { get }
```

```objc
@property (strong, readonly, nullable) NSArray<MXCPUExceptionDiagnostic *> * cpuExceptionDiagnostics;
```

## See Also

### Reading performance metrics
- [var crashDiagnostics: [MXCrashDiagnostic]?](./crashdiagnostics.md)
  The diagnostic reports for app crashes during the reporting period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxdiagnosticpayload/cpuexceptiondiagnostics)*