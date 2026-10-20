# itemObjectValue(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the object located at the specified location in the internal item list.

**Availability**:
- macOS

## Declaration

```swift
func itemObjectValue(at index: Int) -> Any
```

```objc
- (id) itemObjectValueAtIndex:(NSInteger) index;
```

#### Return Value

The object at the given location in the combo box’s internal item list.

#### Discussion

This method logs a warning if [`usesDataSource`](./usesdatasource.md) is [`true`](../../Swift/true.md).

## Parameters

- `index`: The index of the object to return. If `index` is beyond the end of the list, an `NSRangeException` is raised.

## See Also

### Related Documentation
- [var objectValueOfSelectedItem: Any?](./objectvalueofselecteditem.md)
  The object corresponding to the last item selected from the pop-up list.
### Manipulating the Displayed List
- [func indexOfItem(withObjectValue: Any) -> Int](./indexofitem%28withobjectvalue%29.md)
  Searches the combo box’s internal item list for the given object and returns the matching index number.
- [func noteNumberOfItemsChanged()](./notenumberofitemschanged%28%29.md)
  Informs the combo box that the number of items in its data source has changed.
- [func reloadData()](./reloaddata%28%29.md)
  Marks the combo box as needing redisplay, so that it will reload the data for visible pop-up items and draw the new values.
- [func scrollItemAtIndexToTop(Int)](./scrollitematindextotop%28_%29.md)
  Scrolls the combo box’s pop-up list vertically so that the item at the given index is as close to the top as possible.
- [func scrollItemAtIndexToVisible(Int)](./scrollitematindextovisible%28_%29.md)
  Scrolls the combo box’s pop-up list vertically so that the item at the given index is visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxcell/itemobjectvalue(at:))*