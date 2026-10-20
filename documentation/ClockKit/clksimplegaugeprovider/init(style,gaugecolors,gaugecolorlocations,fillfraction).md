# init(style:gaugeColors:gaugeColorLocations:fillFraction:)

**Framework**: ClockKit  
**Kind**: init  
**Role**: Initializer

Creates a multicolor gauge.

**Availability**:
- watchOS 5.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
convenience init(style: CLKGaugeProviderStyle, gaugeColors: [UIColor]?, gaugeColorLocations: [NSNumber]?, fillFraction: Float)
```

```objc
+ (instancetype) gaugeProviderWithStyle:(CLKGaugeProviderStyle) style gaugeColors:(NSArray<UIColor *> *) gaugeColors gaugeColorLocations:(NSArray<NSNumber *> *) gaugeColorLocations fillFraction:(float) fillFraction;
```

#### Return Value

A newly instantiated multicolor gauge.

#### Discussion

If you provide both colors and locations, then the `gaugeColors` and `gaugeColorLocations` arrays must be the same length.

## Parameters

- `style`: The style defining the gauge’s visual appearance. For a list of valid styles, see [`CLKGaugeProviderStyle`](../clkgaugeproviderstyle.md).
- `gaugeColors`: The gauge’s colors. These colors are displayed as a gradient.
- `gaugeColorLocations`: The location of each color along the gauge. Locations are values between `0.0` and `1.0`. If `nil`, the colors are evenly spaced along the gauge.
- `fillFraction`: The value displayed by the gauge. Use a value between `0.0` and `1.0`. For an empty gauge, use [`CLKSimpleGaugeProviderFillFractionEmpty`](../clksimplegaugeproviderfillfractionempty.md).

## See Also

### Creating a Simple Gauge Provider
- [convenience init(style: CLKGaugeProviderStyle, gaugeColor: UIColor, fillFraction: Float)](./init%28style,gaugecolor,fillfraction%29.md)
  Creates a solid-color gauge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clksimplegaugeprovider/init(style:gaugecolors:gaugecolorlocations:fillfraction:))*