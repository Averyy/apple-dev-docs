# reloadData()

**Framework**: AppKit  
**Kind**: method

Marks the receiver as needing redisplay, so that it will reload the data for visible pop-up items and draw the new values.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func reloadData()
```

## See Also

- [func indexOfItem(withObjectValue: Any) -> Int](nscombobox/indexofitem(withobjectvalue:).md)
  Searches the receiver’s internal item list for the specified object and returns the lowest matching index.
- [func itemObjectValue(at: Int) -> Any](nscombobox/itemobjectvalue(at:).md)
  Returns the object located at the given index within the receiver’s internal item list.
- [func noteNumberOfItemsChanged()](nscombobox/notenumberofitemschanged.md)
  Informs the receiver that the number of items in its data source has changed.
- [func scrollItemAtIndexToTop(Int)](nscombobox/scrollitematindextotop(_:).md)
  Scrolls the receiver’s pop-up list vertically so that the item at the specified index is as close to the top as possible.
- [func scrollItemAtIndexToVisible(Int)](nscombobox/scrollitematindextovisible(_:).md)
  Scrolls the receiver’s pop-up list vertically so that the item at the specified index is visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobox/reloaddata())*