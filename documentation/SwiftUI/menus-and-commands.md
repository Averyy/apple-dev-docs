# Menus and commands

**Framework**: SwiftUI

Provide space-efficient, context-dependent access to commands and controls.

#### Overview

Use a menu to provide people with easy access to common commands. You can add items to a macOS app’s menu bar using the [`commands(content:)`](scene/commands(content:).md) scene modifier, or create context menus that people reveal near their current task using the [`contextMenu(menuItems:)`](view/contextmenu(menuitems:).md) view modifier.

![None](https://docs-assets.developer.apple.com/published/dfe1ae858d3f19de19a190f122aaf44a/menus-and-commands-hero%402x.png)

Create submenus by nesting [`Menu`](menu.md) instances inside others. Use a [`Divider`](divider.md) view to create a separator between menu elements.

For design guidance, see [`Menus`](https://developer.apple.com/design/Human-Interface-Guidelines/menus) in the Human Interface Guidelines.

## Topics

### Creating a menu
- [struct Menu](menu.md)
  A control for presenting a menu of actions.
- [func menuStyle<S>(S) -> some View](view/menustyle(_:).md)
  Sets the style for menus within this view.
### Creating context menus
- [func contextMenu<MenuItems>(menuItems: () -> MenuItems) -> some View](view/contextmenu(menuitems:).md)
  Adds a context menu to a view.
- [func contextMenu<M, P>(menuItems: () -> M, preview: () -> P) -> some View](view/contextmenu(menuitems:preview:).md)
  Adds a context menu with a custom preview to a view.
- [func contextMenu<I, M>(forSelectionType: I.Type, menu: (Set<I>) -> M, primaryAction: ((Set<I>) -> Void)?) -> some View](view/contextmenu(forselectiontype:menu:primaryaction:).md)
  Adds an item-based context menu to a view.
### Defining commands
- [func commands<Content>(content: () -> Content) -> some Scene](scene/commands(content:).md)
  Adds commands to the scene.
- [func commandsRemoved() -> some Scene](scene/commandsremoved.md)
  Removes all commands defined by the modified scene.
- [func commandsReplaced<Content>(content: () -> Content) -> some Scene](scene/commandsreplaced(content:).md)
  Replaces all commands defined by the modified scene with the commands from the builder.
- [protocol Commands](commands.md)
  Conforming types represent a group of related commands that can be exposed to the user via the main menu on macOS and key commands on iOS.
- [struct CommandMenu](commandmenu.md)
  Command menus are stand-alone, top-level containers for controls that perform related, app-specific commands.
- [struct CommandGroup](commandgroup.md)
  Groups of controls that you can add to existing command menus.
- [struct CommandsBuilder](commandsbuilder.md)
  Constructs command sets from multi-expression closures. Like `ViewBuilder`, it supports up to ten expressions in the closure body.
- [struct CommandGroupPlacement](commandgroupplacement.md)
  The standard locations that you can place new command groups relative to.
### Getting built-in command groups
- [struct SidebarCommands](sidebarcommands.md)
  A built-in set of commands for manipulating window sidebars.
- [struct TextEditingCommands](texteditingcommands.md)
  A built-in group of commands for searching, editing, and transforming selections of text.
- [struct TextFormattingCommands](textformattingcommands.md)
  A built-in set of commands for transforming the styles applied to selections of text.
- [struct ToolbarCommands](toolbarcommands.md)
  A built-in set of commands for manipulating window toolbars.
- [struct ImportFromDevicesCommands](importfromdevicescommands.md)
  A built-in set of commands that enables importing content from nearby devices.
- [struct InspectorCommands](inspectorcommands.md)
  A built-in set of commands for manipulating inspectors.
- [struct EmptyCommands](emptycommands.md)
  An empty group of commands.
### Showing a menu indicator
- [func menuIndicator(Visibility) -> some View](view/menuindicator(_:).md)
  Sets the menu indicator visibility for controls within this view.
- [var menuIndicatorVisibility: Visibility](environmentvalues/menuindicatorvisibility.md)
  The menu indicator visibility to apply to controls within a view.
### Configuring menu dismissal
- [func menuActionDismissBehavior(MenuActionDismissBehavior) -> some View](view/menuactiondismissbehavior(_:).md)
  Tells a menu whether to dismiss after performing an action.
- [struct MenuActionDismissBehavior](menuactiondismissbehavior.md)
  The set of menu dismissal behavior options.
### Setting a preferred order
- [func menuOrder(MenuOrder) -> some View](view/menuorder(_:).md)
  Sets the preferred order of items for menus presented from this view.
- [var menuOrder: MenuOrder](environmentvalues/menuorder.md)
  The preferred order of items for menus presented from this view.
- [struct MenuOrder](menuorder.md)
  The order in which a menu presents its content.
### Deprecated types
- [struct MenuButton](menubutton.md)
  A button that displays a menu containing a list of choices when pressed.
- [typealias PullDownButton](pulldownbutton.md)
- [struct ContextMenu](contextmenu.md)
  A container for views that you present as menu items in a context menu.

## See Also

- [View fundamentals](view-fundamentals.md)
  Define the visual elements of your app using a hierarchy of views.
- [View configuration](view-configuration.md)
  Adjust the characteristics of views in a hierarchy.
- [View styles](view-styles.md)
  Apply built-in and custom appearances and behaviors to different types of views.
- [Animations](animations.md)
  Create smooth visual updates in response to state changes.
- [Text input and output](text-input-and-output.md)
  Display formatted text and get text input from the user.
- [Images](images.md)
  Add images and symbols to your app’s user interface.
- [Controls and indicators](controls-and-indicators.md)
  Display values and get user selections.
- [Shapes](shapes.md)
  Trace and fill built-in and custom shapes with a color, gradient, or other pattern.
- [Drawing and graphics](drawing-and-graphics.md)
  Enhance your views with graphical effects and customized drawings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/menus-and-commands)*