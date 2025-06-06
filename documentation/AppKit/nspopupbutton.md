# NSPopUpButton

**Framework**: AppKit  
**Kind**: class

A control for selecting an item from a list.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSPopUpButton
```

#### Overview

An `NSPopUpButton` object uses an [`NSPopUpButtonCell`](nspopupbuttoncell.md) object to implement its user interface.

Note that while a menu is tracking user input, programmatic changes to the menu, such as adding, removing, or changing items on the menu, is not reflected.

> ❗ **Important**: Setting a pop up button’s [`image`](nscell/image.md) property has no effect. The image displayed in a pop up button is taken from the selected menu item (in the case of a pop up menu) or from the first menu item (in the case of a pull-down menu).

Setting a pop up button’s [`image`](nscell/image.md) property has no effect. The image displayed in a pop up button is taken from the selected menu item (in the case of a pop up menu) or from the first menu item (in the case of a pull-down menu).

## Topics

### Initializing an NSPopUpButton
- [init(frame: NSRect, pullsDown: Bool)](nspopupbutton/init(frame:pullsdown:).md)
  Returns an `NSPopUpButton` object initialized to the specified dimensions.
### Configuring the Cell
- [class NSPopUpButtonCell](nspopupbuttoncell.md)
  The `NSPopUpButtonCell` class defines the visual appearance of pop-up buttons that display pop-up or pull-down menus. Pop-up menus present the user with a set of choices, much the way radio buttons do, but using much less space. Pull-down menus also provide a set of choices but present the information in a slightly different way, usually to provide a set of commands from which the user can choose.
### Setting the type of menu
- [var pullsDown: Bool](nspopupbutton/pullsdown.md)
  A Boolean value indicating whether the button displays a pull-down or pop-up menu.
- [var autoenablesItems: Bool](nspopupbutton/autoenablesitems.md)
  A Boolean value indicating whether the button enables and disables its items every time a user event occurs.
### Inserting and deleting items
- [func addItem(withTitle: String)](nspopupbutton/additem(withtitle:).md)
  Adds an item with the specified title to the end of the menu.
- [func addItems(withTitles: [String])](nspopupbutton/additems(withtitles:).md)
  Adds multiple items to the end of the menu.
- [func insertItem(withTitle: String, at: Int)](nspopupbutton/insertitem(withtitle:at:).md)
  Inserts an item at the specified position in the menu.
- [func removeAllItems()](nspopupbutton/removeallitems.md)
  Removes all items in the receiver’s item menu.
- [func removeItem(withTitle: String)](nspopupbutton/removeitem(withtitle:).md)
  Removes the item with the specified title from the menu.
- [func removeItem(at: Int)](nspopupbutton/removeitem(at:).md)
  Removes the item at the specified index.
### Getting the user’s selection
- [var selectedItem: NSMenuItem?](nspopupbutton/selecteditem.md)
  The menu item that was last selected by the user.
- [var titleOfSelectedItem: String?](nspopupbutton/titleofselecteditem.md)
  The title of the item that was last selected by the user.
- [var indexOfSelectedItem: Int](nspopupbutton/indexofselecteditem.md)
  The index of the item that was last selected by the user.
### Setting the current selection
- [func select(NSMenuItem?)](nspopupbutton/select(_:).md)
  Selects the specified menu item.
- [func selectItem(at: Int)](nspopupbutton/selectitem(at:).md)
  Selects the item in the menu at the specified index.
- [func selectItem(withTag: Int) -> Bool](nspopupbutton/selectitem(withtag:).md)
  Selects the menu item with the specified tag.
- [func selectItem(withTitle: String)](nspopupbutton/selectitem(withtitle:).md)
  Selects the item with the specified title.
### Getting menu items
- [var menu: NSMenu?](nspopupbutton/menu.md)
  The menu associated with the pop-up button.
- [var numberOfItems: Int](nspopupbutton/numberofitems.md)
  The number of items in the menu.
- [var itemArray: [NSMenuItem]](nspopupbutton/itemarray.md)
  The array of menu item objects associated with the button.
- [func item(at: Int) -> NSMenuItem?](nspopupbutton/item(at:).md)
  Returns the menu item at the specified index.
- [func itemTitle(at: Int) -> String](nspopupbutton/itemtitle(at:).md)
  Returns the title of the item at the specified index.
- [var itemTitles: [String]](nspopupbutton/itemtitles.md)
  An array of strings corresponding to the titles of the items in the menu.
- [func item(withTitle: String) -> NSMenuItem?](nspopupbutton/item(withtitle:).md)
  Returns the menu item with the specified title.
- [var lastItem: NSMenuItem?](nspopupbutton/lastitem.md)
  The last item in the menu.
### Getting the indices of menu items
- [func index(of: NSMenuItem) -> Int](nspopupbutton/index(of:).md)
  Returns the index of the specified menu item.
- [func indexOfItem(withTag: Int) -> Int](nspopupbutton/indexofitem(withtag:).md)
  Returns the index of the menu item with the specified tag.
- [func indexOfItem(withTitle: String) -> Int](nspopupbutton/indexofitem(withtitle:).md)
  Returns the index of the item with the specified title.
- [func indexOfItem(withRepresentedObject: Any?) -> Int](nspopupbutton/indexofitem(withrepresentedobject:).md)
  Returns the index of the menu item that holds the specified represented object.
- [func indexOfItem(withTarget: Any?, andAction: Selector?) -> Int](nspopupbutton/indexofitem(withtarget:andaction:).md)
  Returns the index of the menu item with the specified target and action.
### Setting the cell edge to pop out in restricted situations
- [var preferredEdge: NSRectEdge](nspopupbutton/preferrededge.md)
  The edge of the button on which to display the menu when screen space is constrained.
### Setting the title
- [func setTitle(String)](nspopupbutton/settitle(_:).md)
  Sets the string displayed in the receiver when the user isn’t pressing the mouse button.
### Setting the state
- [func synchronizeTitleAndSelectedItem()](nspopupbutton/synchronizetitleandselecteditem.md)
  Ensures that the item being displayed by the receiver agrees with the selected item.
### Notifications
- [class let willPopUpNotification: NSNotification.Name](nspopupbutton/willpopupnotification.md)
  Posted when an `NSPopUpButton` object receives a mouse-down event—that is, when the user is about to select an item from the menu.
### Instance Methods
- [func selectedTag() -> Int](nspopupbutton/selectedtag.md)
### Initializers
- [convenience init(image: NSImage, pullDownMenu: NSMenu)](nspopupbutton/init(image:pulldownmenu:).md)
  Creates a standard pull-down button with a title, optional image, and menu.
- [convenience init(popUpMenu: NSMenu, target: AnyObject?, action: Selector?)](nspopupbutton/init(popupmenu:target:action:).md)
  Creates a standard pop-up button with a menu, target, and action.
- [convenience init(title: String, image: NSImage?, pullDownMenu: NSMenu)](nspopupbutton/init(title:image:pulldownmenu:).md)
  Creates a standard pull-down button with a title, optional image, and menu.
### Instance Properties
- [var altersStateOfSelectedItem: Bool](nspopupbutton/altersstateofselecteditem.md)
  When the value of this property is `YES`, the selected menu item’s `state` is set to `NSControlStateValueOn`. When the value of this property is `NO`, the menu item’s `state` is not changed. When this property changes, the `state` of the currently selected item is updated appropriately. This property is ignored for pull-down buttons.
- [var usesItemFromMenu: Bool](nspopupbutton/usesitemfrommenu.md)
  When `usesItemFromMenu` is `YES`, a pull-down button uses the title of the first menu item and hides the first menu item. A pop-up button uses the title of the currently selected menu. The default value is `YES`.

## Relationships

### Inherits From
- [NSButton](nsbutton.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityButton](nsaccessibilitybutton.md)
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](nsappearancecustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSDraggingDestination](nsdraggingdestination.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](nstouchbarprovider.md)
- [NSUserActivityRestoring](nsuseractivityrestoring.md)
- [NSUserInterfaceCompression](nsuserinterfacecompression.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [NSUserInterfaceValidations](nsuserinterfacevalidations.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Responding to control-based events using target-action](../UIKit/responding-to-control-based-events-using-target-action.md)
  Handle user input by connecting buttons, sliders, and other controls to your app’s code using the target-action design pattern.
- [class NSButton](nsbutton.md)
  A control that defines an area on the screen that a user clicks to trigger an action.
- [class NSColorWell](nscolorwell.md)
  A control that displays a color value and lets the user change that color value.
- [Combo Box](combo-box.md)
  Display a list of values in a pop-up menu that lets the user select a value or type in a custom value.
- [class NSComboButton](nscombobutton.md)
  A button with a pull-down menu and a default action.
- [Date Picker](date-picker.md)
  Display a calendar date and provide controls for editing the date value.
- [class NSImageView](nsimageview.md)
  A display of image data in a frame.
- [class NSLevelIndicator](nslevelindicator.md)
  A visual representation of a level or quantity, using discrete values.
- [Path Control](path-control.md)
  A display of a file system path or virtual path information.
- [class NSProgressIndicator](nsprogressindicator.md)
  An interface that provides visual feedback to the user about the status of an ongoing task.
- [class NSRuleEditor](nsruleeditor.md)
  An interface for configuring a rule-based list of options.
- [class NSPredicateEditor](nspredicateeditor.md)
  A defined set of rules that allows the editing of predicate objects.
- [Search Field](search-field.md)
  Provide a text field that is optimized for text-based search interfaces.
- [class NSSegmentedControl](nssegmentedcontrol.md)
  Display one or more buttons in a single horizontal group.
- [Slider](slider.md)
  Display a range of values from which the user selects a single value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton)*