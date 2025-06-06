# init(style:gaugeColors:gaugeColorLocations:fillFraction:)

**Framework**: ClockKit  
**Kind**: init

Creates a multicolor gauge.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
convenience init(style: CLKGaugeProviderStyle, gaugeColors: [UIColor]?, gaugeColorLocations: [NSNumber]?, fillFraction: Float)
```

#### Return Value

A newly instantiated multicolor gauge.

#### Discussion

If you provide both colors and locations, then the `gaugeColors` and `gaugeColorLocations` arrays must be the same length.

## Parameters

- `style`: The style defining the gauge’s visual appearance. For a list of valid styles, see  .
- `gaugeColors`: The gauge’s colors. These colors are displayed as a gradient.
- `gaugeColorLocations`: The location of each color along the gauge. Locations are values between   and  . If  , the colors are evenly spaced along the gauge.
- `fillFraction`: The value displayed by the gauge. Use a value between   and  . For an empty gauge, use  .

## See Also

- [convenience init(style: CLKGaugeProviderStyle, gaugeColor: UIColor, fillFraction: Float)](clksimplegaugeprovider/init(style:gaugecolor:fillfraction:).md)
  Creates a solid-color gauge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clksimplegaugeprovider/init(style:gaugecolors:gaugecolorlocations:fillfraction:))*