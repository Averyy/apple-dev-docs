# init(imageProvider:fillFraction:ringStyle:)

**Framework**: ClockKit  
**Kind**: init

Creates a new template from the provided image, fill fraction, and ring style.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
init(imageProvider: CLKImageProvider, fillFraction: Float, ringStyle: CLKComplicationRingStyle)
```

## Parameters

- `imageProvider`: The image provider for the main image. The system renders the image as a tinted template image, a bitmap image where only the opacity of the image matters. For more information, see [`Providing images for different appearances`](https://developer.apple.com/documentation/uikit/providing-images-for-different-appearances).
- `fillFraction`: A value between `0.0` and `1.0` that indicates how much of the ring fills.
- `ringStyle`: The ring’s style. For a complete list of styles, see [`CLKComplicationRingStyle`](clkcomplicationringstyle.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationtemplatecircularsmallringimage/init(imageprovider:fillfraction:ringstyle:))*