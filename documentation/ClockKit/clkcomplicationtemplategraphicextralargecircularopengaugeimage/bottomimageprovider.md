# bottomImageProvider

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

The image to display at the bottom of the gauge.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
@NSCopying
var bottomImageProvider: CLKFullColorImageProvider { get set }
```

```objc
@property (nonatomic, copy) CLKFullColorImageProvider * bottomImageProvider;
```

#### Discussion

This image provider produces a full-color image, masked to a circle.

## See Also

### Setting the Complication Data
- [var centerTextProvider: CLKTextProvider](./centertextprovider.md)
  The text to display in the center of the gauge.
- [var gaugeProvider: CLKGaugeProvider](./gaugeprovider.md)
  The gauge to display in the complication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicextralargecircularopengaugeimage/bottomimageprovider)*