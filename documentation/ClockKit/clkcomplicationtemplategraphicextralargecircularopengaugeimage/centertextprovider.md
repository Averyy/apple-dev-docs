# centerTextProvider

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

The text to display in the center of the gauge.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
@NSCopying
var centerTextProvider: CLKTextProvider { get set }
```

```objc
@property (nonatomic, copy) CLKTextProvider * centerTextProvider;
```

## Discussion

This property supports multicolor text.

## See Also

### Setting the Complication Data
- [var bottomImageProvider: CLKFullColorImageProvider](./bottomimageprovider.md)
  The image to display at the bottom of the gauge.
- [var gaugeProvider: CLKGaugeProvider](./gaugeprovider.md)
  The gauge to display in the complication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicextralargecircularopengaugeimage/centertextprovider)*