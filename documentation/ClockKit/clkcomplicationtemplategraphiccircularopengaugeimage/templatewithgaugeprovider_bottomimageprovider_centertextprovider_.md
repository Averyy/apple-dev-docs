# templateWithGaugeProvider:bottomImageProvider:centerTextProvider:

**Framework**: ClockKit  
**Kind**: method  
**Role**: Type Method

Returns a new template that has an open circular gauge, a small image at the bottom, and a small amount of text in the center.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

## Declaration

```objc
+ (instancetype) templateWithGaugeProvider:(CLKGaugeProvider *) gaugeProvider bottomImageProvider:(CLKFullColorImageProvider *) bottomImageProvider centerTextProvider:(CLKTextProvider *) centerTextProvider;
```

## Parameters

- `gaugeProvider`: The gauge provider for the template.
- `bottomImageProvider`: The image provider for a small image at the bottom of the template. The template uses a full-color image.
- `centerTextProvider`: The text provider for the center text. The template supports multicolored text from this text provider.

## See Also

### Creating the Template
- [init(gaugeProvider: CLKGaugeProvider, bottomImageProvider: CLKFullColorImageProvider, centerTextProvider: CLKTextProvider)](./init%28gaugeprovider,bottomimageprovider,centertextprovider%29.md)
  Creates a new template that has an open circular gauge, a small image at the bottom, and a small amount of text in the center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphiccircularopengaugeimage/templatewithgaugeprovider:bottomimageprovider:centertextprovider:)*