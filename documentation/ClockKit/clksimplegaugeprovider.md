# CLKSimpleGaugeProvider

**Framework**: ClockKit  
**Kind**: class

A gauge that shows a fractional value.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
class CLKSimpleGaugeProvider
```

## Mentions

- [Creating a timeline entry](creating-a-timeline-entry.md)

#### Overview

A simple gauge provider displays values that map to a `0.0` to `1.0` range. For example, you could use the gauge to show the percentage of a task that has been completed, or the current temperature within a specified temperature range.

> **Note**:  Tinted graphic complications display gauges using a solid color chosen by the user.

For time intervals, use the [`CLKTimeIntervalGaugeProvider`](clktimeintervalgaugeprovider.md).

## Topics

### Creating a Simple Gauge Provider
- [convenience init(style: CLKGaugeProviderStyle, gaugeColor: UIColor, fillFraction: Float)](clksimplegaugeprovider/init(style:gaugecolor:fillfraction:).md)
  Creates a solid-color gauge.
- [convenience init(style: CLKGaugeProviderStyle, gaugeColors: [UIColor]?, gaugeColorLocations: [NSNumber]?, fillFraction: Float)](clksimplegaugeprovider/init(style:gaugecolors:gaugecolorlocations:fillfraction:).md)
  Creates a multicolor gauge.
### Getting Information About the Gauge
- [var fillFraction: Float](clksimplegaugeprovider/fillfraction.md)
  The value displayed by the gauge.

## Relationships

### Inherits From
- [CLKGaugeProvider](clkgaugeprovider.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CLKTimeIntervalGaugeProvider](clktimeintervalgaugeprovider.md)
  A gauge that tracks time intervals.
- [class CLKGaugeProvider](clkgaugeprovider.md)
  An abstract superclass that provides all the common behaviors for the gauge providers.
- [let CLKSimpleGaugeProviderFillFractionEmpty: Float](clksimplegaugeproviderfillfractionempty.md)
  A fill value indicating an empty gauge.
- [enum CLKGaugeProviderStyle](clkgaugeproviderstyle.md)
  Visual styles available for gauges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clksimplegaugeprovider)*