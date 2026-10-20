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
- [var outerTextProvider: CLKTextProvider](./outertextprovider.md)
  The outer text to display in the complication.
- [var leadingTextProvider: CLKTextProvider?](./leadingtextprovider.md)
  The text to display on the leading edge of the gague.
- [var trailingTextProvider: CLKTextProvider?](./trailingtextprovider.md)
  The text to display on the trailing edge of the gauge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccornergaugetext/gaugeprovider)*