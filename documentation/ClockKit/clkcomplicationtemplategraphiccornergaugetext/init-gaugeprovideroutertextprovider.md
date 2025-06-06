# init(gaugeProvider:outerTextProvider:)

**Framework**: ClockKit  
**Kind**: init

Creates a template that has a gauge and an outer text element.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
init(gaugeProvider: CLKGaugeProvider, outerTextProvider: CLKTextProvider)
```

## Parameters

- `gaugeProvider`: The gauge provider for the template.
- `outerTextProvider`: The text provider for the outer line of text. The template ignores this text provider’s tint color, and always displays the text with a system color.

## See Also

- [init(gaugeProvider: CLKGaugeProvider, leadingTextProvider: CLKTextProvider?, trailingTextProvider: CLKTextProvider?, outerTextProvider: CLKTextProvider)](clkcomplicationtemplategraphiccornergaugetext/init(gaugeprovider:leadingtextprovider:trailingtextprovider:outertextprovider:).md)
  Creates a template that has a gauge with leading and trailing text, and an outer text element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccornergaugetext/init(gaugeprovider:outertextprovider:))*