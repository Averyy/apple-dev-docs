# largeContentSizeImage

**Framework**: UIKit  
**Kind**: property

The image to display for users who are blind or have low vision.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var largeContentSizeImage: UIImage? { get set }
```

#### Discussion

Use this property to specify a high-resolution version of the item’s image. When displaying an assistive interface for users who are blind or have low vision, UIKit displays this image instead of the standard image. The default value of this property is `nil`.

If you don’t specify an image for this property, UIKit scales the image that you specified in the [`image`](uibaritem/image.md) property.

## See Also

- [var title: String?](uibaritem/title.md)
  The title displayed on the item.
- [var image: UIImage?](uibaritem/image.md)
  The image used to represent the item.
- [var landscapeImagePhone: UIImage?](uibaritem/landscapeimagephone.md)
  The image to use to represent the item in landscape orientation when using the iPhone appearance idiom.
- [var imageInsets: UIEdgeInsets](uibaritem/imageinsets.md)
  The image inset or outset for each edge.
- [var landscapeImagePhoneInsets: UIEdgeInsets](uibaritem/landscapeimagephoneinsets.md)
  The image inset or outset for each edge of the image in landscape orientation when using the iPhone appearance idiom.
- [var largeContentSizeImageInsets: UIEdgeInsets](uibaritem/largecontentsizeimageinsets.md)
  The insets to apply to the bar item’s large image when displaying the image in an assistive UI.
- [var isEnabled: Bool](uibaritem/isenabled.md)
  A Boolean value indicating whether the item is enabled.
- [var tag: Int](uibaritem/tag.md)
  The bar item’s tag, an app-supplied integer that you can use to identify bar item objects in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibaritem/largecontentsizeimage)*