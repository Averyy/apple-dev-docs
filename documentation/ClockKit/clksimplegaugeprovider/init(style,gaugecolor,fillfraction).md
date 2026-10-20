# init(style:gaugeColor:fillFraction:)

**Framework**: ClockKit  
**Kind**: init  
**Role**: Initializer

Creates a solid-color gauge.

**Availability**:
- watchOS 5.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
convenience init(style: CLKGaugeProviderStyle, gaugeColor color: UIColor, fillFraction: Float)
```

```objc
+ (instancetype) gaugeProviderWithStyle:(CLKGaugeProviderStyle) style gaugeColor:(UIColor *) color fillFraction:(float) fillFraction;
```

#### Return Value

A newly instantiated solid-color gauge.

## Parameters

- `style`: The style defining the gauge’s visual appearance. For a list of valid styles, see [`CLKGaugeProviderStyle`](../clkgaugeproviderstyle.md).
- `color`: The gauge’s color.
- `fillFraction`: The value displayed by the gauge. Use a value between `0.0` and `1.0`. For an empty gauge, use [`CLKSimpleGaugeProviderFillFractionEmpty`](../clksimplegaugeproviderfillfractionempty.md).

## See Also

### Creating a Simple Gauge Provider
- [convenience init(style: CLKGaugeProviderStyle, gaugeColors: [UIColor]?, gaugeColorLocations: [NSNumber]?, fillFraction: Float)](./init%28style,gaugecolors,gaugecolorlocations,fillfraction%29.md)
  Creates a multicolor gauge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clksimplegaugeprovider/init(style:gaugecolor:fillfraction:))*