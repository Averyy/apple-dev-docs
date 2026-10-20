# PixelLuminanceMetric

**Framework**: MetricKit  
**Kind**: struct  
**Role**: Structure

A metric that measures the average luminosity of pixels on an OLED display.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+

## Declaration

```swift
struct PixelLuminanceMetric
```

#### Discussion

This metric corresponds to the [`MetricResult.pixelLuminance(_:)`](./metricresult/pixelluminance%28_%29.md) case. It appears only in [`intervalEntries`](./metricreport/intervalentries.md) and is not included in state entries.

Average pixel luminance (APL) is expressed as a value from 0 to 100 in increments of 1. This metric is only available on devices with OLED displays. On other device types, no value is reported.

## Topics

### Measurements
- [let value: AverageStatistics<AveragePixelLuminance>](./pixelluminancemetric/value.md)
  Average pixel luminance for the application with statistical data.

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### GPU and display metrics
- [struct GPUTimeMetric](./gputimemetric.md)
  A metric that measures the total GPU time used by the app.
- [struct MetalFrameRateMetric](./metalframeratemetric.md)
  A metric that measures Metal frame rate statistics for a specific `CAMetalLayer`.
- [class AveragePixelLuminance](./averagepixelluminance.md)
  A unit for average pixel luminance measurements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/pixelluminancemetric)*