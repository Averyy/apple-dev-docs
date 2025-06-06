# scrollItemAtIndexToVisible(_:)

**Framework**: AppKit  
**Kind**: method

Scrolls the receiver’s pop-up list vertically so that the item at the specified index is visible.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobox/scrollitematindextovisible(_:))*