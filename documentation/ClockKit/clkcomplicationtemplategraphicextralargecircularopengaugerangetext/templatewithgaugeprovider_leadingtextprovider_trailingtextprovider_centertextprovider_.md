# templateWithGaugeProvider:leadingTextProvider:trailingTextProvider:centerTextProvider:

**Framework**: ClockKit  
**Kind**: method  
**Role**: Type Method

Returns a new template that has an open, circular gauge with leading and trailing text, and a central text element.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

## Declaration

```objc
+ (instancetype) templateWithGaugeProvider:(CLKGaugeProvider *) gaugeProvider leadingTextProvider:(CLKTextProvider *) leadingTextProvider trailingTextProvider:(CLKTextProvider *) trailingTextProvider centerTextProvider:(CLKTextProvider *) centerTextProvider;
```

## Parameters

- `gaugeProvider`: The gauge provider for the template.
- `leadingTextProvider`: The text provider for the leading text. The template supports multicolored text from this text provider.
- `trailingTextProvider`: The text provider for the trailing text. The template supports multicolored text from this text provider.
- `centerTextProvider`: The text provider for the center text. The template supports multicolored text from this text provider.

## See Also

### Creating the Template
- [init(gaugeProvider: CLKGaugeProvider, leadingTextProvider: CLKTextProvider, trailingTextProvider: CLKTextProvider, centerTextProvider: CLKTextProvider)](./init%28gaugeprovider,leadingtextprovider,trailingtextprovider,centertextprovider%29.md)
  Creates a new template that has an open, circular gauge with leading and trailing text, and a central text element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicextralargecircularopengaugerangetext/templatewithgaugeprovider:leadingtextprovider:trailingtextprovider:centertextprovider:)*