# CLKTimeIntervalGaugeProvider

**Framework**: ClockKit  
**Kind**: class  
**Role**: Class

A gauge that tracks time intervals.

**Availability**:
- watchOS 5.0+ - Deprecated in 27.2

> **Deprecated**: Use [WidgetKit](../WidgetKit/WidgetKit.md) to create complications for watchOS 10 or later. For more information, see Migrating to WidgetKit.

## Declaration

```swift
class CLKTimeIntervalGaugeProvider
```

```objc
@interface CLKTimeIntervalGaugeProvider : CLKGaugeProvider
```

## Mentions

- [Creating a timeline entry](./creating-a-timeline-entry.md)

## Overview

Use this gauge provider to visually show the amount of time that has elapsed within the specified time interval.

> **Note**:  Tinted graphic complications display gauges using a solid color chosen by the user.

## Topics

### Creating a Time Interval Gauge
- [convenience init(style: CLKGaugeProviderStyle, gaugeColors: [UIColor]?, gaugeColorLocations: [NSNumber]?, start: Date, end: Date)](./clktimeintervalgaugeprovider/init%28style,gaugecolors,gaugecolorlocations,start,end%29.md)
  Creates a time interval gauge that fills as time passes.
- [convenience init(style: CLKGaugeProviderStyle, gaugeColors: [UIColor]?, gaugeColorLocations: [NSNumber]?, start: Date, startFillFraction: Float, end: Date, endFillFraction: Float)](./clktimeintervalgaugeprovider/init%28style,gaugecolors,gaugecolorlocations,start,startfillfraction,end,endfillfraction%29.md)
  Creates a time interval gauge, letting you specify whether the gauge fills or empties as time passes.
### Getting Information about the Gauge
- [var startDate: Date](./clktimeintervalgaugeprovider/startdate.md)
  The starting time and date for the gauge’s time interval.
- [var endDate: Date](./clktimeintervalgaugeprovider/enddate.md)
  The ending time and date for the gauge’s time interval.
- [var startFillFraction: Float](./clktimeintervalgaugeprovider/startfillfraction.md)
  The position of the leading edge of the time bar within the specified time interval.
- [var endFillFraction: Float](./clktimeintervalgaugeprovider/endfillfraction.md)
  The position of the trailing edge of the time bar within the specified time interval.
### Initializers
- [convenience init(style: CLKGaugeProviderStyle, gaugeColors: [UIColor]?, gaugeColorLocations: [NSNumber]?, startDate: Date, endDate: Date)](./clktimeintervalgaugeprovider/init%28style,gaugecolors,gaugecolorlocations,startdate,enddate%29.md)
- [convenience init(style: CLKGaugeProviderStyle, gaugeColors: [UIColor]?, gaugeColorLocations: [NSNumber]?, startDate: Date, startFillFraction: Float, endDate: Date, endFillFraction: Float)](./clktimeintervalgaugeprovider/init%28style,gaugecolors,gaugecolorlocations,startdate,startfillfraction,enddate,endfillfraction%29.md)

## Relationships

### Inherits From
- [CLKGaugeProvider](./clkgaugeprovider.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Gauge providers
- [class CLKSimpleGaugeProvider](./clksimplegaugeprovider.md)
  A gauge that shows a fractional value.
- [class CLKGaugeProvider](./clkgaugeprovider.md)
  An abstract superclass that provides all the common behaviors for the gauge providers.
- [let CLKSimpleGaugeProviderFillFractionEmpty: Float](./clksimplegaugeproviderfillfractionempty.md)
  A fill value indicating an empty gauge.
- [enum CLKGaugeProviderStyle](./clkgaugeproviderstyle.md)
  Visual styles available for gauges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clktimeintervalgaugeprovider)*