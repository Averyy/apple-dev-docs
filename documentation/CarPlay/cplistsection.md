# CPListSection

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A container that groups your list items into sections.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class CPListSection
```

```objc
@interface CPListSection : NSObject
```

#### Overview

A section contains zero or more list items. You can configure a section to display a header and a section index title, which CarPlay displays on the trailing edge of the screen. The section header and the section index title are optional.

To create a section, call the [`initWithItems:`](./cplistsection/initwithitems_.md) method and provide an array of list items. Alternatively, use [`initWithItems:header:sectionIndexTitle:`](./cplistsection/initwithitems_header_sectionindextitle_.md) if you want to display a header and a section index title. CarPlay doesn’t support custom list items, so you must use one of the types that the framework provides, such as [`CPListItem`](./cplistitem.md) or [`CPListImageRowItem`](./cplistimagerowitem.md).

At runtime, use [`maximumSectionCount`](./cplisttemplate/maximumsectioncount.md) to determine the maximum number of sections that your list can display. When creating items for your sections, use [`maximumItemCount`](./cplisttemplate/maximumitemcount.md) to establish the maximum number of items across all sections that can appear in your list.

## Topics

### Creating a Section
- [init(items: [any CPListTemplateItem], header: String, headerSubtitle: String?, headerImage: UIImage?, headerButton: CPButton?, sectionIndexTitle: String?)](./cplistsection/init%28items,header,headersubtitle,headerimage,headerbutton,sectionindextitle%29.md)
  Creates a section with list items, a header, a section index title, and section header details.
- [protocol CPListTemplateItem](./cplisttemplateitem.md)
  A description of the common properties of all list item types.
- [protocol CPSelectableListItem](./cpselectablelistitem.md)
  A description of a selectable list item.
- [class CPListItem](./cplistitem.md)
  A selectable row in a list template.
- [class CPListImageRowItem](./cplistimagerowitem.md)
  A list template row that displays a series of images.
- [class CPMessageListItem](./cpmessagelistitem.md)
  A list template row that represents a conversation or contact.
- [- initWithItems:](./cplistsection/initwithitems_.md)
  Creates a section with list items.
- [- initWithItems:header:sectionIndexTitle:](./cplistsection/initwithitems_header_sectionindextitle_.md)
  Creates a section with list items, a header, and a section index title.
### Getting Supplementary Information
- [var header: String?](./cplistsection/header.md)
  The section’s header text.
- [var sectionIndexTitle: String?](./cplistsection/sectionindextitle.md)
  The section’s index title.
### Getting Items
- [var items: [any CPListTemplateItem]](./cplistsection/items.md)
  The list of items for the section.
- [func index(of: any CPListTemplateItem) -> Int](./cplistsection/index%28of%29.md)
  Returns the index of the specified item.
- [func item(at: Int) -> any CPListTemplateItem](./cplistsection/item%28at%29.md)
  Returns the item at the specified index.
### Configuring Section Headers
- [var headerButton: CPButton?](./cplistsection/headerbutton.md)
  A button that the section header displays.
- [var headerImage: UIImage?](./cplistsection/headerimage.md)
  An image that the section header displays.
- [var headerSubtitle: String?](./cplistsection/headersubtitle.md)
  A string that the header displays as a subtitle.
### Initializers
- [convenience init(items: [CPListItem])](./cplistsection/init%28items%29-32d0q.md)
- [convenience init(items: [CPListItem], header: String?, sectionIndexTitle: String?)](./cplistsection/init%28items,header,sectionindextitle%29-743we.md)
- [init?(coder: NSCoder)](./cplistsection/init%28coder%29.md)
- [convenience init(items: [any CPListTemplateItem])](./cplistsection/init%28items%29-6ksy3.md)
- [convenience init(items: [any CPListTemplateItem], header: String?, sectionIndexTitle: String?)](./cplistsection/init%28items,header,sectionindextitle%29-6xewg.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Managing Sections
- [class var maximumSectionCount: Int](./cplisttemplate/maximumsectioncount.md)
  The maximum number of sections that the template can display.
- [var sectionCount: Int](./cplisttemplate/sectioncount.md)
  The number of sections in the list.
- [var sections: [CPListSection]](./cplisttemplate/sections.md)
  The sections that the list displays.
- [func updateSections([CPListSection])](./cplisttemplate/updatesections%28_%29.md)
  Adds, removes, reorders, or updates the list’s sections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistsection)*