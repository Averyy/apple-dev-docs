# CPListSection

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A container that groups related items in a list interface.

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

## Overview

A `CPListSection` object contains one or more rows of a list interface and optional header information. In a list with a large number of rows, sections organize your content into logical groups so people can navigate it more easily. For example, an alphabetical list of songs might have sections for each letter of the alphabet. The section presents the rows in the order you specify and precedes them with any header information you provide.

Create a `CPSection` item and fill it with the items you want to display. A single section can mix and match different item types; for example, you can include [`CPListItem`](./cplistitem.md) and [`CPListImageRowItem`](./cplistimagerowitem.md) objects in the same section. If you want to display a header for the section, provide that information at creation time along with the items. To display the sections in a list, initialize your [`CPListTemplate`](./cplisttemplate.md) with the sections or call its [`updateSections(_:)`](./cplisttemplate/updatesections%28_%29.md) method.

> **Note**: The list interface displays a section only if it contains one or more items. Lists don’t display sections with zero items.

Vehicles can impose restrictions on the number of sections and items in a single list. Get the maximum number of supported sections from the [`maximumSectionCount`](./cplisttemplate/maximumsectioncount.md) property of [`CPListTemplate`](./cplisttemplate.md). Similarly, get the maximum number of items from the [`maximumItemCount`](./cplisttemplate/maximumitemcount.md) property.

## Topics

### Creating a section
- [convenience init(items: [any CPListTemplateItem])](./cplistsection/init%28items%29-6ksy3.md)
- [convenience init(items: [any CPListTemplateItem], header: String?, sectionIndexTitle: String?)](./cplistsection/init%28items,header,sectionindextitle%29-6xewg.md)
- [init(items: [any CPListTemplateItem], header: String, headerSubtitle: String?, headerImage: UIImage?, headerButton: CPButton?, sectionIndexTitle: String?)](./cplistsection/init%28items,header,headersubtitle,headerimage,headerbutton,sectionindextitle%29.md)
  Creates a section with list items, a header, a section index title, and section header details.
- [convenience init(items: [CPListItem])](./cplistsection/init%28items%29-32d0q.md)
- [convenience init(items: [CPListItem], header: String?, sectionIndexTitle: String?)](./cplistsection/init%28items,header,sectionindextitle%29-743we.md)
- [init?(coder: NSCoder)](./cplistsection/init%28coder%29.md)
- [let CPMaximumListSectionImageSize: CGSize](./cpmaximumlistsectionimagesize.md)
  The maximum size of images you include in section headers.
### Getting the section’s header content
- [var header: String?](./cplistsection/header.md)
  The main text to display in the header area of the section.
- [var headerSubtitle: String?](./cplistsection/headersubtitle.md)
  The secondary text to display in the header area of the section.
- [var headerButton: CPButton?](./cplistsection/headerbutton.md)
  The button to display in the header area of the section.
- [var headerImage: UIImage?](./cplistsection/headerimage.md)
  The image to display in the header area of the section.
### Locating items in the section
- [var items: [any CPListTemplateItem]](./cplistsection/items.md)
  The items in the section.
- [func index(of: any CPListTemplateItem) -> Int](./cplistsection/index%28of%29.md)
  Returns the zero-based index of an item in the section.
- [func item(at: Int) -> any CPListTemplateItem](./cplistsection/item%28at%29.md)
  Returns the item at the specified index in the section.
### Getting the index string
- [var sectionIndexTitle: String?](./cplistsection/sectionindextitle.md)
  The string that identifies the current session in an index.
### Instance Methods
- [- initWithItems:](./cplistsection/initwithitems_.md)
  Creates a section with the provided items.
- [- initWithItems:header:sectionIndexTitle:](./cplistsection/initwithitems_header_sectionindextitle_.md)
  Creates a section with the provided items and header information.

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

### Lists
- [class CPListTemplate](./cplisttemplate.md)
  A template that displays a single-column list of items in one of several visual styles.
- [class CPListItem](./cplistitem.md)
  A selectable row in a list interface.
- [class CPListImageRowItem](./cplistimagerowitem.md)
  A row type that displays multiple sub-elements horizontally in a variety of styles.
- [Supporting types for lists](./list-content.md)
  Create sections, single-line items, multi-element rows, headers, and other content for your list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistsection)*