# imageView

**Framework**: TVUIKit  
**Kind**: property

The image view associated with the poster view.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
@MainActor
var imageView: UIImageView { get }
```

#### Discussion

Use the image view to add additional information, such as overlays or badges, to the main content image. Don’t set an image directly on the image view. Always use the poster view’s [`image`](tvposterview/image.md) property.

## See Also

- [var image: UIImage?](tvposterview/image.md)
  The image for the poster view.
- [var title: String?](tvposterview/title.md)
  The title for the poster view.
- [var subtitle: String?](tvposterview/subtitle.md)
  The subtitle for the poster view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvposterview/imageview)*