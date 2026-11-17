# init(thumbnail:title:subtitle:bodyVariants:actionButtons:)

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
init(thumbnail: CPThumbnailImage, title: String?, subtitle: String?, bodyVariants: [NSAttributedString], actionButtons: [CPButton])
```

```objc
- (instancetype) initWithThumbnail:(CPThumbnailImage *) thumbnail title:(NSString *) title subtitle:(NSString *) subtitle bodyVariants:(NSArray<NSAttributedString *> *) bodyVariants actionButtons:(NSArray<CPButton *> *) actionButtons;
```

## Return Value

An initialized header object you can assign to your [`CPListTemplate`](../cplisttemplate.md) object.

## Discussion

Although the `title` and `subtitle` parameters are optional, provide one or both whenever possible to convey meaningful information. For example, if the list shows the songs of an album, you might display the album title in the header.

## Parameters

- `thumbnail`: The thumbnail image to display in the header. This type displays the image you specify plus optional overlay content.
- `title`: The primary text to display in the header. Specify `nil` if you don’t want to display the title text.
- `subtitle`: The secondary text to display below the title. Specify `nil` if you don’t want to display the subtitle text.
- `bodyVariants`: Additional text to display below the `subtitle`. Specify strings in the preferred display order, and provide strings of different lengths. CarPlay chooses the first string from the array that fits the available space. Specify `nil` if you don’t want to display any text below the subtitle.
- `actionButtons`: An array of actions someone can perform. CarPlay displays the buttons in the same order they appear in the array. The [`maximumActionButtonCount`](./maximumactionbuttoncount.md) property specifies the maximum number of buttons that CarPlay includes in the header. If your array contains more buttons than the maximum, CarPlay ignores any extra buttons.

## See Also

### Creating a details header
- [init(thumbnail: CPThumbnailImage, title: String?, subtitle: String?, actionButtons: [CPButton])](./init%28thumbnail,title,subtitle,actionbuttons%29.md)
  Creates a details header with a thumbnail image, optional text, and action buttons.
- [init?(coder: NSCoder)](./init%28coder%29.md)
- [class var maximumActionButtonCount: Int](./maximumactionbuttoncount.md)
  The maximum number of action buttons the header can display.
- [class var maximumActionButtonSize: CGSize](./maximumactionbuttonsize.md)
  The maximum size of the images you use to create action buttons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplatedetailsheader/init(thumbnail:title:subtitle:bodyvariants:actionbuttons:))*