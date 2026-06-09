# pastDiagnosticPayloads

**Framework**: MetricKit  
**Kind**: property

The diagnostic reports since the last initialization of the shared manager instance.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
var pastDiagnosticPayloads: [MXDiagnosticPayload] { get }
```

#### Discussion

You can access this property after you register your first subscriber using [`add(_:)`](mxmetricmanager/add(_:).md) and receive at least one [`MXMetricManagerSubscriber`](mxmetricmanagersubscriber.md) callback.

This property only reflects diagnostic reports from the current session and lifetime of the [`MXMetricManager`](mxmetricmanager.md) instance. It doesn’t include diagnostics from previous app instances.

## See Also

- [var pastPayloads: [MXMetricPayload]](mxmetricmanager/pastpayloads.md)
  Returns an array of the daily metrics reports generated since the last allocation of the shared manager instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmetricmanager/pastdiagnosticpayloads)*