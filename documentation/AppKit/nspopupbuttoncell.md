# NSPopUpButtonCell

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

The `NSPopUpButtonCell` class defines the visual appearance of pop-up buttons that display pop-up or pull-down menus. Pop-up menus present the user with a set of choices, much the way radio buttons do, but using much less space. Pull-down menus also provide a set of choices but present the information in a slightly different way, usually to provide a set of commands from which the user can choose.

**Availability**:
- macOS

## Declaration

```swift
class NSPopUpButtonCell
```

```objc
@interface NSPopUpButtonCell : NSMenuItemCell
```

## Overview

The `NSPopUpButtonCell` class implements the user interface for the [`NSPopUpButton`](./nspopupbutton.md) class.

Changes made to a menu (such as adding, removing, or changing the items) are not apparent while the menu is being displayed or interacted with.

> ❗ **Important**: Setting a pop up button’s [`image`](./nscell/image.md) property has no effect. The image displayed in a pop up button is taken from the selected menu item (in the case of a pop up menu) or from the first menu item (in the case of a pull-down menu).

## Topics

### Initialization
- [init(textCell: String, pullsDown: Bool)](./nspopupbuttoncell/init%28textcell,pullsdown%29.md)
  Returns an `NSPopUpButtonCell` object initialized with the specified title.
### Accessing menu attributes
- [var menu: NSMenu?](./nspopupbuttoncell/menu.md)
  The pop-up button’s associated menu.
- [var pullsDown: Bool](./nspopupbuttoncell/pullsdown.md)
  A Boolean value that indicates the behavior of the button’s menu.
- [var autoenablesItems: Bool](./nspopupbuttoncell/autoenablesitems.md)
  A Boolean value that indicates if the button automatically enables and disables its items every time a user event occurs.
- [var preferredEdge: NSRectEdge](./nspopupbuttoncell/preferrededge.md)
  The edge of the cell from which the menu should pop out when screen conditions are restrictive.
- [var usesItemFromMenu: Bool](./nspopupbuttoncell/usesitemfrommenu.md)
  A Boolean value that indicates if the control uses an item from the menu for its own title.
- [var altersStateOfSelectedItem: Bool](./nspopupbuttoncell/altersstateofselecteditem.md)
  A Boolean value that indicates if the pop-up button links the state of the selected menu item to the current selection.
- [var arrowPosition: NSPopUpButton.ArrowPosition](./nspopupbuttoncell/arrowposition.md)
  The position of the arrow displayed on the button.
### Adding and removing items
- [func addItem(withTitle: String)](./nspopupbuttoncell/additem%28withtitle%29.md)
  Adds an item with the specified title to the end of the menu.
- [func addItems(withTitles: [String])](./nspopupbuttoncell/additems%28withtitles%29.md)
  Adds multiple items to the end of the menu.
- [func insertItem(withTitle: String, at: Int)](./nspopupbuttoncell/insertitem%28withtitle,at%29.md)
  Inserts an item at the specified position in the menu.
- [func removeItem(withTitle: String)](./nspopupbuttoncell/removeitem%28withtitle%29.md)
  Removes the item with the specified title from the menu.
- [func removeItem(at: Int)](./nspopupbuttoncell/removeitem%28at%29.md)
  Removes the item at the specified index.
- [func removeAllItems()](./nspopupbuttoncell/removeallitems%28%29.md)
  Removes all items in the receiver’s item menu.
### Accessing the items
- [var itemArray: [NSMenuItem]](./nspopupbuttoncell/itemarray.md)
  An array of [`NSMenuItem`](./nsmenuitem.md) objects that represent the items in the menu.
- [var numberOfItems: Int](./nspopupbuttoncell/numberofitems.md)
  The number of items in the menu.
- [func index(of: NSMenuItem) -> Int](./nspopupbuttoncell/index%28of%29.md)
  Returns the index of the specified menu item.
- [func indexOfItem(withTitle: String) -> Int](./nspopupbuttoncell/indexofitem%28withtitle%29.md)
  Returns the index of the item with the specified title.
- [func indexOfItem(withTag: Int) -> Int](./nspopupbuttoncell/indexofitem%28withtag%29.md)
  Returns the index of the menu item with the specified tag.
- [func indexOfItem(withRepresentedObject: Any?) -> Int](./nspopupbuttoncell/indexofitem%28withrepresentedobject%29.md)
  Returns the index of the menu item that holds the specified represented object.
- [func indexOfItem(withTarget: Any?, andAction: Selector?) -> Int](./nspopupbuttoncell/indexofitem%28withtarget,andaction%29.md)
  Returns the index of the menu item with the specified target and action.
- [func item(at: Int) -> NSMenuItem?](./nspopupbuttoncell/item%28at%29.md)
  Returns the menu item at the specified index.
- [func item(withTitle: String) -> NSMenuItem?](./nspopupbuttoncell/item%28withtitle%29.md)
  Returns the menu item with the specified title.
- [var lastItem: NSMenuItem?](./nspopupbuttoncell/lastitem.md)
  The last item in the menu.
### Dealing with selection
- [func select(NSMenuItem?)](./nspopupbuttoncell/select%28_%29.md)
  Selects the specified menu item.
- [func selectItem(at: Int)](./nspopupbuttoncell/selectitem%28at%29.md)
  Selects the item in the menu at the specified index.
- [func selectItem(withTag: Int) -> Bool](./nspopupbuttoncell/selectitem%28withtag%29.md)
  Selects the menu item with the specified tag.
- [func selectItem(withTitle: String)](./nspopupbuttoncell/selectitem%28withtitle%29.md)
  Selects the item with the specified title.
- [func setTitle(String?)](./nspopupbuttoncell/settitle%28_%29.md)
  Sets the string displayed in the receiver when the user isn’t pressing the mouse button.
- [var selectedItem: NSMenuItem?](./nspopupbuttoncell/selecteditem.md)
  The menu item last selected by the user.
- [var indexOfSelectedItem: Int](./nspopupbuttoncell/indexofselecteditem.md)
  The index of the item last selected by the user.
- [func synchronizeTitleAndSelectedItem()](./nspopupbuttoncell/synchronizetitleandselecteditem%28%29.md)
  Synchronizes the pop-up button’s displayed item with the currently selected menu item.
### Title conveniences
- [func itemTitle(at: Int) -> String](./nspopupbuttoncell/itemtitle%28at%29.md)
  Returns the title of the item at the specified index.
- [var itemTitles: [String]](./nspopupbuttoncell/itemtitles.md)
  An array of `NSString` objects containing the titles of every item in the menu.
- [var titleOfSelectedItem: String?](./nspopupbuttoncell/titleofselecteditem.md)
  The title of the item last selected by the user.
### Handling events and action messages
- [func attachPopUp(withFrame: NSRect, in: NSView)](./nspopupbuttoncell/attachpopup%28withframe,in%29.md)
  Sets up the receiver to display a menu.
- [func dismissPopUp()](./nspopupbuttoncell/dismisspopup%28%29.md)
  Dismisses the pop-up button’s menu by ordering its window out.
- [func performClick(withFrame: NSRect, in: NSView)](./nspopupbuttoncell/performclick%28withframe,in%29.md)
  Displays the receiver’s menu and track mouse events in it.
### Constants
- [NSPopUpButton.ArrowPosition](./nspopupbutton/arrowposition.md)
  These constants are defined for use with the [`arrowPosition`](./nspopupbuttoncell/arrowposition.md) property.
### Notifications
- [class let willPopUpNotification: NSNotification.Name](./nspopupbuttoncell/willpopupnotification.md)
  This notification is posted just before a pop-up menu is attached to its window frame.
### Initializers
- [init(coder: NSCoder)](./nspopupbuttoncell/init%28coder%29.md)
### Structures
- [NSPopUpButtonCell.WillPopUpMessage](./nspopupbuttoncell/willpopupmessage.md)

## Relationships

### Inherits From
- [NSMenuItemCell](./nsmenuitemcell.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSAccessibilityElementProtocol](./nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](./nsaccessibilityprotocol.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSMenuItemValidation](./nsmenuitemvalidation.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSUserInterfaceItemIdentification](./nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbuttoncell)*