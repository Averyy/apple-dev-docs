# init(items:header:headerSubtitle:headerImage:headerButton:sectionIndexTitle:)

**Framework**: CarPlay  
**Kind**: init

Creates a section with list items, a header, a section index title, and section header details.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
init(items: [any CPListTemplateItem], header: String, headerSubtitle: String?, headerImage: UIImage?, headerButton: CPButton?, sectionIndexTitle: String?)
```

#### Return Value

A newly initialized list section.

## Parameters

- `items`: A list of items to include in the section.
- `header`: The section header text.
- `sectionIndexTitle`: A section index title. The system displays only the first character of the title, so choose a single-character section index title.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistsection/init(items:header:headersubtitle:headerimage:headerbutton:sectionindextitle:))*