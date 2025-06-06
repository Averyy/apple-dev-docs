# init(gaugeProvider:leadingTextProvider:trailingTextProvider:imageProvider:)

**Framework**: ClockKit  
**Kind**: init

Creates a new template that has a gauge with leading and trailing text and an image.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
init(gaugeProvider: CLKGaugeProvider, leadingTextProvider: CLKTextProvider?, trailingTextProvider: CLKTextProvider?, imageProvider: CLKFullColorImageProvider)
```

## Parameters

- `gaugeProvider`: The gauge provider for the template.
- `leadingTextProvider`: The text provider for the gauge’s leading text. The template supports multicolored text from this text provider.
- `trailingTextProvider`: The text provider for the gauge’s trailing text. The template supports multicolored text from this text provider.
- `imageProvider`: A full-color image provider.

## See Also

- [init(gaugeProvider: CLKGaugeProvider, imageProvider: CLKFullColorImageProvider)](clkcomplicationtemplategraphiccornergaugeimage/init(gaugeprovider:imageprovider:).md)
  Creates a new template that has a gauge and an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccornergaugeimage/init(gaugeprovider:leadingtextprovider:trailingtextprovider:imageprovider:))*