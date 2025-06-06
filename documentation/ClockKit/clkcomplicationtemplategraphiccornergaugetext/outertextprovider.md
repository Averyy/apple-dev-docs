# outerTextProvider

**Framework**: ClockKit  
**Kind**: property

The outer text to display in the complication.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
@NSCopying
var outerTextProvider: CLKTextProvider { get set }
```

#### Discussion

The complication ignores the text provider’s tint color. It always displays the outer text as white.

## See Also

- [var gaugeProvider: CLKGaugeProvider](clkcomplicationtemplategraphiccornergaugetext/gaugeprovider.md)
  The gauge to display in the complication.
- [var leadingTextProvider: CLKTextProvider?](clkcomplicationtemplategraphiccornergaugetext/leadingtextprovider.md)
  The text to display on the leading edge of the gague.
- [var trailingTextProvider: CLKTextProvider?](clkcomplicationtemplategraphiccornergaugetext/trailingtextprovider.md)
  The text to display on the trailing edge of the gauge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccornergaugetext/outertextprovider)*