# init(gaugeProvider:leadingTextProvider:trailingTextProvider:outerTextProvider:)

**Framework**: ClockKit  
**Kind**: init

Creates a template that has a gauge with leading and trailing text, and an outer text element.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
init(gaugeProvider: CLKGaugeProvider, leadingTextProvider: CLKTextProvider?, trailingTextProvider: CLKTextProvider?, outerTextProvider: CLKTextProvider)
```

## Parameters

- `gaugeProvider`: The gauge provider for the template.
- `leadingTextProvider`: The text provider for the gauge’s leading text. The template supports multicolored text from this text provider.
- `trailingTextProvider`: The text provider for the gauge’s trailing text. The template supports multicolored text from this text provider.
- `outerTextProvider`: The text provider for the outer line of text. The template ignores this text provider’s tint color, and always displays the text with a system color.

## See Also

- [init(gaugeProvider: CLKGaugeProvider, outerTextProvider: CLKTextProvider)](clkcomplicationtemplategraphiccornergaugetext/init(gaugeprovider:outertextprovider:).md)
  Creates a template that has a gauge and an outer text element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccornergaugetext/init(gaugeprovider:leadingtextprovider:trailingtextprovider:outertextprovider:))*