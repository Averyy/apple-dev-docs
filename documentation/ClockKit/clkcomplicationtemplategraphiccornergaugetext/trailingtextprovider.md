# trailingTextProvider

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

The text to display on the trailing edge of the gauge.

**Availability**:
- watchOS 5.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
@NSCopying
var trailingTextProvider: CLKTextProvider? { get set }
```

```objc
@property (nonatomic, copy, nullable) CLKTextProvider * trailingTextProvider;
```

## Discussion

This property supports multicolor text.

## See Also

### Setting the Complication Data
- [var outerTextProvider: CLKTextProvider](./outertextprovider.md)
  The outer text to display in the complication.
- [var gaugeProvider: CLKGaugeProvider](./gaugeprovider.md)
  The gauge to display in the complication.
- [var leadingTextProvider: CLKTextProvider?](./leadingtextprovider.md)
  The text to display on the leading edge of the gague.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccornergaugetext/trailingtextprovider)*