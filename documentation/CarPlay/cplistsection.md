# CPListSection

**Framework**: CarPlay  
**Kind**: class

A container that groups your list items into sections.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class CPListSection
```

#### Overview

A section contains zero or more list items. You can configure a section to display a header and a section index title, which CarPlay displays on the trailing edge of the screen. The section header and the section index title are optional.

To create a section, call the [`initWithItems:`](cplistsection/initwithitems:.md) method and provide an array of list items. Alternatively, use [`initWithItems:header:sectionIndexTitle:`](cplistsection/initwithitems:header:sectionindextitle:.md) if you want to display a header and a section index title. CarPlay doesn’t support custom list items, so you must use one of the types that the framework provides, such as [`CPListItem`](cplistitem.md) or [`CPListImageRowItem`](cplistimagerowitem.md).

At runtime, use [`maximumSectionCount`](cplisttemplate/maximumsectioncount.md) to determine the maximum number of sections that your list can display. When creating items for your sections, use [`maximumItemCount`](cplisttemplate/maximumitemcount.md) to establish the maximum number of items across all sections that can appear in your list.

## Topics

### Creating a Section
- [init(items: [any CPListTemplateItem], header: String, headerSubtitle: String?, headerImage: UIImage?, headerButton: CPButton?, sectionIndexTitle: String?)](cplistsection/init(items:header:headersubtitle:headerimage:headerbutton:sectionindextitle:).md)
  Creates a section with list items, a header, a section index title, and section header details.
- [protocol CPListTemplateItem](cplisttemplateitem.md)
  A description of the common properties of all list item types.
- [protocol CPSelectableListItem](cpselectablelistitem.md)
  A description of a selectable list item.
- [class CPListItem](cplistitem.md)
  A selectable row in a list template.
- [class CPListImageRowItem](cplistimagerowitem.md)
  A list template row that displays a series of images.
- [class CPMessageListItem](cpmessagelistitem.md)
  A list template row that represents a conversation or contact.
### Getting Supplementary Information
- [var header: String?](cplistsection/header.md)
  The section’s header text.
- [var sectionIndexTitle: String?](cplistsection/sectionindextitle.md)
  The section’s index title.
### Getting Items
- [var items: [any CPListTemplateItem]](cplistsection/items.md)
  The list of items for the section.
- [func index(of: any CPListTemplateItem) -> Int](cplistsection/index(of:).md)
  Returns the index of the specified item.
- [func item(at: Int) -> any CPListTemplateItem](cplistsection/item(at:).md)
  Returns the item at the specified index.
### Configuring Section Headers
- [var headerButton: CPButton?](cplistsection/headerbutton.md)
  A button that the section header displays.
- [var headerImage: UIImage?](cplistsection/headerimage.md)
  An image that the section header displays.
- [var headerSubtitle: String?](cplistsection/headersubtitle.md)
  A string that the header displays as a subtitle.
### Initializers
- [convenience init(items: [CPListItem])](cplistsection/init(items:)-32d0q.md)
- [convenience init(items: [CPListItem], header: String?, sectionIndexTitle: String?)](cplistsection/init(items:header:sectionindextitle:)-743we.md)
- [convenience init(items: [any CPListTemplateItem])](cplistsection/init(items:)-6ksy3.md)
- [convenience init(items: [any CPListTemplateItem], header: String?, sectionIndexTitle: String?)](cplistsection/init(items:header:sectionindextitle:)-6xewg.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class var maximumSectionCount: Int](cplisttemplate/maximumsectioncount.md)
  The maximum number of sections that the template can display.
- [var sectionCount: Int](cplisttemplate/sectioncount.md)
  The number of sections in the list.
- [var sections: [CPListSection]](cplisttemplate/sections.md)
  The sections that the list displays.
- [func updateSections([CPListSection])](cplisttemplate/updatesections(_:).md)
  Adds, removes, reorders, or updates the list’s sections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistsection)*