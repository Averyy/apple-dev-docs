# ToolbarItemGroup

**Framework**: SwiftUI  
**Kind**: struct

A model that represents a group of `ToolbarItem`s which can be placed in the toolbar or navigation bar.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
struct ToolbarItemGroup<Content> where Content : View
```

## Topics

### Creating a toolbar item group
- [init(placement: ToolbarItemPlacement, content: () -> Content)](toolbaritemgroup/init(placement:content:).md)
  Creates a toolbar item group with a specified placement and content.
- [init<C, L>(placement: ToolbarItemPlacement, content: () -> C, label: () -> L)](toolbaritemgroup/init(placement:content:label:).md)
  Creates a toolbar item group with the specified placement, content, and a label describing that content.
### Supporting types
- [struct LabeledToolbarItemGroupContent](labeledtoolbaritemgroupcontent.md)
  A view that represents the view of a toolbar item group with a specified label.

## Relationships

### Conforms To
- [ToolbarContent](toolbarcontent.md)

## See Also

- [func toolbar(content:)](view/toolbar(content:).md)
  Populates the toolbar or navigation bar with the specified items.
- [struct ToolbarItem](toolbaritem.md)
  A model that represents an item which can be placed in the toolbar or navigation bar.
- [struct ToolbarItemPlacement](toolbaritemplacement.md)
  A structure that defines the placement of a toolbar item.
- [protocol ToolbarContent](toolbarcontent.md)
  Conforming types represent items that can be placed in various locations in a toolbar.
- [struct ToolbarContentBuilder](toolbarcontentbuilder.md)
  Constructs a toolbar item set from multi-expression closures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbaritemgroup)*