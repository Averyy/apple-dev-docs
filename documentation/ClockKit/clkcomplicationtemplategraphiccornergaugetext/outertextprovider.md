# outerTextProvider

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

The outer text to display in the complication.

**Availability**:
- watchOS 5.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
@NSCopying
var outerTextProvider: CLKTextProvider { get set }
```

```objc
@property (nonatomic, copy) CLKTextProvider * outerTextProvider;
```

## Discussion

The complication ignores the text provider’s tint color. It always displays the outer text as white.

## See Also

### Setting the Complication Data
- [var gaugeProvider: CLKGaugeProvider](./gaugeprovider.md)
  The gauge to display in the complication.
- [var leadingTextProvider: CLKTextProvider?](./leadingtextprovider.md)
  The text to display on the leading edge of the gague.
- [var trailingTextProvider: CLKTextProvider?](./trailingtextprovider.md)
  The text to display on the trailing edge of the gauge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccornergaugetext/outertextprovider)*