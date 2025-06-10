# CPListTemplateItem

**Framework**: CarPlay  
**Kind**: protocol

A description of the common properties of all list item types.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
protocol CPListTemplateItem : NSObjectProtocol
```

#### Overview

> ❗ **Important**:  You don’t create custom classes that conform to `CPListItemTemplate`. Instead, you use one of the prebuilt list item types that adopt this protocol, such as [`CPMessageListItem`](cpmessagelistitem.md).

## Topics

### Managing Content
- [var text: String?](cplisttemplateitem/text.md)
  The item’s primary text.
- [var userInfo: Any?](cplisttemplateitem/userinfo.md)
  An opaque value for the list item.
### Enabling Items
- [var isEnabled: Bool](cplisttemplateitem/isenabled.md)
  A Boolean value that indicates if the item is enabled.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [CPSelectableListItem](cpselectablelistitem.md)
### Conforming Types
- [CPListImageRowItem](cplistimagerowitem.md)
- [CPListItem](cplistitem.md)
- [CPMessageListItem](cpmessagelistitem.md)

## See Also

- [init(items: [any CPListTemplateItem], header: String, headerSubtitle: String?, headerImage: UIImage?, headerButton: CPButton?, sectionIndexTitle: String?)](cplistsection/init(items:header:headersubtitle:headerimage:headerbutton:sectionindextitle:).md)
  Creates a section with list items, a header, a section index title, and section header details.
- [protocol CPSelectableListItem](cpselectablelistitem.md)
  A description of a selectable list item.
- [class CPListItem](cplistitem.md)
  A selectable row in a list template.
- [class CPListImageRowItem](cplistimagerowitem.md)
  A list template row that displays a series of images.
- [class CPMessageListItem](cpmessagelistitem.md)
  A list template row that represents a conversation or contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplateitem)*