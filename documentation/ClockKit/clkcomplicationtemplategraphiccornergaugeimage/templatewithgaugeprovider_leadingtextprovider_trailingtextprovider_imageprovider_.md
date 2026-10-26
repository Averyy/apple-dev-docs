# templateWithGaugeProvider:leadingTextProvider:trailingTextProvider:imageProvider:

**Framework**: ClockKit  
**Kind**: method  
**Role**: Type Method

Returns a new template that has a gauge with leading and trailing text and an image.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

## Declaration

```objc
+ (instancetype) templateWithGaugeProvider:(CLKGaugeProvider *) gaugeProvider leadingTextProvider:(CLKTextProvider *) leadingTextProvider trailingTextProvider:(CLKTextProvider *) trailingTextProvider imageProvider:(CLKFullColorImageProvider *) imageProvider;
```

## Parameters

- `gaugeProvider`: The gauge provider for the template.
- `leadingTextProvider`: The text provider for the gauge’s leading text. The template supports multicolored text from this text provider.
- `trailingTextProvider`: The text provider for the gauge’s trailing text. The template supports multicolored text from this text provider.
- `imageProvider`: A full-color image provider.

## See Also

### Creating the Template
- [init(gaugeProvider: CLKGaugeProvider, imageProvider: CLKFullColorImageProvider)](./init%28gaugeprovider,imageprovider%29.md)
  Creates a new template that has a gauge and an image.
- [init(gaugeProvider: CLKGaugeProvider, leadingTextProvider: CLKTextProvider?, trailingTextProvider: CLKTextProvider?, imageProvider: CLKFullColorImageProvider)](./init%28gaugeprovider,leadingtextprovider,trailingtextprovider,imageprovider%29.md)
  Creates a new template that has a gauge with leading and trailing text and an image.
- [+ templateWithGaugeProvider:imageProvider:](./templatewithgaugeprovider_imageprovider_.md)
  Returns a new template that has a gauge and an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccornergaugeimage/templatewithgaugeprovider:leadingtextprovider:trailingtextprovider:imageprovider:)*