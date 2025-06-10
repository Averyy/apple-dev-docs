# UIMenuSystem

**Framework**: UIKit  
**Kind**: class

An object representing a main or contextual menu system.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIMenuSystem
```

#### Overview

A menu system groups root menus together. The [`main`](uimenusystem/main.md) system has only one root menu while the [`context`](uimenusystem/context.md) system can have multiple root menus, each built in different [`UIResponder`](uiresponder.md) objects like a view controller.

Use [`UIMenuSystem`](uimenusystem.md) in your implementation of [`buildMenu(with:)`](uiresponder/buildmenu(with:).md) to isolate changes to a specific system.

```swift
override func buildMenu(with builder: UIMenuBuilder) {
    super.buildMenu(with: builder)
    
    // Ensure that the builder is modifying the menu bar system.
    guard builder.system == UIMenuSystem.main else { return }

    // ...
}
```

You can also use a menu system to rebuild or revalidate menus as changes occur in your app. To rebuild a menu, call the [`setNeedsRebuild()`](uimenusystem/setneedsrebuild().md) method. Call [`setNeedsRevalidate()`](uimenusystem/setneedsrevalidate().md) when you need the menu system to revalidate a menu.

For more information, see [`Adding menus and shortcuts to the menu bar and user interface`](adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md).

## Topics

### Getting a menu system
- [class var main: UIMenuSystem](uimenusystem/main.md)
  The main menu system.
- [class var context: UIMenuSystem](uimenusystem/context.md)
  The context menu system.
### Rebuilding a menu system
- [func setNeedsRebuild()](uimenusystem/setneedsrebuild.md)
  Tells the menu system to rebuild all of its menus.
### Revalidating a menu system
- [func setNeedsRevalidate()](uimenusystem/setneedsrevalidate.md)
  Tells the menu system to validate all of its menus.
### Setting group preferences
- [UIMenuSystem.ElementGroupPreference](uimenusystem/elementgrouppreference.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [UIContextMenuSystem](uicontextmenusystem.md)
- [UIMainMenuSystem](uimainmenusystem.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class UIMenu](uimenu.md)
  A container for grouping related menu elements in an app menu or contextual menu.
- [protocol UIMenuBuilder](uimenubuilder.md)
  An interface for adding and removing menus from a menu system.
- [class UIMainMenuSystem](uimainmenusystem.md)
  The main menu system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenusystem)*