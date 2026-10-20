# metrics(forType:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func metrics<MetricEvent>(forType metricType: MetricEvent.Type) -> AVMetrics<MetricEvent> where MetricEvent : AVMetricEvent
```

## See Also

### Getting the metrics
- [func allMetrics() -> AVMetrics<AVMetricEvent>](./allmetrics%28%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetriceventstreampublisher/metrics(fortype:))*