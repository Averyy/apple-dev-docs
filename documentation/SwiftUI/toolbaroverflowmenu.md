# ToolbarOverflowMenu

**Framework**: SwiftUI  
**Kind**: struct

The overflow menu of a toolbar.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
struct ToolbarOverflowMenu<Content> where Content : View
```

#### Overview

An overflow menu represents actions that are always placed in the toolbar’s overflow menu, regardless of the toolbar mode, platform, or customizability.

```swift
ContentView()
    .toolbar {
        ToolbarOverflowMenu {
            Button("Action 1") { }
            Button("Action 2") { }
        }
    }
```

In iOS and visionOS, this content is placed into the overflow menu in the navigation bar.

## Topics

### Creating a toolbar overflow menu
- [init(content: () -> Content)](toolbaroverflowmenu/init(content:).md)
  Creates toolbar overflow menu content.

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
- [func toolbarOverflowMenu<C>(content: () -> C) -> some View](view/toolbaroverflowmenu(content:).md)
  Configures the overflow menu of a toolbar.
- [protocol ToolbarContent](toolbarcontent.md)
  Conforming types represent items that can be placed in various locations in a toolbar.
- [struct ToolbarContentBuilder](toolbarcontentbuilder.md)
  Constructs a toolbar item set from multi-expression closures.
- [struct ToolbarSpacer](toolbarspacer.md)
  A standard space item in toolbars.
- [struct DefaultToolbarItem](defaulttoolbaritem.md)
  A toolbar item that represents a system component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbaroverflowmenu)*