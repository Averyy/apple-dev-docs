# chronologicalMerge(with:_:)

**Framework**: AVFoundation  
**Kind**: method

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func chronologicalMerge<OtherSecondMetric, each MetricEventPack>(with secondMetric: AVMetrics<OtherSecondMetric>, _ metrics: repeat AVMetrics<each MetricEventPack>) -> AVMergedMetrics<MetricEvent, OtherSecondMetric, repeat each MetricEventPack> where OtherSecondMetric : AVMetricEvent, repeat each MetricEventPack : AVMetricEvent
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetrics/chronologicalmerge(with:_:))*