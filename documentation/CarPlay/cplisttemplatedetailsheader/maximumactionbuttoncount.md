# maximumActionButtonCount

**Framework**: CarPlay  
**Kind**: property  
**Role**: Type Property

The maximum number of action buttons the header can display.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
class var maximumActionButtonCount: Int { get }
```

```objc
@property (class, nonatomic, readonly) NSInteger maximumActionButtonCount;
```

## Discussion

When configuring a header, use this class property to determine how many [`CPButton`](../cpbutton.md) types you can include in the header. CarPlay limits the total number of buttons to ensure usability and a readable layout. If you configure the header with more than the maximum number of buttons, CarPlay ignores any extra buttons.

## See Also

### Creating a details header
- [init(thumbnail: CPThumbnailImage, title: String?, subtitle: String?, actionButtons: [CPButton])](./init%28thumbnail,title,subtitle,actionbuttons%29.md)
  Creates a details header with a thumbnail image, optional text, and action buttons.
- [init(thumbnail: CPThumbnailImage, title: String?, subtitle: String?, bodyVariants: [NSAttributedString], actionButtons: [CPButton])](./init%28thumbnail,title,subtitle,bodyvariants,actionbuttons%29.md)
  Creates a details header with a thumbnail image, optional text, and action buttons.
- [init?(coder: NSCoder)](./init%28coder%29.md)
- [class var maximumActionButtonSize: CGSize](./maximumactionbuttonsize.md)
  The maximum size of the images you use to create action buttons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplatedetailsheader/maximumactionbuttoncount)*