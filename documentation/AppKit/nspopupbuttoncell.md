# NSPopUpButtonCell

**Framework**: AppKit  
**Kind**: class

The `NSPopUpButtonCell` class defines the visual appearance of pop-up buttons that display pop-up or pull-down menus. Pop-up menus present the user with a set of choices, much the way radio buttons do, but using much less space. Pull-down menus also provide a set of choices but present the information in a slightly different way, usually to provide a set of commands from which the user can choose.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSPopUpButtonCell
```

#### Overview

The `NSPopUpButtonCell` class implements the user interface for the [`NSPopUpButton`](nspopupbutton.md) class.

Changes made to a menu (such as adding, removing, or changing the items) are not apparent while the menu is being displayed or interacted with.

> ❗ **Important**: Setting a pop up button’s [`image`](nscell/image.md) property has no effect. The image displayed in a pop up button is taken from the selected menu item (in the case of a pop up menu) or from the first menu item (in the case of a pull-down menu).

## Topics

### Initialization
- [init(textCell: String, pullsDown: Bool)](nspopupbuttoncell/init(textcell:pullsdown:).md)
  Returns an `NSPopUpButtonCell` object initialized with the specified title.
### Accessing menu attributes
- [var menu: NSMenu?](nspopupbuttoncell/menu.md)
  The pop-up button’s associated menu.
- [var pullsDown: Bool](nspopupbuttoncell/pullsdown.md)
  A Boolean value that indicates the behavior of the button’s menu.
- [var autoenablesItems: Bool](nspopupbuttoncell/autoenablesitems.md)
  A Boolean value that indicates if the button automatically enables and disables its items every time a user event occurs.
- [var preferredEdge: NSRectEdge](nspopupbuttoncell/preferrededge.md)
  The edge of the cell from which the menu should pop out when screen conditions are restrictive.
- [var usesItemFromMenu: Bool](nspopupbuttoncell/usesitemfrommenu.md)
  A Boolean value that indicates if the control uses an item from the menu for its own title.
- [var altersStateOfSelectedItem: Bool](nspopupbuttoncell/altersstateofselecteditem.md)
  A Boolean value that indicates if the pop-up button links the state of the selected menu item to the current selection.
- [var arrowPosition: NSPopUpButton.ArrowPosition](nspopupbuttoncell/arrowposition.md)
  The position of the arrow displayed on the button.
### Adding and removing items
- [func addItem(withTitle: String)](nspopupbuttoncell/additem(withtitle:).md)
  Adds an item with the specified title to the end of the menu.
- [func addItems(withTitles: [String])](nspopupbuttoncell/additems(withtitles:).md)
  Adds multiple items to the end of the menu.
- [func insertItem(withTitle: String, at: Int)](nspopupbuttoncell/insertitem(withtitle:at:).md)
  Inserts an item at the specified position in the menu.
- [func removeItem(withTitle: String)](nspopupbuttoncell/removeitem(withtitle:).md)
  Removes the item with the specified title from the menu.
- [func removeItem(at: Int)](nspopupbuttoncell/removeitem(at:).md)
  Removes the item at the specified index.
- [func removeAllItems()](nspopupbuttoncell/removeallitems.md)
  Removes all items in the receiver’s item menu.
### Accessing the items
- [var itemArray: [NSMenuItem]](nspopupbuttoncell/itemarray.md)
  An array of [`NSMenuItem`](nsmenuitem.md) objects that represent the items in the menu.
- [var numberOfItems: Int](nspopupbuttoncell/numberofitems.md)
  The number of items in the menu.
- [func index(of: NSMenuItem) -> Int](nspopupbuttoncell/index(of:).md)
  Returns the index of the specified menu item.
- [func indexOfItem(withTitle: String) -> Int](nspopupbuttoncell/indexofitem(withtitle:).md)
  Returns the index of the item with the specified title.
- [func indexOfItem(withTag: Int) -> Int](nspopupbuttoncell/indexofitem(withtag:).md)
  Returns the index of the menu item with the specified tag.
- [func indexOfItem(withRepresentedObject: Any?) -> Int](nspopupbuttoncell/indexofitem(withrepresentedobject:).md)
  Returns the index of the menu item that holds the specified represented object.
- [func indexOfItem(withTarget: Any?, andAction: Selector?) -> Int](nspopupbuttoncell/indexofitem(withtarget:andaction:).md)
  Returns the index of the menu item with the specified target and action.
- [func item(at: Int) -> NSMenuItem?](nspopupbuttoncell/item(at:).md)
  Returns the menu item at the specified index.
- [func item(withTitle: String) -> NSMenuItem?](nspopupbuttoncell/item(withtitle:).md)
  Returns the menu item with the specified title.
- [var lastItem: NSMenuItem?](nspopupbuttoncell/lastitem.md)
  The last item in the menu.
### Dealing with selection
- [func select(NSMenuItem?)](nspopupbuttoncell/select(_:).md)
  Selects the specified menu item.
- [func selectItem(at: Int)](nspopupbuttoncell/selectitem(at:).md)
  Selects the item in the menu at the specified index.
- [func selectItem(withTag: Int) -> Bool](nspopupbuttoncell/selectitem(withtag:).md)
  Selects the menu item with the specified tag.
- [func selectItem(withTitle: String)](nspopupbuttoncell/selectitem(withtitle:).md)
  Selects the item with the specified title.
- [func setTitle(String?)](nspopupbuttoncell/settitle(_:).md)
  Sets the string displayed in the receiver when the user isn’t pressing the mouse button.
- [var selectedItem: NSMenuItem?](nspopupbuttoncell/selecteditem.md)
  The menu item last selected by the user.
- [var indexOfSelectedItem: Int](nspopupbuttoncell/indexofselecteditem.md)
  The index of the item last selected by the user.
- [func synchronizeTitleAndSelectedItem()](nspopupbuttoncell/synchronizetitleandselecteditem.md)
  Synchronizes the pop-up button’s displayed item with the currently selected menu item.
### Title conveniences
- [func itemTitle(at: Int) -> String](nspopupbuttoncell/itemtitle(at:).md)
  Returns the title of the item at the specified index.
- [var itemTitles: [String]](nspopupbuttoncell/itemtitles.md)
  An array of `NSString` objects containing the titles of every item in the menu.
- [var titleOfSelectedItem: String?](nspopupbuttoncell/titleofselecteditem.md)
  The title of the item last selected by the user.
### Handling events and action messages
- [func attachPopUp(withFrame: NSRect, in: NSView)](nspopupbuttoncell/attachpopup(withframe:in:).md)
  Sets up the receiver to display a menu.
- [func dismissPopUp()](nspopupbuttoncell/dismisspopup.md)
  Dismisses the pop-up button’s menu by ordering its window out.
- [func performClick(withFrame: NSRect, in: NSView)](nspopupbuttoncell/performclick(withframe:in:).md)
  Displays the receiver’s menu and track mouse events in it.
### Constants
- [NSPopUpButton.ArrowPosition](nspopupbutton/arrowposition.md)
  These constants are defined for use with the [`arrowPosition`](nspopupbuttoncell/arrowposition.md) property.
### Notifications
- [class let willPopUpNotification: NSNotification.Name](nspopupbuttoncell/willpopupnotification.md)
  This notification is posted just before a pop-up menu is attached to its window frame.
### Initializers
- [init(coder: NSCoder)](nspopupbuttoncell/init(coder:).md)

## Relationships

### Inherits From
- [NSMenuItemCell](nsmenuitemcell.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](nsaccessibilityprotocol.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSMenuItemValidation](nsmenuitemvalidation.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbuttoncell)*