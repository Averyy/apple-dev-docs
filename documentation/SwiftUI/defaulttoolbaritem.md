# DefaultToolbarItem

**Framework**: SwiftUI  
**Kind**: struct

A toolbar item that represents a system component.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
struct DefaultToolbarItem
```

#### Overview

Place this item in your toolbar to control where the system-provided item, like search, will be positioned.

## Topics

### Initializers
- [init(kind: ToolbarDefaultItemKind, placement: ToolbarItemPlacement)](defaulttoolbaritem/init(kind:placement:).md)
  Creates a system-defined toolbar item from a `ToolbarDefaultItemKind` at the given `placement`.

## Relationships

### Conforms To
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
- [struct ToolbarSpacer](toolbarspacer.md)
  A standard space item in toolbars.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/defaulttoolbaritem)*