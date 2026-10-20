# init(gaugeProvider:imageProvider:)

**Framework**: ClockKit  
**Kind**: init  
**Role**: Initializer

Creates a new template that has a gauge and an image.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

## Declaration

```swift
init(gaugeProvider: CLKGaugeProvider, imageProvider: CLKFullColorImageProvider)
```

```objc
- (instancetype) initWithGaugeProvider:(CLKGaugeProvider *) gaugeProvider imageProvider:(CLKFullColorImageProvider *) imageProvider;
```

## Parameters

- `gaugeProvider`: The gauge provider for the template.
- `imageProvider`: A full-color image provider.

## See Also

### Creating the Template
- [init(gaugeProvider: CLKGaugeProvider, leadingTextProvider: CLKTextProvider?, trailingTextProvider: CLKTextProvider?, imageProvider: CLKFullColorImageProvider)](./init%28gaugeprovider,leadingtextprovider,trailingtextprovider,imageprovider%29.md)
  Creates a new template that has a gauge with leading and trailing text and an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccornergaugeimage/init(gaugeprovider:imageprovider:))*