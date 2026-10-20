# SignalBars

**Framework**: MetricKit  
**Kind**: class  
**Role**: Class

A unit for cellular signal strength measurements in bars.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
@objc
final class SignalBars
```

## Mentions

- [Analyzing app performance with MetricKit](./analyzing-app-performance-with-metrickit.md)

#### Discussion

This is used as the dimension type in [`histogram`](./cellularconditiontimemetric/histogram.md), which has type `Histogram<SignalBars>`. The base unit symbol is `"bars"`.

## Topics

### Type Methods
- [static func baseUnit() -> SignalBars](./signalbars/baseunit%28%29.md)

## Relationships

### Inherits From
- [Dimension](../Foundation/dimension.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Supporting types
- [struct Histogram](./histogram.md)
  A distribution of values organized into buckets.
- [struct AverageStatistics](./averagestatistics.md)
  A value that encapsulates an average measurement with supporting statistical data.
- [class HitchTimeRatio](./hitchtimeratio.md)
  A unit for animation hitch time ratio measurements.
- [struct OSVersion](./osversion.md)
  The version of the operating system on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/signalbars)*