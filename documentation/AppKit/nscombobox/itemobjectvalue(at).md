# itemObjectValue(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the object located at the given index within the receiver’s internal item list.

**Availability**:
- macOS

## Declaration

```swift
func itemObjectValue(at index: Int) -> Any
```

```objc
- (id) itemObjectValueAtIndex:(NSInteger) index;
```

## Return Value

The object located at the specified index in the internal item list.

## Discussion

This method logs a warning if the [`usesDataSource`](./usesdatasource.md) property is [`true`](../../Swift/true.md).

## Parameters

- `index`: The index of the object to retrieve. If `index` is beyond the end of the list, an `NSRangeException` is raised.

## See Also

### Related Documentation
- [var objectValueOfSelectedItem: Any?](./objectvalueofselecteditem.md)
  The object corresponding to the last item selected from the pop-up list.
### Manipulating the Displayed List
- [func indexOfItem(withObjectValue: Any) -> Int](./indexofitem%28withobjectvalue%29.md)
  Searches the receiver’s internal item list for the specified object and returns the lowest matching index.
- [func noteNumberOfItemsChanged()](./notenumberofitemschanged%28%29.md)
  Informs the receiver that the number of items in its data source has changed.
- [func reloadData()](./reloaddata%28%29.md)
  Marks the receiver as needing redisplay, so that it will reload the data for visible pop-up items and draw the new values.
- [func scrollItemAtIndexToTop(Int)](./scrollitematindextotop%28_%29.md)
  Scrolls the receiver’s pop-up list vertically so that the item at the specified index is as close to the top as possible.
- [func scrollItemAtIndexToVisible(Int)](./scrollitematindextovisible%28_%29.md)
  Scrolls the receiver’s pop-up list vertically so that the item at the specified index is visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobox/itemobjectvalue(at:))*