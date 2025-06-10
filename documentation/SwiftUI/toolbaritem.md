# ToolbarItem

**Framework**: SwiftUI  
**Kind**: struct

A model that represents an item which can be placed in the toolbar or navigation bar.

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
struct ToolbarItem<ID, Content> where Content : View
```

## Topics

### Creating a toolbar item
- [init(placement: ToolbarItemPlacement, content: () -> Content)](toolbaritem/init(placement:content:).md)
  Creates a toolbar item with the specified placement and content.
- [init(id: String, placement: ToolbarItemPlacement, content: () -> Content)](toolbaritem/init(id:placement:content:).md)
  Creates a toolbar item with the specified placement and content, which allows for user customization.
- [init(id: String, placement: ToolbarItemPlacement, showsByDefault: Bool, content: () -> Content)](toolbaritem/init(id:placement:showsbydefault:content:).md)
  Creates a toolbar item with the specified placement and content, which allows for user customization.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomizableToolbarContent](customizabletoolbarcontent.md)
- [Identifiable](../Swift/Identifiable.md)
- [ToolbarContent](toolbarcontent.md)

## See Also

- [func toolbar(content:)](view/toolbar(content:).md)
  Populates the toolbar or navigation bar with the specified items.
- [struct ToolbarItemGroup](toolbaritemgroup.md)
  A model that represents a group of `ToolbarItem`s which can be placed in the toolbar or navigation bar.
- [struct ToolbarItemPlacement](toolbaritemplacement.md)
  A structure that defines the placement of a toolbar item.
- [protocol ToolbarContent](toolbarcontent.md)
  Conforming types represent items that can be placed in various locations in a toolbar.
- [struct ToolbarContentBuilder](toolbarcontentbuilder.md)
  Constructs a toolbar item set from multi-expression closures.
- [struct ToolbarSpacer](toolbarspacer.md)
  A standard space item in toolbars.
- [struct DefaultToolbarItem](defaulttoolbaritem.md)
  A toolbar item that represents a system component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbaritem)*