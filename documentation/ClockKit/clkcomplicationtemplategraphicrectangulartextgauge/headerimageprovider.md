# headerImageProvider

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

The header image to display.

**Availability**:
- watchOS 5.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
@NSCopying
var headerImageProvider: CLKFullColorImageProvider? { get set }
```

```objc
@property (nonatomic, copy, nullable) CLKFullColorImageProvider * headerImageProvider;
```

#### Discussion

This image provider produces a full-color image.

## See Also

### Setting the Complication Data
- [var headerTextProvider: CLKTextProvider](./headertextprovider.md)
  The header text to display in the complication.
- [var body1TextProvider: CLKTextProvider](./body1textprovider.md)
  The main body text to display in the complication.
- [var gaugeProvider: CLKGaugeProvider](./gaugeprovider.md)
  The gauge to display in the complication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicrectangulartextgauge/headerimageprovider)*