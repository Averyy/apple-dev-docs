# didReceive(_:)

**Framework**: MetricKit  
**Kind**: method

Delivers new metrics reports to the object registered with the metrics manager.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
optional func didReceive(_ payloads: [MXMetricPayload])
```

#### Discussion

The system calls this method at most once per day. It’s safe to process the payload on a separate thread.

> **Note**:  MetricKit delivers daily metric reports from iOS 13 or later, and macOS 26 or later.

## Parameters

- `payloads`: An array of new metrics reports.

## See Also

- [func didReceive([MXDiagnosticPayload])](mxmetricmanagersubscriber/didreceive(_:)-9yd4u.md)
  Delivers new diagnostic reports to the object registered with the metrics manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmetricmanagersubscriber/didreceive(_:)-3zq5g)*