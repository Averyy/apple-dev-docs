# didReceive(_:)

**Framework**: MetricKit  
**Kind**: method  
**Role**: Instance Method

Delivers new diagnostic reports to the object registered with the metrics manager.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2
- iPadOS 14.0+ - Deprecated in 27.2
- Mac Catalyst 14.0+ - Deprecated in 27.0
- macOS 12.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`diagnosticReports`](../metricmanager/diagnosticreports.md) instead.

## Declaration

```swift
optional func didReceive(_ payloads: [MXDiagnosticPayload])
```

```objc
- (void) didReceiveDiagnosticPayloads:(NSArray<MXDiagnosticPayload *> *) payloads;
```

## Discussion

The system calls this method at most once per day. It’s safe to process the payload on a separate thread.

## Parameters

- `payloads`: An array of new diagnostic reports.

## See Also

### Receiving reports
- [func didReceive([MXMetricPayload])](./didreceive%28_%29-3zq5g.md)
  Delivers new metrics reports to the object registered with the metrics manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmetricmanagersubscriber/didreceive(_:)-9yd4u)*