# image

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The contact’s image.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var image: UIImage { get set }
```

```objc
@property (nonatomic, strong) UIImage * image;
```

#### Discussion

Provide an image that is display-ready. If necessary, provide light and dark variants using an asset catalog, or use an instance of [`UIImageAsset`](../../UIKit/uiimageasset.md) and register an image for each interface style. To properly size your image, use the display scale of the vehicle’s primary screen, which you access from your interface controller’s [`carTraitCollection`](../cpinterfacecontroller/cartraitcollection.md) property.

CarPlay doesn’t support animated images. If you provide an animated image, CarPlay uses only the first image in the animation sequence.

## See Also

### Configuring the Contact’s Attributes
- [var name: String](./name.md)
  The contact’s name.
- [var subtitle: String?](./subtitle.md)
  A subtitle that the template displays in addition to the contact’s name.
- [var informativeText: String?](./informativetext.md)
  Additional text that the template displays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpcontact/image)*