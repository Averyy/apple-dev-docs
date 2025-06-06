# noteNumberOfItemsChanged()

**Framework**: AppKit  
**Kind**: method

Informs the combo box that the number of items in its data source has changed.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func noteNumberOfItemsChanged()
```

#### Discussion

This method allows the combo box to update the scrollers in its displayed pop-up list without actually reloading data into the combo box. It is particularly useful for a data source that continually receives data in the background over a period of time, in which case the `NSComboBoxCell` can remain responsive to the user while the data is received.

See the NSComboBoxCellDataSource informal protocol specification for information on the messages an `NSComboBoxCell` sends to its data source.

## See Also

- [func indexOfItem(withObjectValue: Any) -> Int](nscomboboxcell/indexofitem(withobjectvalue:).md)
  Searches the combo box’s internal item list for the given object and returns the matching index number.
- [func itemObjectValue(at: Int) -> Any](nscomboboxcell/itemobjectvalue(at:).md)
  Returns the object located at the specified location in the internal item list.
- [func reloadData()](nscomboboxcell/reloaddata.md)
  Marks the combo box as needing redisplay, so that it will reload the data for visible pop-up items and draw the new values.
- [func scrollItemAtIndexToTop(Int)](nscomboboxcell/scrollitematindextotop(_:).md)
  Scrolls the combo box’s pop-up list vertically so that the item at the given index is as close to the top as possible.
- [func scrollItemAtIndexToVisible(Int)](nscomboboxcell/scrollitematindextovisible(_:).md)
  Scrolls the combo box’s pop-up list vertically so that the item at the given index is visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxcell/notenumberofitemschanged())*