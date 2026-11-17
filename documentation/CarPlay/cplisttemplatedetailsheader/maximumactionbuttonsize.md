# maximumActionButtonSize

**Framework**: CarPlay  
**Kind**: property  
**Role**: Type Property

The maximum size of the images you use to create action buttons.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
class var maximumActionButtonSize: CGSize { get }
```

```objc
@property (class, nonatomic, readonly) CGSize maximumActionButtonSize;
```

## Discussion

An action button displays an image to represent the intended action. This property contains the maximum supported image dimensions in points.

## See Also

### Creating a details header
- [init(thumbnail: CPThumbnailImage, title: String?, subtitle: String?, actionButtons: [CPButton])](./init%28thumbnail,title,subtitle,actionbuttons%29.md)
  Creates a details header with a thumbnail image, optional text, and action buttons.
- [init(thumbnail: CPThumbnailImage, title: String?, subtitle: String?, bodyVariants: [NSAttributedString], actionButtons: [CPButton])](./init%28thumbnail,title,subtitle,bodyvariants,actionbuttons%29.md)
  Creates a details header with a thumbnail image, optional text, and action buttons.
- [init?(coder: NSCoder)](./init%28coder%29.md)
- [class var maximumActionButtonCount: Int](./maximumactionbuttoncount.md)
  The maximum number of action buttons the header can display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplatedetailsheader/maximumactionbuttonsize)*