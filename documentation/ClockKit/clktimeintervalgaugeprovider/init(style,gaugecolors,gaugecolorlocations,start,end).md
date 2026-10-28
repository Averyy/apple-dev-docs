# init(style:gaugeColors:gaugeColorLocations:start:end:)

**Framework**: ClockKit  
**Kind**: init  
**Role**: Initializer

Creates a time interval gauge that fills as time passes.

**Availability**:
- watchOS 5.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
convenience init(style: CLKGaugeProviderStyle, gaugeColors: [UIColor]?, gaugeColorLocations: [NSNumber]?, start startDate: Date, end endDate: Date)
```

```objc
+ (instancetype) gaugeProviderWithStyle:(CLKGaugeProviderStyle) style gaugeColors:(NSArray<UIColor *> *) gaugeColors gaugeColorLocations:(NSArray<NSNumber *> *) gaugeColorLocations startDate:(NSDate *) startDate endDate:(NSDate *) endDate;
```

## Return Value

A newly instantiated time interval gauge provider.

## Discussion

The gauge shows the amount of time that has elapsed, based on the current time relative to the specified start and end dates. The gauge fills as it counts up from the start time to the end time.

If you provide both colors and locations, then the `gaugeColors` and `gaugeColorLocations` arrays must be the same length.

## Parameters

- `style`: The style defining the gauge’s visual appearance. For a list of valid styles, see [`CLKGaugeProviderStyle`](../clkgaugeproviderstyle.md).
- `gaugeColors`: The gauge’s colors. These colors are displayed as a gradient.
- `gaugeColorLocations`: The location of each color along the gauge. Locations are values between `0.0` and `1.0`. If `nil`, the colors are evenly spaced along the gauge.
- `startDate`: The start time and date.
- `endDate`: The end time and date. This value must be later than or equal to the start date.

## See Also

### Creating a Time Interval Gauge
- [convenience init(style: CLKGaugeProviderStyle, gaugeColors: [UIColor]?, gaugeColorLocations: [NSNumber]?, start: Date, startFillFraction: Float, end: Date, endFillFraction: Float)](./init%28style,gaugecolors,gaugecolorlocations,start,startfillfraction,end,endfillfraction%29.md)
  Creates a time interval gauge, letting you specify whether the gauge fills or empties as time passes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clktimeintervalgaugeprovider/init(style:gaugecolors:gaugecolorlocations:start:end:))*