# init(thumbnail:title:subtitle:tintColor:)

**Framework**: CarPlay  
**Kind**: init

Initialize an element with a thumbnail, title, subtitle, and tint color.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
init(thumbnail: CPThumbnailImage, title: String?, subtitle: String?, tintColor: UIColor?)
```

#### Discussion

This initializer uses a CPThumbnailImage which encapsulates the image, aspect ratio, image, and sports overlay information.

## Parameters

- `thumbnail`: The thumbnail containing image, aspect ratio, image, and sports overlay information.
- `title`: The title of the element.
- `subtitle`: The subtitle of the element.
- `tintColor`: The color used for styling the element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitemcardelement/init(thumbnail:title:subtitle:tintcolor:))*