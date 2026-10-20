# pastPayloads

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

Returns an array of the daily metrics reports generated since the last allocation of the shared manager instance.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 12.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`metricReports`](../metricmanager/metricreports.md) instead.

## Declaration

```swift
var pastPayloads: [MXMetricPayload] { get }
```

```objc
@property (strong, readonly, nonnull) NSArray<MXMetricPayload *> * pastPayloads;
```

## See Also

### Retrieving previous reports
- [var pastDiagnosticPayloads: [MXDiagnosticPayload]](./pastdiagnosticpayloads.md)
  The diagnostic reports since the last initialization of the shared manager instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmetricmanager/pastpayloads)*