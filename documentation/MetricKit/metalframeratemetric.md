# MetalFrameRateMetric

**Framework**: MetricKit  
**Kind**: struct

A metric that measures Metal frame rate statistics for a specific `CAMetalLayer`.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
struct MetalFrameRateMetric
```

#### Discussion

This metric corresponds to the [`MetricResult.metalFrameRate(_:)`](metricresult/metalframerate(_:).md) case. It appears only in [`intervalEntries`](metricreport/intervalentries.md) and is not included in state entries.

Each `MetalFrameRateMetric` corresponds to a single `CAMetalLayer`, identified by [`layerName`](metalframeratemetric/layername.md). When your app has multiple Metal layers, the report may include multiple instances of this metric case, one for each layer.

## Topics

### Frame rate
- [let framesPerSecond: Measurement<UnitFrequency>](metalframeratemetric/framespersecond.md)
  The frame rate associated with this `CAMetalLayer`
- [let frameCount: Int](metalframeratemetric/framecount.md)
  The total Metal drawable count
- [let activeDrawingDuration: Measurement<UnitDuration>](metalframeratemetric/activedrawingduration.md)
  The duration of time spent actively producing new frames
### Layer
- [let layerName: String](metalframeratemetric/layername.md)
  The `CAMetalLayer` name this metric corresponds to

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct GPUTimeMetric](gputimemetric.md)
  A metric that measures the total GPU time used by the app.
- [struct PixelLuminanceMetric](pixelluminancemetric.md)
  A metric that measures the average luminosity of pixels on an OLED display.
- [class AveragePixelLuminance](averagepixelluminance.md)
  A unit for average pixel luminance measurements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/metalframeratemetric)*