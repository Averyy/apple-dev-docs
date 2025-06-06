# CLKTimeIntervalGaugeProvider

**Framework**: ClockKit  
**Kind**: class

A gauge that tracks time intervals.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
class CLKTimeIntervalGaugeProvider
```

## Mentions

- [Creating a timeline entry](creating-a-timeline-entry.md)

#### Overview

Use this gauge provider to visually show the amount of time that has elapsed within the specified time interval.

> **Note**:  Tinted graphic complications display gauges using a solid color chosen by the user.

 Tinted graphic complications display gauges using a solid color chosen by the user.

## Topics

### Creating a Time Interval Gauge
- [convenience init(style: CLKGaugeProviderStyle, gaugeColors: [UIColor]?, gaugeColorLocations: [NSNumber]?, start: Date, end: Date)](clktimeintervalgaugeprovider/init(style:gaugecolors:gaugecolorlocations:start:end:).md)
  Creates a time interval gauge that fills as time passes.
- [convenience init(style: CLKGaugeProviderStyle, gaugeColors: [UIColor]?, gaugeColorLocations: [NSNumber]?, start: Date, startFillFraction: Float, end: Date, endFillFraction: Float)](clktimeintervalgaugeprovider/init(style:gaugecolors:gaugecolorlocations:start:startfillfraction:end:endfillfraction:).md)
  Creates a time interval gauge, letting you specify whether the gauge fills or empties as time passes.
### Getting Information about the Gauge
- [var startDate: Date](clktimeintervalgaugeprovider/startdate.md)
  The starting time and date for the gauge’s time interval.
- [var endDate: Date](clktimeintervalgaugeprovider/enddate.md)
  The ending time and date for the gauge’s time interval.
- [var startFillFraction: Float](clktimeintervalgaugeprovider/startfillfraction.md)
  The position of the leading edge of the time bar within the specified time interval.
- [var endFillFraction: Float](clktimeintervalgaugeprovider/endfillfraction.md)
  The position of the trailing edge of the time bar within the specified time interval.

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

- [class CLKSimpleGaugeProvider](clksimplegaugeprovider.md)
  A gauge that shows a fractional value.
- [class CLKGaugeProvider](clkgaugeprovider.md)
  An abstract superclass that provides all the common behaviors for the gauge providers.
- [let CLKSimpleGaugeProviderFillFractionEmpty: Float](clksimplegaugeproviderfillfractionempty.md)
  A fill value indicating an empty gauge.
- [enum CLKGaugeProviderStyle](clkgaugeproviderstyle.md)
  Visual styles available for gauges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clktimeintervalgaugeprovider)*