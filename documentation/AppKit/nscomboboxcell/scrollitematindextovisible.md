# scrollItemAtIndexToVisible(_:)

**Framework**: AppKit  
**Kind**: method

Scrolls the combo box’s pop-up list vertically so that the item at the given index is visible.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func scrollItemAtIndexToVisible(_ index: Int)
```

#### Discussion

The pop-up list need not be displayed at the time this method is invoked.

## Parameters

- `index`: The index of the item to make visible.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxcell/scrollitematindextovisible(_:))*