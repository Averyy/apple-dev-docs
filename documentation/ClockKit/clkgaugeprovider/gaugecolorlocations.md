# gaugeColorLocations

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

The location of each color in a multicolor gauge’s gradient.

**Availability**:
- watchOS 5.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
var gaugeColorLocations: [NSNumber]? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSArray<NSNumber *> * gaugeColorLocations;
```

#### Discussion

This property specifies the location of each color in the [`gaugeColors`](./gaugecolors.md) array. Each location must be a value between `0.0` and `1.0`.

A gauge with more than one color appears as a gradient. The provider specifies the colors using the [`gaugeColors`](./gaugecolors.md) property. The [`gaugeColors`](./gaugecolors.md) and [`gaugeColorLocations`](./gaugecolorlocations.md) properties must have the same number of elements.

## See Also

### Setting the Gauge’s Appearance
- [var gaugeColors: [UIColor]?](./gaugecolors.md)
  The colors of the gauge.
- [var style: CLKGaugeProviderStyle](./style.md)
  The style that defines the gauge’s appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkgaugeprovider/gaugecolorlocations)*