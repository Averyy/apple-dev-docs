# toolbarOverflowMenu(content:)

**Framework**: SwiftUI  
**Kind**: method

Configures the overflow menu of a toolbar.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
func toolbarOverflowMenu<C>(@ContentBuilder content: () -> C) -> some View where C : View
```

#### Discussion

An overflow menu represents actions that are always placed in the toolbar’s overflow menu, regardless of the toolbar mode, platform, or customizability.

```swift
ContentView()
    .toolbarOverflowMenu {
        Button("Action 1") { }
        Button("Action 2") { }
    }
```

In iOS and visionOS, this content is placed into the overflow menu in the navigation bar.

## Parameters

- `content`: The content of the overflow menu.

## See Also

- [func toolbar(content:)](view/toolbar(content:).md)
  Populates the toolbar or navigation bar with the specified items.
- [struct ToolbarItem](toolbaritem.md)
  A model that represents an item which can be placed in the toolbar or navigation bar.
- [struct ToolbarItemGroup](toolbaritemgroup.md)
  A model that represents a group of `ToolbarItem`s which can be placed in the toolbar or navigation bar.
- [struct ToolbarItemPlacement](toolbaritemplacement.md)
  A structure that defines the placement of a toolbar item.
- [struct ToolbarOverflowMenu](toolbaroverflowmenu.md)
  The overflow menu of a toolbar.
- [protocol ToolbarContent](toolbarcontent.md)
  Conforming types represent items that can be placed in various locations in a toolbar.
- [struct ToolbarContentBuilder](toolbarcontentbuilder.md)
  Constructs a toolbar item set from multi-expression closures.
- [struct ToolbarSpacer](toolbarspacer.md)
  A standard space item in toolbars.
- [struct DefaultToolbarItem](defaulttoolbaritem.md)
  A toolbar item that represents a system component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/toolbaroverflowmenu(content:))*