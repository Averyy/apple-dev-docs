# init(items:header:headerSubtitle:headerImage:headerButton:sectionIndexTitle:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Creates a section with list items, a header, a section index title, and section header details.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
init(items: [any CPListTemplateItem], header: String, headerSubtitle: String?, headerImage: UIImage?, headerButton: CPButton?, sectionIndexTitle: String?)
```

```objc
- (instancetype) initWithItems:(NSArray<id<CPListTemplateItem>> *) items header:(NSString *) header headerSubtitle:(NSString *) headerSubtitle headerImage:(UIImage *) headerImage headerButton:(CPButton *) headerButton sectionIndexTitle:(NSString *) sectionIndexTitle;
```

## Return Value

A newly initialized list section.

## Discussion

CarPlay formats the header content based on the information you provide.

## Parameters

- `items`: The items to include in the section. CarPlay displays your items in the same order as your array. You can specify only [`CPListItem`](../cplistitem.md), [`CPListImageRowItem`](../cplistimagerowitem.md), and [`CPMessageListItem`](../cpmessagelistitem.md) types in your array. You can’t specify custom types that conform to the [`CPListTemplateItem`](../cplisttemplateitem.md) protocol. If you specify an empty array, the list interface hides the section. Empty sections count against the maximum number of allowed sections.
- `header`: Text to display in the area immediately above the items.    - headerSubtitle: Secondary text to display below the `header` text.
- `headerImage`: An image to display in the header. If you initialize your image from an asset catalog resource, CarPlay manages light and dark variants of your image and switches them when needed. The [`CPMaximumListSectionImageSize`](../cpmaximumlistsectionimagesize.md) constant contains the maximum dimensions for the image.
- `headerButton`: An interactive button to display in the header. Include a button to give someone the ability to perform some section-related task.
- `sectionIndexTitle`: The string to display for this section in the index. For long lists, an index helps people navigate quickly to specific sections of content. If you specify a string with more than one character, CarPlay uses only the first character in the string.

## See Also

### Creating a section
- [convenience init(items: [any CPListTemplateItem])](./init%28items%29-6ksy3.md)
- [convenience init(items: [any CPListTemplateItem], header: String?, sectionIndexTitle: String?)](./init%28items,header,sectionindextitle%29-6xewg.md)
- [convenience init(items: [CPListItem])](./init%28items%29-32d0q.md)
- [convenience init(items: [CPListItem], header: String?, sectionIndexTitle: String?)](./init%28items,header,sectionindextitle%29-743we.md)
- [init?(coder: NSCoder)](./init%28coder%29.md)
- [let CPMaximumListSectionImageSize: CGSize](../cpmaximumlistsectionimagesize.md)
  The maximum size of images you include in section headers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistsection/init(items:header:headersubtitle:headerimage:headerbutton:sectionindextitle:))*