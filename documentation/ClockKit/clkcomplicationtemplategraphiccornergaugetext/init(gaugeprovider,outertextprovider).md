# init(gaugeProvider:outerTextProvider:)

**Framework**: ClockKit  
**Kind**: init  
**Role**: Initializer

Creates a template that has a gauge and an outer text element.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

## Declaration

```swift
init(gaugeProvider: CLKGaugeProvider, outerTextProvider: CLKTextProvider)
```

```objc
- (instancetype) initWithGaugeProvider:(CLKGaugeProvider *) gaugeProvider outerTextProvider:(CLKTextProvider *) outerTextProvider;
```

## Parameters

- `gaugeProvider`: The gauge provider for the template.
- `outerTextProvider`: The text provider for the outer line of text. The template ignores this text provider’s tint color, and always displays the text with a system color.

## See Also

### Creating the Template
- [init(gaugeProvider: CLKGaugeProvider, leadingTextProvider: CLKTextProvider?, trailingTextProvider: CLKTextProvider?, outerTextProvider: CLKTextProvider)](./init%28gaugeprovider,leadingtextprovider,trailingtextprovider,outertextprovider%29.md)
  Creates a template that has a gauge with leading and trailing text, and an outer text element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccornergaugetext/init(gaugeprovider:outertextprovider:))*