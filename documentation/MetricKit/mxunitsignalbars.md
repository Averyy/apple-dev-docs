# MXUnitSignalBars

**Framework**: MetricKit  
**Kind**: class

A unit of measure for the number of bars of cellular network connectivity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class MXUnitSignalBars
```

#### Overview

Cellular connectivity measures the relative strength of the device’s signal reception in decibels, which usually falls in a range of 0 to -110.

`MXUnitSignalBars` defines the base unit as bars corresponding to the bars in the cellular connection status icon at the top of a device screen.

## Topics

### Measuring Connection Strength
- [class var bars: MXUnitSignalBars](mxunitsignalbars/bars.md)
  The number of bars of connectivity to the cellular network.

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

## See Also

- [var histogrammedCellularConditionTime: MXHistogram<MXUnitSignalBars>](mxcellularconditionmetric/histogrammedcellularconditiontime.md)
  An object representing the distribution of the different levels of connectivity to the cellular network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxunitsignalbars)*