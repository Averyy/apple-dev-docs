# headerTextProvider

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

The header text to display in the complication.

**Availability**:
- watchOS 5.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
@NSCopying
var headerTextProvider: CLKTextProvider { get set }
```

```objc
@property (nonatomic, copy) CLKTextProvider * headerTextProvider;
```

#### Discussion

This property supports multicolor text.

## See Also

### Setting the Complication Data
- [var headerImageProvider: CLKFullColorImageProvider?](./headerimageprovider.md)
  The header image to display.
- [var body1TextProvider: CLKTextProvider](./body1textprovider.md)
  The main body text to display in the complication.
- [var gaugeProvider: CLKGaugeProvider](./gaugeprovider.md)
  The gauge to display in the complication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicrectangulartextgauge/headertextprovider)*