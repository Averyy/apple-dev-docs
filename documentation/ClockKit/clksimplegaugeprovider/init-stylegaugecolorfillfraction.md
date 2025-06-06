# init(style:gaugeColor:fillFraction:)

**Framework**: ClockKit  
**Kind**: init

Creates a solid-color gauge.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
convenience init(style: CLKGaugeProviderStyle, gaugeColor color: UIColor, fillFraction: Float)
```

#### Return Value

A newly instantiated solid-color gauge.

## Parameters

- `style`: The style defining the gauge’s visual appearance. For a list of valid styles, see  .
- `color`: The gauge’s color.
- `fillFraction`: The value displayed by the gauge. Use a value between   and  . For an empty gauge, use  .

## See Also

- [convenience init(style: CLKGaugeProviderStyle, gaugeColors: [UIColor]?, gaugeColorLocations: [NSNumber]?, fillFraction: Float)](clksimplegaugeprovider/init(style:gaugecolors:gaugecolorlocations:fillfraction:).md)
  Creates a multicolor gauge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clksimplegaugeprovider/init(style:gaugecolor:fillfraction:))*