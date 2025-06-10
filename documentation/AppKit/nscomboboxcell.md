# NSComboBoxCell

**Framework**: AppKit  
**Kind**: class

The user interface of a combo box.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSComboBoxCell
```

#### Overview

[`NSComboBoxCell`](nscomboboxcell.md) is a subclass of [`NSTextFieldCell`](nstextfieldcell.md) used to implement the user interface of “combo boxes” (see [`NSComboBox`](nscombobox.md) for information on how combo boxes look and work). The [`NSComboBox`](nscombobox.md) subclass of [`NSTextField`](nstextfield.md) uses a single [`NSComboBoxCell`](nscomboboxcell.md), and essentially all of the [`NSComboBox`](nscombobox.md) class’s methods simply invoke the corresponding [`NSComboBoxCell`](nscomboboxcell.md) method.

Also see the [`NSComboBoxCellDataSource`](nscomboboxcelldatasource.md) protocol, which declares the methods that an [`NSComboBoxCell`](nscomboboxcell.md) object uses to access the contents of its data source object.

## Topics

### Setting Display Attributes
- [var hasVerticalScroller: Bool](nscomboboxcell/hasverticalscroller.md)
  A Boolean value that indicates if the combo box displays a vertical scroller.
- [var isButtonBordered: Bool](nscomboboxcell/isbuttonbordered.md)
  A Boolean value that indicates whether the combo box button displays a border.
- [var intercellSpacing: NSSize](nscomboboxcell/intercellspacing.md)
  The spacing between cells in the combo box’s pop-up list.
- [var itemHeight: CGFloat](nscomboboxcell/itemheight.md)
  The height of each item in the combo box’s pop-up list.
- [var numberOfVisibleItems: Int](nscomboboxcell/numberofvisibleitems.md)
  The maximum number of items visible in the pop-up list at any one time.
### Accessing a Data Source
- [var dataSource: (any NSComboBoxCellDataSource)?](nscomboboxcell/datasource.md)
  The object that provides the data displayed in the combo box’s pop-up list.
- [var usesDataSource: Bool](nscomboboxcell/usesdatasource.md)
  A Boolean value that indicates if the combo box uses an external data source to populate its pop-up list.
### Working with an Internal List
- [func addItems(withObjectValues: [Any])](nscomboboxcell/additems(withobjectvalues:).md)
  Adds multiple objects to the internal item list.
- [func addItem(withObjectValue: Any)](nscomboboxcell/additem(withobjectvalue:).md)
  Adds the specified object to the internal item list.
- [func insertItem(withObjectValue: Any, at: Int)](nscomboboxcell/insertitem(withobjectvalue:at:).md)
  Inserts an object at the specified location in the internal item list.
- [var objectValues: [Any]](nscomboboxcell/objectvalues.md)
  The combo box’s internal item list in an array.
- [func removeAllItems()](nscomboboxcell/removeallitems.md)
  Removes all items from the combo box’s internal item list.
- [func removeItem(at: Int)](nscomboboxcell/removeitem(at:).md)
  Removes the object at the specified location from the combo box’s internal item list.
- [func removeItem(withObjectValue: Any)](nscomboboxcell/removeitem(withobjectvalue:).md)
  Removes all occurrences of the specified object from the combo box’s internal item list.
- [var numberOfItems: Int](nscomboboxcell/numberofitems.md)
  The total number of items in the pop-up list.
### Manipulating the Displayed List
- [func indexOfItem(withObjectValue: Any) -> Int](nscomboboxcell/indexofitem(withobjectvalue:).md)
  Searches the combo box’s internal item list for the given object and returns the matching index number.
- [func itemObjectValue(at: Int) -> Any](nscomboboxcell/itemobjectvalue(at:).md)
  Returns the object located at the specified location in the internal item list.
- [func noteNumberOfItemsChanged()](nscomboboxcell/notenumberofitemschanged.md)
  Informs the combo box that the number of items in its data source has changed.
- [func reloadData()](nscomboboxcell/reloaddata.md)
  Marks the combo box as needing redisplay, so that it will reload the data for visible pop-up items and draw the new values.
- [func scrollItemAtIndexToTop(Int)](nscomboboxcell/scrollitematindextotop(_:).md)
  Scrolls the combo box’s pop-up list vertically so that the item at the given index is as close to the top as possible.
- [func scrollItemAtIndexToVisible(Int)](nscomboboxcell/scrollitematindextovisible(_:).md)
  Scrolls the combo box’s pop-up list vertically so that the item at the given index is visible.
### Manipulating the Selection
- [func deselectItem(at: Int)](nscomboboxcell/deselectitem(at:).md)
  Deselects the pop-up list item at the given index if it’s selected.
- [var indexOfSelectedItem: Int](nscomboboxcell/indexofselecteditem.md)
  The index of the last item selected from the pop-up list.
- [var objectValueOfSelectedItem: Any?](nscomboboxcell/objectvalueofselecteditem.md)
  The object corresponding to the last item selected from the pop-up list.
- [func selectItem(at: Int)](nscomboboxcell/selectitem(at:).md)
  Selects the pop-up list row at the given index.
- [func selectItem(withObjectValue: Any?)](nscomboboxcell/selectitem(withobjectvalue:).md)
  Selects the first pop-up list item that corresponds to the specified object.
### Completing the Text Field
- [func completedString(String) -> String?](nscomboboxcell/completedstring(_:).md)
  Returns a string from the combo box’s pop-up list that starts with the given substring.
- [var completes: Bool](nscomboboxcell/completes.md)
  A Boolean value that indicates if the combo box tries to complete text entered by the user.

## Relationships

### Inherits From
- [NSTextFieldCell](nstextfieldcell.md)
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
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol NSComboBoxCellDataSource](nscomboboxcelldatasource.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxcell)*