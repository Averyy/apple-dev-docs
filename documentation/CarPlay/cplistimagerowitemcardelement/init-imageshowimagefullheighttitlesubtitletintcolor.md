# init(image:showImageFullHeight:title:subtitle:tintColor:)

**Framework**: CarPlay  
**Kind**: init

Initialize an element that is constituted of an image, boolean to entierely cover the element with the image, title, subtitle and a tint color.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
@MainActor
init(image: UIImage, showImageFullHeight: Bool, title: String?, subtitle: String?, tintColor: UIColor?)
```

#### Discussion

When providing an image, your app should provide a @c UIImage that is display-ready. If necessary for the image, provide light and dark styles by using an asset from your asset catalog, prepared with light and dark styles or by using @c UIImageAsset to combine two @c UIImage instances into a single image with both styles.

UIImageAsset is used to combine multiple UIImages with different trait collections into a single UIImage.

> **Note**: The expected image size is given by +[CPListImageRowItemCardElement maximumImageSize] or by +[CPListImageRowItemCardElement maximumFullHeightImageSize] if @c showImageFullHeight is true. Images provided will be resized to this size if necessary.

@c title should be non-nil when @c showImageFullHeight is true.

To properly size your images, your app should size them to the display scale of the car screen. See -[CPInterfaceController carTraitCollection].

## Parameters

- `image`: The image associated to the element.
- `showImageFullHeight`: Determines if the image should entierely cover the card
- `title`: The title of the element.
- `subtitle`: The subtitle of the element.
- `tintColor`: The color used as background if @c showImageFullHeight is true, part of the gradient color at the bottom of the card otherwise.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitemcardelement/init(image:showimagefullheight:title:subtitle:tintcolor:))*