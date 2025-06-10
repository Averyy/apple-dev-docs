# init(image:title:subtitle:)

**Framework**: CarPlay  
**Kind**: init

Initialize an element that is constituted of an image, title and subtitle. Only image is required while the two others can be omitted.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
@MainActor
init(image: UIImage, title: String?, subtitle: String?)
```

#### Discussion

When providing an image, your app should provide a @c UIImage that is display-ready. If necessary for the image, provide light and dark styles by using an asset from your asset catalog, prepared with light and dark styles or by using @c UIImageAsset to combine two @c UIImage instances into a single image with both styles.

UIImageAsset is used to combine multiple UIImages with different trait collections into a single UIImage.

> **Note**: The expected image size is given by +[CPListImageRowItemRowElement maximumImageSize]. Images provided will be resized to this size if necessary.

To properly size your images, your app should size them to the display scale of the car screen. See -[CPInterfaceController carTraitCollection].

## Parameters

- `image`: The image associated to the element.
- `title`: The title of the element.
- `subtitle`: The subtitle of the element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitemrowelement/init(image:title:subtitle:))*