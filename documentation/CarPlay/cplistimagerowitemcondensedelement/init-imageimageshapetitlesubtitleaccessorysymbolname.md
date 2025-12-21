# init(image:imageShape:title:subtitle:accessorySymbolName:)

**Framework**: CarPlay  
**Kind**: init

Initialize a list image row condensed element with an image, an image shape, a title, subtitle and a system symbol name.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
@MainActor
init(image: UIImage, imageShape: CPListImageRowItemCondensedElement.Shape, title: String, subtitle: String?, accessorySymbolName: String?)
```

## Parameters

- `image`: The image associated to the element.
- `imageShape`: The @c CPListImageRowItemCondensedElementShape shape being applied on the image.
- `title`: The title of the element.
- `subtitle`: The subtitle of the element.
- `accessorySymbolName`: The system symbol used as an accessory view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitemcondensedelement/init(image:imageshape:title:subtitle:accessorysymbolname:))*