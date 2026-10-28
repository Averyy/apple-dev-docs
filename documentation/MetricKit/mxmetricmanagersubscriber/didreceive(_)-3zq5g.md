# didReceive(_:)

**Framework**: MetricKit  
**Kind**: method  
**Role**: Instance Method

Delivers new metrics reports to the object registered with the metrics manager.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`metricReports`](../metricmanager/metricreports.md) instead.

## Declaration

```swift
optional func didReceive(_ payloads: [MXMetricPayload])
```

```objc
- (void) didReceiveMetricPayloads:(NSArray<MXMetricPayload *> *) payloads;
```

## Discussion

The system calls this method at most once per day. It’s safe to process the payload on a separate thread.

> **Note**:  MetricKit delivers daily metric reports from iOS 13 or later, and macOS 26 or later.

## Parameters

- `payloads`: An array of new metrics reports.

## See Also

### Receiving reports
- [func didReceive([MXDiagnosticPayload])](./didreceive%28_%29-9yd4u.md)
  Delivers new diagnostic reports to the object registered with the metrics manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmetricmanagersubscriber/didreceive(_:)-3zq5g)*