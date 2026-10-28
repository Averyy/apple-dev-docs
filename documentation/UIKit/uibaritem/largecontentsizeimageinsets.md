# largeContentSizeImageInsets

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The insets to apply to the bar item’s large image when displaying the image in an assistive UI.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var largeContentSizeImageInsets: UIEdgeInsets { get set }
```

```objc
@property (nonatomic) UIEdgeInsets largeContentSizeImageInsets;
```

## Discussion

The default value of this property is [`zero`](../uiedgeinsets/zero.md).

## See Also

### Getting and setting properties
- [var title: String?](./title.md)
  The title displayed on the item.
- [var image: UIImage?](./image.md)
  The image used to represent the item.
- [var landscapeImagePhone: UIImage?](./landscapeimagephone.md)
  The image to use to represent the item in landscape orientation when using the iPhone appearance idiom.
- [var largeContentSizeImage: UIImage?](./largecontentsizeimage.md)
  The image to display for users who are blind or have low vision.
- [var imageInsets: UIEdgeInsets](./imageinsets.md)
  The image inset or outset for each edge.
- [var landscapeImagePhoneInsets: UIEdgeInsets](./landscapeimagephoneinsets.md)
  The image inset or outset for each edge of the image in landscape orientation when using the iPhone appearance idiom.
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value indicating whether the item is enabled.
- [var tag: Int](./tag.md)
  The bar item’s tag, an app-supplied integer that you can use to identify bar item objects in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibaritem/largecontentsizeimageinsets)*