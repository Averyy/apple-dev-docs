# indexOfItem(withObjectValue:)

**Framework**: AppKit  
**Kind**: method

Searches the receiver’s internal item list for the specified object and returns the lowest matching index.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func indexOfItem(withObjectValue object: Any) -> Int
```

#### Return Value

The lowest index in the internal item list whose corresponding value is equal to that of the specified object. Objects are considered equal if they have the same id or if `isEqual:` returns [`true`](https://developer.apple.com/documentation/swift/true).

#### Discussion

If none of the objects in the receiver’s internal item list are equal to `anObject`, [`indexOfItem(withObjectValue:)`](nscombobox/indexofitem(withobjectvalue:).md) returns `NSNotFound`.

#### Discussion

This method logs a warning if the [`usesDataSource`](nscombobox/usesdatasource.md) property is [`true`](https://developer.apple.com/documentation/swift/true).

## Parameters

- `object`: The object for which to return the index.

## See Also

- [func selectItem(withObjectValue: Any?)](nscombobox/selectitem(withobjectvalue:).md)
  Selects the first pop-up list item that corresponds to the given object.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobox/indexofitem(withobjectvalue:))*