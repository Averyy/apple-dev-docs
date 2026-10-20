# init(headerImageProvider:headerTextProvider:body1TextProvider:gaugeProvider:)

**Framework**: ClockKit  
**Kind**: init  
**Role**: Initializer

Creates a new template that has a header row with an image and text, body text, and a gauge.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

## Declaration

```swift
init(headerImageProvider: CLKFullColorImageProvider?, headerTextProvider: CLKTextProvider, body1TextProvider: CLKTextProvider, gaugeProvider: CLKGaugeProvider)
```

```objc
- (instancetype) initWithHeaderImageProvider:(CLKFullColorImageProvider *) headerImageProvider headerTextProvider:(CLKTextProvider *) headerTextProvider body1TextProvider:(CLKTextProvider *) body1TextProvider gaugeProvider:(CLKGaugeProvider *) gaugeProvider;
```

## Parameters

- `headerImageProvider`: A full-color image provider.
- `headerTextProvider`: The text provider for the header text. The template supports multicolored text from this text provider.
- `body1TextProvider`: The text provider for the body text. The template supports multicolored text from this text provider.
- `gaugeProvider`: The gauge provider for the template.

## See Also

### Creating the Template
- [init(headerTextProvider: CLKTextProvider, body1TextProvider: CLKTextProvider, gaugeProvider: CLKGaugeProvider)](./init%28headertextprovider,body1textprovider,gaugeprovider%29.md)
  Creates a new template that has header text, body text, and a gauge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicrectangulartextgauge/init(headerimageprovider:headertextprovider:body1textprovider:gaugeprovider:))*