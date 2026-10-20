# gaugeProvider

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

The gauge to display in the complication.

**Availability**:
- watchOS 5.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
@NSCopying
var gaugeProvider: CLKGaugeProvider { get set }
```

```objc
@property (nonatomic, copy) CLKGaugeProvider * gaugeProvider;
```

## See Also

### Setting the Complication Data
- [var headerTextProvider: CLKTextProvider](./headertextprovider.md)
  The header text to display in the complication.
- [var headerImageProvider: CLKFullColorImageProvider?](./headerimageprovider.md)
  The header image to display.
- [var body1TextProvider: CLKTextProvider](./body1textprovider.md)
  The main body text to display in the complication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicrectangulartextgauge/gaugeprovider)*