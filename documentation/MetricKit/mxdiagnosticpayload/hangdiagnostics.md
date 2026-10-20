# hangDiagnostics

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The diagnostic reports for times when the app was too busy to handle input responsively during the reporting period.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.0
- macOS 12.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`DiagnosticResult.hang(_:)`](../diagnosticresult/hang%28_%29.md) instead.

## Declaration

```swift
var hangDiagnostics: [MXHangDiagnostic]? { get }
```

```objc
@property (strong, readonly, nullable) NSArray<MXHangDiagnostic *> * hangDiagnostics;
```

## See Also

### Reading responsiveness metrics
- [var appLaunchDiagnostics: [MXAppLaunchDiagnostic]?](./applaunchdiagnostics.md)
  The diagnostic reports for the app launch time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxdiagnosticpayload/hangdiagnostics)*