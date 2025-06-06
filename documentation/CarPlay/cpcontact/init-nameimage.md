# init(name:image:)

**Framework**: CarPlay  
**Kind**: init

Creates a contact with a name and an image.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
init(name: String, image: UIImage)
```

#### Return Value

A new contact with the provided name and image.

#### Discussion

Provide an image that is display-ready. If necessary, provide light and dark variants using an asset catalog, or use an instance of [`UIImageAsset`](https://developer.apple.com/documentation/UIKit/UIImageAsset) and register an image for each interface style. To properly size your image, use the display scale of the vehicle’s primary screen, which you access from your interface controller’s [`carTraitCollection`](cpinterfacecontroller/cartraitcollection.md) property.

CarPlay doesn’t support animated images. If you provide an animated image, CarPlay uses only the first image in the animation sequence.

## Parameters

- `name`: The name that the template displays.
- `image`: The image that the template displays beside the contact’s name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpcontact/init(name:image:))*