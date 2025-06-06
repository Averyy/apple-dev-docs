# init(style:gaugeColors:gaugeColorLocations:start:startFillFraction:end:endFillFraction:)

**Framework**: ClockKit  
**Kind**: init

Creates a time interval gauge, letting you specify whether the gauge fills or empties as time passes.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
convenience init(style: CLKGaugeProviderStyle, gaugeColors: [UIColor]?, gaugeColorLocations: [NSNumber]?, start startDate: Date, startFillFraction: Float, end endDate: Date, endFillFraction: Float)
```

#### Return Value

A newly instantiated time interval gauge provider.

#### Discussion

The gauge shows the amount of time that has elapsed, based on the current time relative to the specified start and end dates. You can specify whether the gauge counts up or counts down using the `startFillFraction` and `endFillFraction` parameters.

- If the `startFillFraction` is less than the `endFillFraction`, the gauge fills as it counts up from the start time to the end time.
- If the `startFillFraction` is greater than the `endFillFraction`, the gauge empties as it counts down from the start time to the end time.
- On circular gauges, the fill fractions also determine the position of the start and end points along the circle. `0.0` indicates the top of the circle. Values increase as you move around the circle clockwise, with `1.0` back at the top again.
- On corner gauges, you should always use the `0.0` and `1.0` as your fractional values, to ensure that you’re utilizing the whole gauge.

If you provide both colors and locations, then the `gaugeColors` and `gaugeColorLocations` arrays must be the same length.

## Parameters

- `style`: The style defining the gauge’s visual appearance. For a list of valid styles, see  .
- `gaugeColors`: The gauge’s colors. These colors are displayed as a gradient.
- `gaugeColorLocations`: The location of each color along the gauge. Locations are values between   and  . If  , the colors are evenly spaced along the gauge.
- `startDate`: The start time and date.
- `startFillFraction`: The starting position for the gague. This is a value between   and  .
- `endDate`: The end time and date. This value must be later than or equal to the start date.
- `endFillFraction`: The end position of the gague. This is a value between   and  .

## See Also

- [convenience init(style: CLKGaugeProviderStyle, gaugeColors: [UIColor]?, gaugeColorLocations: [NSNumber]?, start: Date, end: Date)](clktimeintervalgaugeprovider/init(style:gaugecolors:gaugecolorlocations:start:end:).md)
  Creates a time interval gauge that fills as time passes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clktimeintervalgaugeprovider/init(style:gaugecolors:gaugecolorlocations:start:startfillfraction:end:endfillfraction:))*