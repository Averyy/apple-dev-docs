# templateWithGaugeProvider:bottomTextProvider:centerTextProvider:

**Framework**: ClockKit  
**Kind**: method  
**Role**: Type Method

Returns a new template with an open circular gauge, a small text element at the bottom, and a larger text element in the center.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

## Declaration

```objc
+ (instancetype) templateWithGaugeProvider:(CLKGaugeProvider *) gaugeProvider bottomTextProvider:(CLKTextProvider *) bottomTextProvider centerTextProvider:(CLKTextProvider *) centerTextProvider;
```

## Parameters

- `gaugeProvider`: The gauge provider for the template.
- `bottomTextProvider`: The text provider for the bottom text. The template supports multicolored text from this text provider.
- `centerTextProvider`: The text provider for the center text. The template supports multicolored text from this text provider.

## See Also

### Creating the Template
- [init(gaugeProvider: CLKGaugeProvider, bottomTextProvider: CLKTextProvider, centerTextProvider: CLKTextProvider)](./init%28gaugeprovider,bottomtextprovider,centertextprovider%29.md)
  Creates a new template with an open circular gauge, a small text element at the bottom, and a larger text element in the center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicextralargecircularopengaugesimpletext/templatewithgaugeprovider:bottomtextprovider:centertextprovider:)*