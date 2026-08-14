# OSVersion

**Framework**: MetricKit  
**Kind**: struct

The version of the operating system on the device.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct OSVersion
```

## Topics

### Instance Properties
- [let buildNumber: String](osversion/buildnumber.md)
  The build number of the operating system (e.g., “23F75”).
- [let number: String](osversion/number.md)
  The version number of the operating system (e.g., “26.5”).
- [let platform: String](osversion/platform.md)
  The name of the operating system platform (e.g., “iPhone OS”).

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct Histogram](histogram.md)
  A distribution of values organized into buckets.
- [struct AverageStatistics](averagestatistics.md)
  A value that encapsulates an average measurement with supporting statistical data.
- [class SignalBars](signalbars.md)
  A unit for cellular signal strength measurements in bars.
- [class HitchTimeRatio](hitchtimeratio.md)
  A unit for animation hitch time ratio measurements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/osversion)*