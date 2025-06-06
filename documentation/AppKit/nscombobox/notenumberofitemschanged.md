# noteNumberOfItemsChanged()

**Framework**: AppKit  
**Kind**: method

Informs the receiver that the number of items in its data source has changed.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func noteNumberOfItemsChanged()
```

#### Discussion

This method allows the receiver to update the scrollers in its displayed pop-up list without actually reloading data into the receiver. It is particularly useful for a data source that continually receives data in the background over a period of time, in which case the `NSComboBox` can remain responsive to the user while the data is received.

See the NSComboBoxDataSource informal protocol specification for information on the messages an `NSComboBox` sends to its data source.

## See Also

- [func indexOfItem(withObjectValue: Any) -> Int](nscombobox/indexofitem(withobjectvalue:).md)
  Searches the receiver’s internal item list for the specified object and returns the lowest matching index.
- [func itemObjectValue(at: Int) -> Any](nscombobox/itemobjectvalue(at:).md)
  Returns the object located at the given index within the receiver’s internal item list.
- [func reloadData()](nscombobox/reloaddata.md)
  Marks the receiver as needing redisplay, so that it will reload the data for visible pop-up items and draw the new values.
- [func scrollItemAtIndexToTop(Int)](nscombobox/scrollitematindextotop(_:).md)
  Scrolls the receiver’s pop-up list vertically so that the item at the specified index is as close to the top as possible.
- [func scrollItemAtIndexToVisible(Int)](nscombobox/scrollitematindextovisible(_:).md)
  Scrolls the receiver’s pop-up list vertically so that the item at the specified index is visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobox/notenumberofitemschanged())*