# imageView

**Framework**: TVUIKit  
**Kind**: property  
**Role**: Instance Property

The image view associated with the poster view.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
var imageView: UIImageView { get }
```

```objc
@property (nonatomic, strong, readonly) UIImageView * imageView;
```

#### Discussion

Use the image view to add additional information, such as overlays or badges, to the main content image. Don’t set an image directly on the image view. Always use the poster view’s [`image`](./image.md) property.

## See Also

### Configuring a Poster View
- [var image: UIImage?](./image.md)
  The image for the poster view.
- [var title: String?](./title.md)
  The title for the poster view.
- [var subtitle: String?](./subtitle.md)
  The subtitle for the poster view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvposterview/imageview)*