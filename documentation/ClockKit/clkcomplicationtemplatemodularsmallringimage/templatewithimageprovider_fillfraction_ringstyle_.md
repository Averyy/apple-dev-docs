# templateWithImageProvider:fillFraction:ringStyle:

**Framework**: ClockKit  
**Kind**: method  
**Role**: Type Method

Returns a new template from the provided image, fill fraction, and ring style.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

## Declaration

```objc
+ (instancetype) templateWithImageProvider:(CLKImageProvider *) imageProvider fillFraction:(float) fillFraction ringStyle:(CLKComplicationRingStyle) ringStyle;
```

## Parameters

- `imageProvider`: The image provider for the center image. The system renders the image as a tinted template image, a bitmap image where only the opacity of the image matters. For more information, see [Providing images for different appearances](../../UIKit/providing-images-for-different-appearances.md).
- `fillFraction`: A value between `0.0` and `1.0` that indicates how much of the ring fills.
- `ringStyle`: The ring’s style. For a complete list of styles, see [`CLKComplicationRingStyle`](../clkcomplicationringstyle.md).

## See Also

### Creating the Template
- [init(imageProvider: CLKImageProvider, fillFraction: Float, ringStyle: CLKComplicationRingStyle)](./init%28imageprovider,fillfraction,ringstyle%29.md)
  Creates a new template from the provided image, fill fraction, and ring style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatemodularsmallringimage/templatewithimageprovider:fillfraction:ringstyle:)*