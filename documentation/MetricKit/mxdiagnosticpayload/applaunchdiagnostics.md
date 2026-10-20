# appLaunchDiagnostics

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The diagnostic reports for the app launch time.

**Availability**:
- iOS 16.0+ - Deprecated in 27.2
- iPadOS 16.0+ - Deprecated in 27.2
- Mac Catalyst 16.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`DiagnosticResult.appLaunch(_:)`](../diagnosticresult/applaunch%28_%29.md) instead.

## Declaration

```swift
var appLaunchDiagnostics: [MXAppLaunchDiagnostic]? { get }
```

```objc
@property (strong, readonly, nullable) NSArray<MXAppLaunchDiagnostic *> * appLaunchDiagnostics;
```

## See Also

### Reading responsiveness metrics
- [var hangDiagnostics: [MXHangDiagnostic]?](./hangdiagnostics.md)
  The diagnostic reports for times when the app was too busy to handle input responsively during the reporting period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxdiagnosticpayload/applaunchdiagnostics)*