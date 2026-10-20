# MXMetricManagerSubscriber

**Framework**: MetricKit  
**Kind**: protocol  
**Role**: Protocol

A protocol defining a method for receiving a daily metrics report.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 12.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`MetricManager`](./metricmanager.md) instead.

## Declaration

```swift
protocol MXMetricManagerSubscriber : NSObjectProtocol
```

```objc
@protocol MXMetricManagerSubscriber <NSObject>
```

## Topics

### Receiving reports
- [func didReceive([MXMetricPayload])](./mxmetricmanagersubscriber/didreceive%28_%29-3zq5g.md)
  Delivers new metrics reports to the object registered with the metrics manager.
- [func didReceive([MXDiagnosticPayload])](./mxmetricmanagersubscriber/didreceive%28_%29-9yd4u.md)
  Delivers new diagnostic reports to the object registered with the metrics manager.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Metric and diagnostic reports
- [class MXMetricManager](./mxmetricmanager.md)
  The shared object that registers you to receive metrics, creates logs for custom metrics, and gives access to past reports.
- [class MXMetricPayload](./mxmetricpayload.md)
  An object that encapsulates a daily metrics report.
- [class MXDiagnosticPayload](./mxdiagnosticpayload.md)
  An object that encapsulates a diagnostic report.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmetricmanagersubscriber)*