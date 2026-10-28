# gaugeColors

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

The colors of the gauge.

**Availability**:
- watchOS 5.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
var gaugeColors: [UIColor]? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSArray<UIColor *> * gaugeColors;
```

## Discussion

A gauge with more than one color appears as a gradient. The provider specifies the location of the colors using the [`gaugeColorLocations`](./gaugecolorlocations.md) property. The [`gaugeColors`](./gaugecolors.md) and [`gaugeColorLocations`](./gaugecolorlocations.md) properties must have the same number of elements.

> **Note**:  Tinted graphic complications display gauges using a solid color chosen by the user. The gauge colors have no affect on the appearance of these complications.

## See Also

### Setting the Gauge’s Appearance
- [var gaugeColorLocations: [NSNumber]?](./gaugecolorlocations.md)
  The location of each color in a multicolor gauge’s gradient.
- [var style: CLKGaugeProviderStyle](./style.md)
  The style that defines the gauge’s appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkgaugeprovider/gaugecolors)*