# pinImage

**Framework**: CarPlay  
**Kind**: property

A custom image that the map annotation displays.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var pinImage: UIImage? { get set }
```

#### Discussion

Provide an image that is display-ready. If necessary, provide light and dark variants using an asset catalog, or use an instance of [`UIImageAsset`](https://developer.apple.com/documentation/UIKit/UIImageAsset) and register an image for each interface style. To properly size your image, use the display scale of the vehicle’s primary screen from your interface controller’s [`carTraitCollection`](cpinterfacecontroller/cartraitcollection.md) property.

CarPlay doesn’t support animated images. If you provide an animated image, CarPlay uses only the first image in the animation sequence.

## See Also

- [var location: MKMapItem](cppointofinterest/location.md)
  The map item that contains the point of interest’s geographical information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cppointofinterest/pinimage)*