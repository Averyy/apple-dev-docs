# init(gaugeProvider:imageProvider:)

**Framework**: ClockKit  
**Kind**: init  
**Role**: Initializer

Creates a new template with a closed circular gauge and an image in the center.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
init(gaugeProvider: CLKGaugeProvider, imageProvider: CLKFullColorImageProvider)
```

```objc
- (instancetype) initWithGaugeProvider:(CLKGaugeProvider *) gaugeProvider imageProvider:(CLKFullColorImageProvider *) imageProvider;
```

## Parameters

- `gaugeProvider`: The gauge provider for the template.
- `imageProvider`: The image provider for the image at the center of the template. This template uses a full-color image.

## See Also

### Creating the Template
- [+ templateWithGaugeProvider:imageProvider:](./templatewithgaugeprovider_imageprovider_.md)
  Returns a new template with a closed circular gauge and an image in the center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplategraphicextralargecircularclosedgaugeimage/init(gaugeprovider:imageprovider:))*