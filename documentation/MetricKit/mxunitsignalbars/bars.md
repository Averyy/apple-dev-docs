# bars

**Framework**: MetricKit  
**Kind**: property  
**Role**: Type Property

The number of bars of connectivity to the cellular network.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`SignalBars`](../signalbars.md) instead.

## Declaration

```swift
@NSCopying
class var bars: MXUnitSignalBars { get }
```

```objc
@property (class, copy, readonly) MXUnitSignalBars * bars;
```

#### Discussion

The value of `bars` is a whole number ranging from 0 to the number of bars that represents a full-strength connection. A value of 0 represents no connectivity. The maximum value varies depending on the country or region, and the carrier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxunitsignalbars/bars)*