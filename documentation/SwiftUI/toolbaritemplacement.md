# ToolbarItemPlacement

**Framework**: SwiftUI  
**Kind**: struct

A structure that defines the placement of a toolbar item.

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
struct ToolbarItemPlacement
```

#### Overview

There are two types of placements:

- Semantic placements, such as [`principal`](toolbaritemplacement/principal.md) and [`navigation`](toolbaritemplacement/navigation.md), denote the intent of the item being added. SwiftUI determines the appropriate placement for the item based on this intent and its surrounding context, like the current platform.
- Positional placements, such as [`navigationBarLeading`](toolbaritemplacement/navigationbarleading.md), denote a precise placement for the item, usually for a particular platform.

In iOS, iPadOS, and macOS, the system uses the space available to the toolbar when determining how many items to render in the toolbar. If not all items fit in the available space, an overflow menu may be created and remaining items placed in that menu.

## Topics

### Getting semantic placement
- [static let automatic: ToolbarItemPlacement](toolbaritemplacement/automatic.md)
  The system places the item automatically, depending on many factors including the platform, size class, or presence of other items.
- [static let principal: ToolbarItemPlacement](toolbaritemplacement/principal.md)
  The system places the item in the principal item section.
- [static let status: ToolbarItemPlacement](toolbaritemplacement/status.md)
  The item represents a change in status for the current context.
### Getting placement for specific actions
- [static let primaryAction: ToolbarItemPlacement](toolbaritemplacement/primaryaction.md)
  The item represents a primary action.
- [static let secondaryAction: ToolbarItemPlacement](toolbaritemplacement/secondaryaction.md)
  The item represents a secondary action.
- [static let confirmationAction: ToolbarItemPlacement](toolbaritemplacement/confirmationaction.md)
  The item represents a confirmation action for a modal interface.
- [static let cancellationAction: ToolbarItemPlacement](toolbaritemplacement/cancellationaction.md)
  The item represents a cancellation action for a modal interface.
- [static let destructiveAction: ToolbarItemPlacement](toolbaritemplacement/destructiveaction.md)
  The item represents a destructive action for a modal interface.
- [static let navigation: ToolbarItemPlacement](toolbaritemplacement/navigation.md)
  The item represents a navigation action.
### Getting explicit placement
- [static var topBarLeading: ToolbarItemPlacement](toolbaritemplacement/topbarleading.md)
  Places the item in the leading edge of the top bar.
- [static var topBarTrailing: ToolbarItemPlacement](toolbaritemplacement/topbartrailing.md)
  Places the item in the trailing edge of the top bar.
- [static let bottomBar: ToolbarItemPlacement](toolbaritemplacement/bottombar.md)
  Places the item in the bottom toolbar.
- [static let bottomOrnament: ToolbarItemPlacement](toolbaritemplacement/bottomornament.md)
  Places the item in an ornament under the window.
- [static let keyboard: ToolbarItemPlacement](toolbaritemplacement/keyboard.md)
  The item is placed in the keyboard section.
- [static func accessoryBar<ID>(id: ID) -> ToolbarItemPlacement](toolbaritemplacement/accessorybar(id:).md)
  Creates a unique accessory bar placement.
### Deprecated symbols
- [init<ID>(id: ID)](toolbaritemplacement/init(id:).md)
  Creates a custom accessory bar item placement.
- [static let navigationBarLeading: ToolbarItemPlacement](toolbaritemplacement/navigationbarleading.md)
  Places the item in the leading edge of the navigation bar.
- [static let navigationBarTrailing: ToolbarItemPlacement](toolbaritemplacement/navigationbartrailing.md)
  Places the item in the trailing edge of the navigation bar.

## See Also

- [func toolbar(content:)](view/toolbar(content:).md)
  Populates the toolbar or navigation bar with the specified items.
- [struct ToolbarItem](toolbaritem.md)
  A model that represents an item which can be placed in the toolbar or navigation bar.
- [struct ToolbarItemGroup](toolbaritemgroup.md)
  A model that represents a group of `ToolbarItem`s which can be placed in the toolbar or navigation bar.
- [protocol ToolbarContent](toolbarcontent.md)
  Conforming types represent items that can be placed in various locations in a toolbar.
- [struct ToolbarContentBuilder](toolbarcontentbuilder.md)
  Constructs a toolbar item set from multi-expression closures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbaritemplacement)*