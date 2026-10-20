# init(imageProvider:fillFraction:ringStyle:)

**Framework**: ClockKit  
**Kind**: init  
**Role**: Initializer

Creates a new template from the provided image, fill fraction, and ring style.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

## Declaration

```swift
init(imageProvider: CLKImageProvider, fillFraction: Float, ringStyle: CLKComplicationRingStyle)
```

```objc
- (instancetype) initWithImageProvider:(CLKImageProvider *) imageProvider fillFraction:(float) fillFraction ringStyle:(CLKComplicationRingStyle) ringStyle;
```

## Parameters

- `imageProvider`: The image provider for the main image. The system renders the image as a tinted template image, a bitmap image where only the opacity of the image matters. For more information, see [Providing images for different appearances](../../UIKit/providing-images-for-different-appearances.md).
- `fillFraction`: A value between `0.0` and `1.0` that indicates how much of the ring fills.
- `ringStyle`: The ring’s style. For a complete list of styles, see [`CLKComplicationRingStyle`](../clkcomplicationringstyle.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplateutilitariansmallringimage/init(imageprovider:fillfraction:ringstyle:))*