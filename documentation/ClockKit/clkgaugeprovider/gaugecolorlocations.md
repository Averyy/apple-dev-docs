# gaugeColorLocations

**Framework**: ClockKit  
**Kind**: property

The location of each color in a multicolor gauge’s gradient.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
var gaugeColorLocations: [NSNumber]? { get }
```

#### Discussion

This property specifies the location of each color in the [`gaugeColors`](clkgaugeprovider/gaugecolors.md) array. Each location must be a value between `0.0` and `1.0`.

A gauge with more than one color appears as a gradient. The provider specifies the colors using the [`gaugeColors`](clkgaugeprovider/gaugecolors.md) property. The [`gaugeColors`](clkgaugeprovider/gaugecolors.md) and [`gaugeColorLocations`](clkgaugeprovider/gaugecolorlocations.md) properties must have the same number of elements.

## See Also

- [var gaugeColors: [UIColor]?](clkgaugeprovider/gaugecolors.md)
  The colors of the gauge.
- [var style: CLKGaugeProviderStyle](clkgaugeprovider/style.md)
  The style that defines the gauge’s appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkgaugeprovider/gaugecolorlocations)*