# didReceive(_:)

**Framework**: MetricKit  
**Kind**: method

Delivers new diagnostic reports to the object registered with the metrics manager.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
optional func didReceive(_ payloads: [MXDiagnosticPayload])
```

#### Discussion

The system calls this method at most once per day. It’s safe to process the payload on a separate thread.

## Parameters

- `payloads`: An array of new diagnostic reports.

## See Also

- [func didReceive([MXMetricPayload])](mxmetricmanagersubscriber/didreceive(_:)-3zq5g.md)
  Delivers new metrics reports to the object registered with the metrics manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxmetricmanagersubscriber/didreceive(_:)-9yd4u)*