# isEnabled

**Framework**: UIKit  
**Kind**: property

A Boolean value indicating whether the item is enabled.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isEnabled: Bool { get set }
```

#### Discussion

If [`false`](https://developer.apple.com/documentation/swift/false), the item is drawn partially dimmed to indicate it’s disabled. The default value is [`true`](https://developer.apple.com/documentation/swift/true).

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
- [var largeContentSizeImageInsets: UIEdgeInsets](uibaritem/largecontentsizeimageinsets.md)
  The insets to apply to the bar item’s large image when displaying the image in an assistive UI.
- [var tag: Int](uibaritem/tag.md)
  The bar item’s tag, an app-supplied integer that you can use to identify bar item objects in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibaritem/isenabled)*