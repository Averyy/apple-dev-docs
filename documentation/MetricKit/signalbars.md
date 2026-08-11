# SignalBars

**Framework**: MetricKit  
**Kind**: class

A unit for cellular signal strength measurements in bars.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
@objc
final class SignalBars
```

## Mentions

- [Analyzing app performance with MetricKit](analyzing-app-performance-with-metrickit.md)

#### Discussion

This is used as the dimension type in [`histogram`](cellularconditiontimemetric/histogram.md), which has type `Histogram<SignalBars>`. The base unit symbol is `"bars"`.

## Topics

### Type Methods
- [static func baseUnit() -> SignalBars](signalbars/baseunit.md)

## Relationships

### Inherits From
- [Dimension](../Foundation/Dimension.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct Histogram](histogram.md)
  A distribution of values organized into buckets.
- [struct AverageStatistics](averagestatistics.md)
  A value that encapsulates an average measurement with supporting statistical data.
- [class HitchTimeRatio](hitchtimeratio.md)
  A unit for animation hitch time ratio measurements.
- [struct OSVersion](osversion.md)
  The version of the operating system on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/signalbars)*