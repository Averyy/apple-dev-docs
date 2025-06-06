# MXMetricManagerSubscriber

**Framework**: MetricKit  
**Kind**: protocol

A protocol defining a method for receiving a daily metrics report.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
protocol MXMetricManagerSubscriber : NSObjectProtocol
```

## Topics

### Receiving reports
- [func didReceive([MXMetricPayload])](mxmetricmanagersubscriber/didreceive(_:)-3zq5g.md)
  Delivers new metrics reports to the object registered with the metrics manager.
- [func didReceive([MXDiagnosticPayload])](mxmetricmanagersubscriber/didreceive(_:)-9yd4u.md)
  Delivers new diagnostic reports to the object registered with the metrics manager.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MXMetricManager](mxmetricmanager.md)
  The shared object that registers you to receive metrics, creates logs for custom metrics, and gives access to past reports.
- [class MXMetricPayload](mxmetricpayload.md)
  An object that encapsulates a daily metrics report.
- [class MXDiagnosticPayload](mxdiagnosticpayload.md)
  An object that encapsulates a diagnostic report.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmetricmanagersubscriber)*