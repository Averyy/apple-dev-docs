# tag

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The bar item’s tag, an app-supplied integer that you can use to identify bar item objects in your app.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var tag: Int { get set }
```

```objc
@property (nonatomic) NSInteger tag;
```

## Discussion

The default value is `0`.

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
- [var largeContentSizeImageInsets: UIEdgeInsets](./largecontentsizeimageinsets.md)
  The insets to apply to the bar item’s large image when displaying the image in an assistive UI.
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value indicating whether the item is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibaritem/tag)*