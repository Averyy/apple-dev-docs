# NSComboBox

**Framework**: AppKit  
**Kind**: class

A view that displays a list of values in a pop-up menu where the user selects a value or types in a custom value.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSComboBox
```

#### Overview

A combo box combines the behavior of an [`NSTextField`](nstextfield.md) object with an [`NSPopUpButton`](nspopupbutton.md) object. A combo box displays a list of values from a pop-up list, but also provides a means for users to type in custom values. For example, here’s a combo box in its initial state.

![A screenshot of a collapsed combo box.](https://docs-assets.developer.apple.com/published/65f42bd3cb9d4a4446fbf8d1787c78ef/media-4305420%402x.png)

Clicking in the text portion of the control allows the user to edit the current value. When the user clicks the down arrow at the right side of the text field, the pop-up list appears.

![A screenshot of an expanded combo box. The first item in the list, Item A, is selected. The remaining three items are expanded and listed below.](https://docs-assets.developer.apple.com/published/f83a89430289e9e2f8f6682454ce30b5/media-4305419%402x.png)

The [`NSComboBox`](nscombobox.md) class uses [`NSComboBoxCell`](nscomboboxcell.md) to implement its user interface.

Also see the [`NSComboBoxDataSource`](nscomboboxdatasource.md) protocol, which declares the methods that [`NSComboBox`](nscombobox.md) uses to access the contents of its data source object.

## Topics

### Setting Display Attributes
- [var hasVerticalScroller: Bool](nscombobox/hasverticalscroller.md)
  A Boolean value indicating whether the combo box has a vertical scroller.
- [var intercellSpacing: NSSize](nscombobox/intercellspacing.md)
  The horizontal and vertical spacing between cells in the pop-up list.
- [var isButtonBordered: Bool](nscombobox/isbuttonbordered.md)
  A Boolean value indicating whether the combo box displays a border.
- [var itemHeight: CGFloat](nscombobox/itemheight.md)
  The height of each item in the pop-up list.
- [var numberOfVisibleItems: Int](nscombobox/numberofvisibleitems.md)
  The maximum number of visible items to display in the pop-up list at one time.
### Setting a Data Source
- [var dataSource: (any NSComboBoxDataSource)?](nscombobox/datasource.md)
  The object that provides the item data for the combo box.
- [var usesDataSource: Bool](nscombobox/usesdatasource.md)
  A Boolean value indicating whether the combo box retrieves its items from a data source object.
### Configuring the Combo Box Items
- [func addItems(withObjectValues: [Any])](nscombobox/additems(withobjectvalues:).md)
  Adds multiple objects to the end of the receiver’s internal item list.
- [func addItem(withObjectValue: Any)](nscombobox/additem(withobjectvalue:).md)
  Adds an object to the end of the receiver’s internal item list.
- [func insertItem(withObjectValue: Any, at: Int)](nscombobox/insertitem(withobjectvalue:at:).md)
  Inserts an object at the specified location in the receiver’s internal item list.
- [var objectValues: [Any]](nscombobox/objectvalues.md)
  An array of the items from the combo box’s internal list.
- [func removeAllItems()](nscombobox/removeallitems.md)
  Removes all items from the receiver’s internal item list.
- [func removeItem(at: Int)](nscombobox/removeitem(at:).md)
  Removes the object at the specified location from the receiver’s internal item list.
- [func removeItem(withObjectValue: Any)](nscombobox/removeitem(withobjectvalue:).md)
  Removes all occurrences of the given object from the receiver’s internal item list.
- [var numberOfItems: Int](nscombobox/numberofitems.md)
  The total number of items in the pop-up list.
### Manipulating the Displayed List
- [func indexOfItem(withObjectValue: Any) -> Int](nscombobox/indexofitem(withobjectvalue:).md)
  Searches the receiver’s internal item list for the specified object and returns the lowest matching index.
- [func itemObjectValue(at: Int) -> Any](nscombobox/itemobjectvalue(at:).md)
  Returns the object located at the given index within the receiver’s internal item list.
- [func noteNumberOfItemsChanged()](nscombobox/notenumberofitemschanged.md)
  Informs the receiver that the number of items in its data source has changed.
- [func reloadData()](nscombobox/reloaddata.md)
  Marks the receiver as needing redisplay, so that it will reload the data for visible pop-up items and draw the new values.
- [func scrollItemAtIndexToTop(Int)](nscombobox/scrollitematindextotop(_:).md)
  Scrolls the receiver’s pop-up list vertically so that the item at the specified index is as close to the top as possible.
- [func scrollItemAtIndexToVisible(Int)](nscombobox/scrollitematindextovisible(_:).md)
  Scrolls the receiver’s pop-up list vertically so that the item at the specified index is visible.
### Manipulating the Selection
- [func deselectItem(at: Int)](nscombobox/deselectitem(at:).md)
  Deselects the pop-up list item at the specified index if it’s selected.
- [var indexOfSelectedItem: Int](nscombobox/indexofselecteditem.md)
  The index of the last item selected from the pop-up list.
- [var objectValueOfSelectedItem: Any?](nscombobox/objectvalueofselecteditem.md)
  The object corresponding to the last item selected from the pop-up list.
- [func selectItem(at: Int)](nscombobox/selectitem(at:).md)
  Selects the pop-up list row at the given index.
- [func selectItem(withObjectValue: Any?)](nscombobox/selectitem(withobjectvalue:).md)
  Selects the first pop-up list item that corresponds to the given object.
### Completing the Text Field
- [var completes: Bool](nscombobox/completes.md)
  A Boolean value indicating whether the combo box tries to complete what the user types.
### Accessing the Delegate
- [var delegate: (any NSComboBoxDelegate)?](nscombobox/delegate.md)
  Sets the receiver’s delegate.
### Notifications
- [class let selectionDidChangeNotification: NSNotification.Name](nscombobox/selectiondidchangenotification.md)
  Posted after the pop-up list selection of the `NSComboBox` changes.
- [class let selectionIsChangingNotification: NSNotification.Name](nscombobox/selectionischangingnotification.md)
  Posted whenever the pop-up list selection of the `NSComboBox` is changing.
- [class let willDismissNotification: NSNotification.Name](nscombobox/willdismissnotification.md)
  Posted whenever the pop-up list of the `NSComboBox` is about to be dismissed.
- [class let willPopUpNotification: NSNotification.Name](nscombobox/willpopupnotification.md)
  Posted whenever the pop-up list of the `NSComboBox` is going to be displayed.

## Relationships

### Inherits From
- [NSTextField](nstextfield.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSAccessibilityNavigableStaticText](nsaccessibilitynavigablestatictext.md)
- [NSAccessibilityProtocol](nsaccessibilityprotocol.md)
- [NSAccessibilityStaticText](nsaccessibilitystatictext.md)
- [NSAnimatablePropertyContainer](nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](nsappearancecustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSDraggingDestination](nsdraggingdestination.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](nsstandardkeybindingresponding.md)
- [NSTextContent](nstextcontent.md)
- [NSTouchBarProvider](nstouchbarprovider.md)
- [NSUserActivityRestoring](nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [NSUserInterfaceValidations](nsuserinterfacevalidations.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobox)*