# pastDiagnosticPayloads

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The diagnostic reports since the last initialization of the shared manager instance.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.0
- macOS 12.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`diagnosticReports`](../metricmanager/diagnosticreports.md) instead.

## Declaration

```swift
var pastDiagnosticPayloads: [MXDiagnosticPayload] { get }
```

```objc
@property (strong, readonly, nonnull) NSArray<MXDiagnosticPayload *> * pastDiagnosticPayloads;
```

#### Discussion

You can access this property after you register your first subscriber using [`add(_:)`](./add%28_%29.md) and receive at least one [`MXMetricManagerSubscriber`](../mxmetricmanagersubscriber.md) callback.

This property only reflects diagnostic reports from the current session and lifetime of the [`MXMetricManager`](../mxmetricmanager.md) instance. It doesn’t include diagnostics from previous app instances.

## See Also

### Retrieving previous reports
- [var pastPayloads: [MXMetricPayload]](./pastpayloads.md)
  Returns an array of the daily metrics reports generated since the last allocation of the shared manager instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmetricmanager/pastdiagnosticpayloads)*