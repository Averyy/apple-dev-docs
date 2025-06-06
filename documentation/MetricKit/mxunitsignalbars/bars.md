# bars

**Framework**: MetricKit  
**Kind**: property

The number of bars of connectivity to the cellular network.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
class var bars: MXUnitSignalBars { get }
```

#### Discussion

The value of `bars` is a whole number ranging from 0 to the number of bars that represents a full-strength connection. A value of 0 represents no connectivity. The maximum value varies depending on the country or region, and the carrier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxunitsignalbars/bars)*