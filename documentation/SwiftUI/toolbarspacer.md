# ToolbarSpacer

**Framework**: SwiftUI  
**Kind**: struct

A standard space item in toolbars.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
struct ToolbarSpacer
```

#### Overview

A space item creates visual breaks in the toolbar between items. Spacers can have a standard fixed size or be flexible and push items apart.

Spacers can also be used in customizable toolbars:

```swift
ContentView()
    .toolbar(id: "main-toolbar") {
        ToolbarItem(id: "tag") {
           TagButton()
        }
        ToolbarItem(id: "share") {
           ShareButton()
        }
        ToolbarSpacer(.fixed)
        ToolbarItem(id: "more") {
           MoreButton()
        }
    }
```

Space items are customizable and can be added, removed, and rearranged by users. If a customizable toolbar supports a spacer of a given type, users can also add in multiple copies of that spacer from the customization panel.

## Topics

### Initializers
- [init(SpacerSizing, placement: ToolbarItemPlacement)](toolbarspacer/init(_:placement:).md)
  Creates a toolbar spacer item with the specified sizing behavior and placement.

## Relationships

### Conforms To
- [CustomizableToolbarContent](customizabletoolbarcontent.md)
- [ToolbarContent](toolbarcontent.md)

## See Also

- [func toolbar(content:)](view/toolbar(content:).md)
  Populates the toolbar or navigation bar with the specified items.
- [struct ToolbarItem](toolbaritem.md)
  A model that represents an item which can be placed in the toolbar or navigation bar.
- [struct ToolbarItemGroup](toolbaritemgroup.md)
  A model that represents a group of `ToolbarItem`s which can be placed in the toolbar or navigation bar.
- [struct ToolbarItemPlacement](toolbaritemplacement.md)
  A structure that defines the placement of a toolbar item.
- [protocol ToolbarContent](toolbarcontent.md)
  Conforming types represent items that can be placed in various locations in a toolbar.
- [struct ToolbarContentBuilder](toolbarcontentbuilder.md)
  Constructs a toolbar item set from multi-expression closures.
- [struct DefaultToolbarItem](defaulttoolbaritem.md)
  A toolbar item that represents a system component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbarspacer)*