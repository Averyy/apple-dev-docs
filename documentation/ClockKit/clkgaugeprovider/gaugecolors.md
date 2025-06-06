# gaugeColors

**Framework**: Clockkit  
**Kind**: property

The colors of the gauge.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
var gaugeColors: [UIColor]? { get }
```

#### Discussion

A gauge with more than one color appears as a gradient. The provider specifies the location of the colors using the [`gaugeColorLocations`](clkgaugeprovider/gaugecolorlocations.md) property. The [`gaugeColors`](clkgaugeprovider/gaugecolors.md) and [`gaugeColorLocations`](clkgaugeprovider/gaugecolorlocations.md) properties must have the same number of elements.

> **Note**:  Tinted graphic complications display gauges using a solid color chosen by the user. The gauge colors have no affect on the appearance of these complications.

## See Also

- [var gaugeColorLocations: [NSNumber]?](clkgaugeprovider/gaugecolorlocations.md)
  The location of each color in a multicolor gauge’s gradient.
- [var style: CLKGaugeProviderStyle](clkgaugeprovider/style.md)
  The style that defines the gauge’s appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkgaugeprovider/gaugecolors)*