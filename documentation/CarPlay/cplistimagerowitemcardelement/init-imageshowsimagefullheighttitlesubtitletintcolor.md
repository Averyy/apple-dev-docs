# init(image:showsImageFullHeight:title:subtitle:tintColor:)

**Framework**: CarPlay  
**Kind**: init

Initialize an element that is constituted of an image, boolean to entirely cover the element with the image, title, subtitle and a tint color.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
@MainActor
init(image: UIImage, showsImageFullHeight: Bool, title: String?, subtitle: String?, tintColor: UIColor?)
```

#### Discussion

When providing an image, your app should provide a @c UIImage that is display-ready. If necessary for the image, provide light and dark styles by using an asset from your asset catalog, prepared with light and dark styles or by using @c UIImageAsset to combine two @c UIImage instances into a single image with both styles.

UIImageAsset is used to combine multiple UIImages with different trait collections into a single UIImage.

> **Note**: The expected image size is given by +[CPListImageRowItemCardElement maximumImageSize] or by +[CPListImageRowItemCardElement maximumFullHeightImageSize] if @c showsImageFullHeight is true. Images provided will be resized to this size if necessary.

To properly size your images, your app should size them to the display scale of the car screen. See -[CPInterfaceController carTraitCollection].

## Parameters

- `image`: The image associated to the element.
- `showsImageFullHeight`: Determines if the image should entirely cover the card
- `title`: The title of the element.
- `subtitle`: The subtitle of the element.
- `tintColor`: The color used as background if @c showsImageFullHeight is true, part of the gradient color at the bottom of the card otherwise.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitemcardelement/init(image:showsimagefullheight:title:subtitle:tintcolor:))*