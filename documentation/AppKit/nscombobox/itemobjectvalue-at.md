# itemObjectValue(at:)

**Framework**: AppKit  
**Kind**: method

Returns the object located at the given index within the receiver’s internal item list.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func itemObjectValue(at index: Int) -> Any
```

#### Return Value

The object located at the specified index in the internal item list.

#### Discussion

This method logs a warning if the [`usesDataSource`](nscombobox/usesdatasource.md) property is [`true`](https://developer.apple.com/documentation/Swift/true).

## Parameters

- `index`: The index of the object to retrieve. If   is beyond the end of the list, an   is raised.

## See Also

- [var objectValueOfSelectedItem: Any?](nscombobox/objectvalueofselecteditem.md)
  The object corresponding to the last item selected from the pop-up list.
- [func indexOfItem(withObjectValue: Any) -> Int](nscombobox/indexofitem(withobjectvalue:).md)
  Searches the receiver’s internal item list for the specified object and returns the lowest matching index.
- [func noteNumberOfItemsChanged()](nscombobox/notenumberofitemschanged.md)
  Informs the receiver that the number of items in its data source has changed.
- [func reloadData()](nscombobox/reloaddata.md)
  Marks the receiver as needing redisplay, so that it will reload the data for visible pop-up items and draw the new values.
- [func scrollItemAtIndexToTop(Int)](nscombobox/scrollitematindextotop(_:).md)
  Scrolls the receiver’s pop-up list vertically so that the item at the specified index is as close to the top as possible.
- [func scrollItemAtIndexToVisible(Int)](nscombobox/scrollitematindextovisible(_:).md)
  Scrolls the receiver’s pop-up list vertically so that the item at the specified index is visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobox/itemobjectvalue(at:))*