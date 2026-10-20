# NSToolbar

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

An object that manages the space above your app’s custom content and either below or integrated with the window’s title bar.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS

## Declaration

```swift
@MainActor
class NSToolbar
```

```objc
@interface NSToolbar : NSObject
```

#### Overview

An [`NSToolbar`](./nstoolbar.md) object manages the controls and views that apply to the main window’s content area. Toolbars provide convenient access to the commands and features people use most often. Toolbars are also user-configurable and support the display of an interactive customization palette.

Create and configure your toolbar programmatically or using Interface Builder. Add items to the toolbar that correspond to the commands you want to feature in your window. Each item has a corresponding [`NSToolbarItem`](./nstoolbaritem.md) object, which you use to make changes. Each toolbar manages a unique set of items, but you can synchronize the items and state of multiple toolbars by assigning the same value to their [`identifier`](./nstoolbar/identifier-swift.property.md) properties.

For more information about how to use toolbars, see [Integrating a Toolbar and Touch Bar into Your App](./integrating-a-toolbar-and-touch-bar-into-your-app.md).

## Topics

### Creating an toolbar object
- [init(identifier: NSToolbar.Identifier)](./nstoolbar/init%28identifier%29.md)
  Creates a newly allocated toolbar with the specified identifier.
- [convenience init()](./nstoolbar/init%28%29.md)
  Creates a new toolbar with an empty identifier string.
### Configuring the toolbar contents
- [var delegate: (any NSToolbarDelegate)?](./nstoolbar/delegate.md)
  The object you use to customize the toolbar contents and configuration.
- [protocol NSToolbarDelegate](./nstoolbardelegate.md)
  A set of optional methods you use to configure the toolbar and respond to changes.
### Getting the toolbar’s identity
- [var identifier: NSToolbar.Identifier](./nstoolbar/identifier-swift.property.md)
  The value you use to identify the toolbar in your app.
- [NSToolbar.Identifier](./nstoolbar/identifier-swift.typealias.md)
  A string value that you use to differentiate your app’s toolbars.
### Configuring the toolbar’s behavior
- [var isVisible: Bool](./nstoolbar/isvisible.md)
  A Boolean value that indicates whether the toolbar is visible.
- [var displayMode: NSToolbar.DisplayMode](./nstoolbar/displaymode-swift.property.md)
  A value that indicates whether the toolbar displays items using a name, icon, or combination of elements.
- [NSToolbar.DisplayMode](./nstoolbar/displaymode-swift.enum.md)
  Constants that indicate whether the toolbar displays items using a name, icon, or combination of elements.
- [var allowsUserCustomization: Bool](./nstoolbar/allowsusercustomization.md)
  A Boolean value that indicates whether users can modify the contents of the toolbar.
- [var allowsExtensionItems: Bool](./nstoolbar/allowsextensionitems.md)
  A Boolean value that indicates whether the toolbar can add items for Action extensions.
### Managing items on the toolbar
- [var items: [NSToolbarItem]](./nstoolbar/items.md)
  An array containing the toolbar’s current items, in order.
- [var visibleItems: [NSToolbarItem]?](./nstoolbar/visibleitems.md)
  An array containing the toolbar’s currently visible items.
- [var centeredItemIdentifiers: Set<NSToolbarItem.Identifier>](./nstoolbar/centereditemidentifiers.md)
  The set of custom items to display in the center of the toolbar.
- [var selectedItemIdentifier: NSToolbarItem.Identifier?](./nstoolbar/selecteditemidentifier.md)
  The identifier of the toolbar’s currently selected item.
- [class let willAddItemNotification: NSNotification.Name](./nstoolbar/willadditemnotification.md)
  Posts before the toolbar adds a new item.
- [class let didRemoveItemNotification: NSNotification.Name](./nstoolbar/didremoveitemnotification.md)
  Posted after an item is removed from a toolbar.
- [func insertItem(withItemIdentifier: NSToolbarItem.Identifier, at: Int)](./nstoolbar/insertitem%28withitemidentifier,at%29.md)
  Inserts an item into the toolbar at the specified index.
- [func removeItem(at: Int)](./nstoolbar/removeitem%28at%29.md)
  Removes the item at the specified index in the toolbar.
### Autosaving the configuration
- [var autosavesConfiguration: Bool](./nstoolbar/autosavesconfiguration.md)
  A Boolean value that indicates whether the toolbar autosaves its configuration.
### Displaying the customization palette
- [func runCustomizationPalette(Any?)](./nstoolbar/runcustomizationpalette%28_%29.md)
  Displays the toolbar’s customization palette and handles any user-initiated customizations.
- [var customizationPaletteIsRunning: Bool](./nstoolbar/customizationpaletteisrunning.md)
  A Boolean value that indicates whether the toolbar’s customization palette is in use.
### Validating visible items
- [func validateVisibleItems()](./nstoolbar/validatevisibleitems%28%29.md)
  Validates the toolbar’s visible items during a window update.
### Deprecated
- [Deprecated symbols](./nstoolbar-deprecated-symbols.md)
  Review symbols that are no longer in active development, and their recommended replacements.
### Structures
- [NSToolbar.DidRemoveItemMessage](./nstoolbar/didremoveitemmessage.md)
- [NSToolbar.WillAddItemMessage](./nstoolbar/willadditemmessage.md)
### Instance Properties
- [var allowsDisplayModeCustomization: Bool](./nstoolbar/allowsdisplaymodecustomization.md)
  Whether or not the user is allowed to change display modes at run time. This functionality is independent of customizing the order of the items themselves. Only disable when the functionality or legibility of your toolbar could not be improved by another display mode. The user’s selection will be persisted using the toolbar’s `identifier` when `autosavesConfiguration` is enabled. The default is YES for apps linked on macOS 15.0 and above.
- [var itemIdentifiers: [NSToolbarItem.Identifier]](./nstoolbar/itemidentifiers.md)
  An array of itemIdentifiers that represent the current items in the toolbar. Setting this property will set the current items in the toolbar by diffing against items that already exist. Use this with great caution if `allowsUserCustomization` is enabled as it will override any customizations the user has made. This property is key value observable.
### Instance Methods
- [func removeItem(identifier: NSToolbarItem.Identifier)](./nstoolbar/removeitem%28identifier%29.md)
  Removes the item with matching `itemIdentifier` in the receiving toolbar. If multiple items share the same identifier (as is the case with space items) all matching items will be removed. To remove only a single space item, use `-removeItemAtIndex:` instead.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)

## See Also

### View
- [Integrating a Toolbar and Touch Bar into Your App](./integrating-a-toolbar-and-touch-bar-into-your-app.md)
  Provide users quick access to your app’s features from a toolbar and corresponding Touch Bar.
- [protocol NSToolbarItemValidation](./nstoolbaritemvalidation.md)
  Validation of a toolbar item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbar)*