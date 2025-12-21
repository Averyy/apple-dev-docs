# itemObjectValue(at:)

**Framework**: AppKit  
**Kind**: method

Returns the object located at the specified location in the internal item list.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func itemObjectValue(at index: Int) -> Any
```

#### Return Value

The object at the given location in the combo box’s internal item list.

#### Discussion

This method logs a warning if [`usesDataSource`](nscomboboxcell/usesdatasource.md) is [`true`](https://developer.apple.com/documentation/Swift/true).

## Parameters

- `index`: The index of the object to return. If   is beyond the end of the list, an   is raised.

## See Also

- [var objectValueOfSelectedItem: Any?](nscomboboxcell/objectvalueofselecteditem.md)
  The object corresponding to the last item selected from the pop-up list.
- [func indexOfItem(withObjectValue: Any) -> Int](nscomboboxcell/indexofitem(withobjectvalue:).md)
  Searches the combo box’s internal item list for the given object and returns the matching index number.
- [func noteNumberOfItemsChanged()](nscomboboxcell/notenumberofitemschanged.md)
  Informs the combo box that the number of items in its data source has changed.
- [func reloadData()](nscomboboxcell/reloaddata.md)
  Marks the combo box as needing redisplay, so that it will reload the data for visible pop-up items and draw the new values.
- [func scrollItemAtIndexToTop(Int)](nscomboboxcell/scrollitematindextotop(_:).md)
  Scrolls the combo box’s pop-up list vertically so that the item at the given index is as close to the top as possible.
- [func scrollItemAtIndexToVisible(Int)](nscomboboxcell/scrollitematindextovisible(_:).md)
  Scrolls the combo box’s pop-up list vertically so that the item at the given index is visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxcell/itemobjectvalue(at:))*