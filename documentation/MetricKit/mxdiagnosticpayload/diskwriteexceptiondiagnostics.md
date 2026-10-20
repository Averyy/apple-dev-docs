# diskWriteExceptionDiagnostics

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The diagnostic reports for disk write exceptions for the app during the reporting period.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.0
- macOS 12.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`DiagnosticResult.diskWriteException(_:)`](../diagnosticresult/diskwriteexception%28_%29.md) instead.

## Declaration

```swift
var diskWriteExceptionDiagnostics: [MXDiskWriteExceptionDiagnostic]? { get }
```

```objc
@property (strong, readonly, nullable) NSArray<MXDiskWriteExceptionDiagnostic *> * diskWriteExceptionDiagnostics;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxdiagnosticpayload/diskwriteexceptiondiagnostics)*