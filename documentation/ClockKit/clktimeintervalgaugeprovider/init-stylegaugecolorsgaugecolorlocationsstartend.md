# init(style:gaugeColors:gaugeColorLocations:start:end:)

**Framework**: ClockKit  
**Kind**: init

Creates a time interval gauge that fills as time passes.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
convenience init(style: CLKGaugeProviderStyle, gaugeColors: [UIColor]?, gaugeColorLocations: [NSNumber]?, start startDate: Date, end endDate: Date)
```

#### Return Value

A newly instantiated time interval gauge provider.

#### Discussion

The gauge shows the amount of time that has elapsed, based on the current time relative to the specified start and end dates. The gauge fills as it counts up from the start time to the end time.

If you provide both colors and locations, then the `gaugeColors` and `gaugeColorLocations` arrays must be the same length.

## Parameters

- `style`: The style defining the gauge’s visual appearance. For a list of valid styles, see  .
- `gaugeColors`: The gauge’s colors. These colors are displayed as a gradient.
- `gaugeColorLocations`: The location of each color along the gauge. Locations are values between   and  . If  , the colors are evenly spaced along the gauge.
- `startDate`: The start time and date.
- `endDate`: The end time and date. This value must be later than or equal to the start date.

## See Also

- [convenience init(style: CLKGaugeProviderStyle, gaugeColors: [UIColor]?, gaugeColorLocations: [NSNumber]?, start: Date, startFillFraction: Float, end: Date, endFillFraction: Float)](clktimeintervalgaugeprovider/init(style:gaugecolors:gaugecolorlocations:start:startfillfraction:end:endfillfraction:).md)
  Creates a time interval gauge, letting you specify whether the gauge fills or empties as time passes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clktimeintervalgaugeprovider/init(style:gaugecolors:gaugecolorlocations:start:end:))*