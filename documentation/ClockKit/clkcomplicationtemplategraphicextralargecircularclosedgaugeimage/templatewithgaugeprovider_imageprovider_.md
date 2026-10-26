# templateWithGaugeProvider:imageProvider:

**Framework**: ClockKit  
**Kind**: method  
**Role**: Type Method

Returns a new template with a closed circular gauge and an image in the center.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

## Declaration

```objc
+ (instancetype) templateWithGaugeProvider:(CLKGaugeProvider *) gaugeProvider imageProvider:(CLKFullColorImageProvider *) imageProvider;
```

## Parameters

- `gaugeProvider`: The gauge provider for the template.
- `imageProvider`: The image provider for the image at the center of the template. This template uses a full-color image.

## See Also

### Creating the Template
- [init(gaugeProvider: CLKGaugeProvider, imageProvider: CLKFullColorImageProvider)](./init%28gaugeprovider,imageprovider%29.md)
  Creates a new template with a closed circular gauge and an image in the center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicextralargecircularclosedgaugeimage/templatewithgaugeprovider:imageprovider:)*