# initWithItems:

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Creates a section with list items.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```objc
- (instancetype) initWithItems:(NSArray<id<CPListTemplateItem>> *) items;
```

#### Return Value

A newly initialized list section.

## Parameters

- `items`: A list of items to include in the section.

## See Also

### Creating a Section
- [- initWithItems:header:sectionIndexTitle:](./initwithitems_header_sectionindextitle_.md)
  Creates a section with list items, a header, and a section index title.
- [init(items: [any CPListTemplateItem], header: String, headerSubtitle: String?, headerImage: UIImage?, headerButton: CPButton?, sectionIndexTitle: String?)](./init%28items,header,headersubtitle,headerimage,headerbutton,sectionindextitle%29.md)
  Creates a section with list items, a header, a section index title, and section header details.
- [protocol CPListTemplateItem](../cplisttemplateitem.md)
  A description of the common properties of all list item types.
- [protocol CPSelectableListItem](../cpselectablelistitem.md)
  A description of a selectable list item.
- [class CPListItem](../cplistitem.md)
  A selectable row in a list template.
- [class CPListImageRowItem](../cplistimagerowitem.md)
  A list template row that displays a series of images.
- [class CPMessageListItem](../cpmessagelistitem.md)
  A list template row that represents a conversation or contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistsection/initwithitems:)*