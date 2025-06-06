# CPSelectableListItem

**Framework**: CarPlay  
**Kind**: protocol

A description of a selectable list item.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
protocol CPSelectableListItem : CPListTemplateItem
```

#### Overview

> ❗ **Important**:  You don’t create custom classes that conform to `CPSelectableListItem`. Instead, you use one of the prebuilt list item types that adopt this protocol, such as [`CPListItem`](cplistitem.md) or [`CPListImageRowItem`](cplistimagerowitem.md).

 You don’t create custom classes that conform to `CPSelectableListItem`. Instead, you use one of the prebuilt list item types that adopt this protocol, such as [`CPListItem`](cplistitem.md) or [`CPListImageRowItem`](cplistimagerowitem.md).

## Topics

### Managing Selection
- [var handler: ((any CPSelectableListItem, () -> Void) -> Void)?](cpselectablelistitem/handler.md)
  An optional closure that CarPlay invokes when the user selects the list item.

## Relationships

### Inherits From
- [CPListTemplateItem](cplisttemplateitem.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [CPListImageRowItem](cplistimagerowitem.md)
- [CPListItem](cplistitem.md)

## See Also

- [init(items: [any CPListTemplateItem], header: String, headerSubtitle: String?, headerImage: UIImage?, headerButton: CPButton?, sectionIndexTitle: String?)](cplistsection/init(items:header:headersubtitle:headerimage:headerbutton:sectionindextitle:).md)
  Creates a section with list items, a header, a section index title, and section header details.
- [protocol CPListTemplateItem](cplisttemplateitem.md)
  A description of the common properties of all list item types.
- [class CPListItem](cplistitem.md)
  A selectable row in a list template.
- [class CPListImageRowItem](cplistimagerowitem.md)
  A list template row that displays a series of images.
- [class CPMessageListItem](cpmessagelistitem.md)
  A list template row that represents a conversation or contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpselectablelistitem)*