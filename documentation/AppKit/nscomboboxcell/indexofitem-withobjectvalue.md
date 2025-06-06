# indexOfItem(withObjectValue:)

**Framework**: AppKit  
**Kind**: method

Searches the combo box’s internal item list for the given object and returns the matching index number.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func indexOfItem(withObjectValue object: Any) -> Int
```

#### Return Value

The lowest index whose corresponding value is equal to `anObject`. Objects are considered equal if they have the same id or if `isEqual:` returns [`true`](https://developer.apple.com/documentation/swift/true). If none of the objects in the combo box’s internal item list is equal to `anObject`, [`indexOfItem(withObjectValue:)`](nscomboboxcell/indexofitem(withobjectvalue:).md) returns `NSNotFound`.

#### Discussion

This method logs a warning if [`usesDataSource`](nscomboboxcell/usesdatasource.md) is [`true`](https://developer.apple.com/documentation/swift/true).

## Parameters

- `object`: The object for which to return the index.

## See Also

- [func selectItem(withObjectValue: Any?)](nscomboboxcell/selectitem(withobjectvalue:).md)
  Selects the first pop-up list item that corresponds to the specified object.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxcell/indexofitem(withobjectvalue:))*