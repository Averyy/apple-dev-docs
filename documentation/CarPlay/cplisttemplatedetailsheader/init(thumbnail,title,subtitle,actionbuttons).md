# init(thumbnail:title:subtitle:actionButtons:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates a details header with a thumbnail image, optional text, and action buttons.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
init(thumbnail: CPThumbnailImage, title: String?, subtitle: String?, actionButtons actionButton: [CPButton])
```

```objc
- (instancetype) initWithThumbnail:(CPThumbnailImage *) thumbnail title:(NSString *) title subtitle:(NSString *) subtitle actionButtons:(NSArray<CPButton *> *) actionButton;
```

## Return Value

An initialized details header you can assign to your [`CPListTemplate`](../cplisttemplate.md) object.

## Discussion

Although the `title` and `subtitle` parameters are optional, specify one or both whenever possible to convey meaningful information. For example, if the list shows the songs of an album, you might display the album title in the header.

## Parameters

- `thumbnail`: The thumbnail image to display in the header. This type displays the image you specify and any optional overlay content.
- `title`: The primary text to display in the header. Specify `nil` if you don’t want to display the title text.
- `subtitle`: The secondary text to display below the title. Specify `nil` if you don’t want to display the secondary text.

## See Also

### Creating a details header
- [init(thumbnail: CPThumbnailImage, title: String?, subtitle: String?, bodyVariants: [NSAttributedString], actionButtons: [CPButton])](./init%28thumbnail,title,subtitle,bodyvariants,actionbuttons%29.md)
  Creates a details header with a thumbnail image, optional text, and action buttons.
- [init?(coder: NSCoder)](./init%28coder%29.md)
- [class var maximumActionButtonCount: Int](./maximumactionbuttoncount.md)
  The maximum number of action buttons the header can display.
- [class var maximumActionButtonSize: CGSize](./maximumactionbuttonsize.md)
  The maximum size of the images you use to create action buttons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplatedetailsheader/init(thumbnail:title:subtitle:actionbuttons:))*