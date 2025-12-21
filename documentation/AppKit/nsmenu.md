# NSMenu

**Framework**: AppKit  
**Kind**: class

An object that manages an app’s menus.

**Availability**:
- macOS ?+

## Declaration

```swift
class NSMenu
```

## Topics

### Managing the Menu Bar
- [class func menuBarVisible() -> Bool](nsmenu/menubarvisible.md)
  Returns a Boolean value that indicates whether the menu bar is visible.
- [class func setMenuBarVisible(Bool)](nsmenu/setmenubarvisible(_:).md)
  Sets whether the menu bar is visible and selectable by the user.
- [var menuBarHeight: CGFloat](nsmenu/menubarheight.md)
  The menu bar height for the main menu in pixels.
### Creating an NSMenu Object
- [init(title: String)](nsmenu/init(title:).md)
  Initializes and returns a menu having the specified title and with autoenabling of menu items turned on.
- [init(coder: NSCoder)](nsmenu/init(coder:).md)
### Adding and Removing Menu Items
- [func insertItem(NSMenuItem, at: Int)](nsmenu/insertitem(_:at:).md)
  Inserts a menu item into the menu at a specific location.
- [func insertItem(withTitle: String, action: Selector?, keyEquivalent: String, at: Int) -> NSMenuItem](nsmenu/insertitem(withtitle:action:keyequivalent:at:).md)
  Creates and adds a menu item at a specified location in the menu.
- [func addItem(NSMenuItem)](nsmenu/additem(_:).md)
  Adds a menu item to the end of the menu.
- [func addItem(withTitle: String, action: Selector?, keyEquivalent: String) -> NSMenuItem](nsmenu/additem(withtitle:action:keyequivalent:).md)
  Creates a new menu item and adds it to the end of the menu.
- [func removeItem(NSMenuItem)](nsmenu/removeitem(_:).md)
  Removes a menu item from the menu.
- [func removeItem(at: Int)](nsmenu/removeitem(at:).md)
  Removes the menu item at a specified location in the menu.
- [func itemChanged(NSMenuItem)](nsmenu/itemchanged(_:).md)
  Invoked when a menu item is modified visually (for example, its title changes).
- [func removeAllItems()](nsmenu/removeallitems.md)
  Removes all the menu items in the menu.
### Finding Menu Items
- [func item(withTag: Int) -> NSMenuItem?](nsmenu/item(withtag:).md)
  Returns the first menu item in the menu with the specified tag.
- [func item(withTitle: String) -> NSMenuItem?](nsmenu/item(withtitle:).md)
  Returns the first menu item in the menu with a specified title.
- [func item(at: Int) -> NSMenuItem?](nsmenu/item(at:).md)
  Returns the menu item at a specific location of the menu.
- [var numberOfItems: Int](nsmenu/numberofitems.md)
  The number of menu items in the menu, including separator items.
- [var items: [NSMenuItem]](nsmenu/items.md)
  An array containing the menu items in the menu.
### Finding Indices of Menu Items
- [func index(of: NSMenuItem) -> Int](nsmenu/index(of:).md)
  Returns the index identifying the location of a specified menu item in the menu.
- [func indexOfItem(withTitle: String) -> Int](nsmenu/indexofitem(withtitle:).md)
  Returns the index of the first menu item in the menu that has a specified title.
- [func indexOfItem(withTag: Int) -> Int](nsmenu/indexofitem(withtag:).md)
  Returns the index of the first menu item in the menu identified by a tag.
- [func indexOfItem(withTarget: Any?, andAction: Selector?) -> Int](nsmenu/indexofitem(withtarget:andaction:).md)
  Returns the index of the first menu item in the menu that has a specified action and target.
- [func indexOfItem(withRepresentedObject: Any?) -> Int](nsmenu/indexofitem(withrepresentedobject:).md)
  Returns the index of the first menu item in the menu that has a given represented object.
- [func indexOfItem(withSubmenu: NSMenu?) -> Int](nsmenu/indexofitem(withsubmenu:).md)
  Returns the index of the menu item in the menu with the given submenu.
### Managing Submenus
- [func setSubmenu(NSMenu?, for: NSMenuItem)](nsmenu/setsubmenu(_:for:).md)
  Assigns a menu to be a submenu of the menu controlled by a given menu item.
- [func submenuAction(Any?)](nsmenu/submenuaction(_:).md)
  The action method assigned to menu items that open submenus.
- [var supermenu: NSMenu?](nsmenu/supermenu.md)
  The parent menu that contains the menu as a submenu.
- [var isTornOff: Bool](nsmenu/istornoff.md)
  Indicates whether the menu is offscreen or attached to another menu (or if it’s the main menu).
### Enabling and Disabling Menu Items
- [var autoenablesItems: Bool](nsmenu/autoenablesitems.md)
  Indicates whether the menu automatically enables and disables its menu items.
- [func update()](nsmenu/update.md)
  Enables or disables the menu items of the menu based on the NSMenuValidation informal protocol and sizes the menu to fit its current menu items if necessary.
### Getting and Setting the Menu Font
- [var font: NSFont!](nsmenu/font.md)
  The font of the menu and its submenus.
### Handling Keyboard Equivalents
- [func performKeyEquivalent(with: NSEvent) -> Bool](nsmenu/performkeyequivalent(with:).md)
  Performs the action for the menu item that corresponds to the given key equivalent.
### Simulating Mouse Clicks
- [func performActionForItem(at: Int)](nsmenu/performactionforitem(at:).md)
  Causes the application to send the action message of a specified menu item to its target.
### Managing the Title
- [var title: String](nsmenu/title.md)
  The title of the menu.
### Selecting Items
- [var selectedItems: [NSMenuItem]](nsmenu/selecteditems.md)
  The menu items that are currently selected.
- [var selectionMode: NSMenu.SelectionMode](nsmenu/selectionmode-swift.property.md)
  The selection mode of the menu.
- [NSMenu.SelectionMode](nsmenu/selectionmode-swift.enum.md)
  Describes how the menu manages selection states of the menu items that belong to the same selection group.
### Configuring Menu Size
- [var minimumWidth: CGFloat](nsmenu/minimumwidth.md)
  The minimum width of the menu in screen coordinates.
- [var size: NSSize](nsmenu/size.md)
  The size of the menu in screen coordinates
### Getting Menu Properties
- [var propertiesToUpdate: NSMenu.Properties](nsmenu/propertiestoupdate.md)
  The available properties for the menu.
### Managing Presentation Styles
- [var presentationStyle: NSMenu.PresentationStyle](nsmenu/presentationstyle-swift.property.md)
  The presentation style of the menu.
- [NSMenu.PresentationStyle](nsmenu/presentationstyle-swift.enum.md)
  Specifies the style of a menu.
### Working with Palettes
- [static func palette(colors: [NSColor], titles: [String], template: NSImage?, onSelectionChange: ((NSMenu) -> Void)?) -> NSMenu](nsmenu/palette(colors:titles:template:onselectionchange:).md)
  Creates a palette style menu displaying user-selectable color tags that tint using the specified array of colors.
### Managing Menu Change Notifications
- [var menuChangedMessagesEnabled: Bool](nsmenu/menuchangedmessagesenabled.md)
  Indicates whether messages are sent to the application’s windows each time the menu changes.
### Displaying Contextual Menus
- [var allowsContextMenuPlugIns: Bool](nsmenu/allowscontextmenuplugins.md)
  Indicates whether the pop-up menu allows appending of contextual menu plug-in items.
### Displaying Context-Sensitive Help
- [class func popUpContextMenu(NSMenu, with: NSEvent, for: NSView)](nsmenu/popupcontextmenu(_:with:for:).md)
  Displays a contextual menu over a view for an event.
- [class func popUpContextMenu(NSMenu, with: NSEvent, for: NSView, with: NSFont?)](nsmenu/popupcontextmenu(_:with:for:with:).md)
  Displays a contextual menu over a view for an event using a specified font.
- [func helpRequested(with: NSEvent)](nsmenu/helprequested(with:).md)
  Overridden by subclasses to implement specialized context-sensitive help behavior.
- [func popUp(positioning: NSMenuItem?, at: NSPoint, in: NSView?) -> Bool](nsmenu/popup(positioning:at:in:).md)
  Pops up the menu at the specified location.
### Managing Display of the State Column
- [var showsStateColumn: Bool](nsmenu/showsstatecolumn.md)
  Indicates whether the menu displays the state column.
### Controlling Allocation Zones
- [class func menuZone() -> NSZone!](nsmenu/menuzone.md)
  Returns the zone from which `NSMenu` objects should be allocated.
### Handling Highlighting
- [var highlightedItem: NSMenuItem?](nsmenu/highlighteditem.md)
  Indicates the currently highlighted item in the menu.
### Managing the User Interface
- [var userInterfaceLayoutDirection: NSUserInterfaceLayoutDirection](nsmenu/userinterfacelayoutdirection.md)
  Configures the layout direction of menu items in the menu.
### Managing the Delegate
- [var delegate: (any NSMenuDelegate)?](nsmenu/delegate.md)
  The delegate of the menu.
### Handling Tracking
- [func cancelTracking()](nsmenu/canceltracking.md)
  Dismisses the menu and ends all menu tracking.
- [func cancelTrackingWithoutAnimation()](nsmenu/canceltrackingwithoutanimation.md)
  Dismisses the menu and ends all menu tracking without displaying the associated animation.
### Constants
- [NSMenu.Properties](nsmenu/properties.md)
  These constants are used as a bitmask for specifying a set of menu or menu item properties, and are contained by the [`propertiesToUpdate`](nsmenu/propertiestoupdate.md) property.
### Notifications
- [class let didAddItemNotification: NSNotification.Name](nsmenu/didadditemnotification.md)
  Posted after a menu item is added to the menu.
- [class let didChangeItemNotification: NSNotification.Name](nsmenu/didchangeitemnotification.md)
  Posted after a menu item in the menu changes appearance.
- [class let didBeginTrackingNotification: NSNotification.Name](nsmenu/didbegintrackingnotification.md)
  Posted when menu tracking begins.
- [class let didEndTrackingNotification: NSNotification.Name](nsmenu/didendtrackingnotification.md)
  Posted when menu tracking ends, even if no action is sent.
- [class let didRemoveItemNotification: NSNotification.Name](nsmenu/didremoveitemnotification.md)
  Posted after a menu item is removed from the menu.
- [class let didSendActionNotification: NSNotification.Name](nsmenu/didsendactionnotification.md)
  Posted just after the application dispatches a menu item’s action method to the menu item’s target.
- [class let willSendActionNotification: NSNotification.Name](nsmenu/willsendactionnotification.md)
  Posted just before the application dispatches a menu item’s action method to the menu item’s target.
### Instance Properties
- [var automaticallyInsertsWritingToolsItems: Bool](nsmenu/automaticallyinsertswritingtoolsitems.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](nsaccessibilityprotocol.md)
- [NSAppearanceCustomization](nsappearancecustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)

## See Also

- [class NSMenuItem](nsmenuitem.md)
  A command item in an app menu.
- [class NSMenuItemBadge](nsmenuitembadge.md)
  A control that provides additional quantitative information specific to a menu item, such as the number of available updates.
- [protocol NSMenuDelegate](nsmenudelegate.md)
  The optional methods implemented by delegates of [`NSMenu`](nsmenu.md) objects to manage menu display and handle some events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu)*