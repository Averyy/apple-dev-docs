# templateWithGaugeProvider:centerTextProvider:

**Framework**: ClockKit  
**Kind**: method  
**Role**: Type Method

Returns a new template with a closed circular gauge with text in the center.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

## Declaration

```objc
+ (instancetype) templateWithGaugeProvider:(CLKGaugeProvider *) gaugeProvider centerTextProvider:(CLKTextProvider *) centerTextProvider;
```

## Parameters

- `gaugeProvider`: The gauge provider for the template.
- `centerTextProvider`: The text provider for the center text. The template supports multicolored text from this text provider.

## See Also

### Creating the Template
- [init(gaugeProvider: CLKGaugeProvider, centerTextProvider: CLKTextProvider)](./init%28gaugeprovider,centertextprovider%29.md)
  Creates a new template with a closed circular gauge with text in the center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicextralargecircularclosedgaugetext/templatewithgaugeprovider:centertextprovider:)*