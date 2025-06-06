# largeContentSizeImageInsets

**Framework**: UIKit  
**Kind**: property

The insets to apply to the bar item’s large image when displaying the image in an assistive UI.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var largeContentSizeImageInsets: UIEdgeInsets { get set }
```

#### Discussion

The default value of this property is [`zero`](uiedgeinsets/zero.md).

## See Also

- [var title: String?](uibaritem/title.md)
  The title displayed on the item.
- [var image: UIImage?](uibaritem/image.md)
  The image used to represent the item.
- [var landscapeImagePhone: UIImage?](uibaritem/landscapeimagephone.md)
  The image to use to represent the item in landscape orientation when using the iPhone appearance idiom.
- [var largeContentSizeImage: UIImage?](uibaritem/largecontentsizeimage.md)
  The image to display for users who are blind or have low vision.
- [var imageInsets: UIEdgeInsets](uibaritem/imageinsets.md)
  The image inset or outset for each edge.
- [var landscapeImagePhoneInsets: UIEdgeInsets](uibaritem/landscapeimagephoneinsets.md)
  The image inset or outset for each edge of the image in landscape orientation when using the iPhone appearance idiom.
- [var isEnabled: Bool](uibaritem/isenabled.md)
  A Boolean value indicating whether the item is enabled.
- [var tag: Int](uibaritem/tag.md)
  The bar item’s tag, an app-supplied integer that you can use to identify bar item objects in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibaritem/largecontentsizeimageinsets)*