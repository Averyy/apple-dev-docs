# indexOfItem(withObjectValue:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Searches the combo box’s internal item list for the given object and returns the matching index number.

**Availability**:
- macOS

## Declaration

```swift
func indexOfItem(withObjectValue object: Any) -> Int
```

```objc
- (NSInteger) indexOfItemWithObjectValue:(id) object;
```

## Return Value

The lowest index whose corresponding value is equal to `anObject`. Objects are considered equal if they have the same id or if `isEqual:` returns [`true`](../../Swift/true.md). If none of the objects in the combo box’s internal item list is equal to `anObject`, [`indexOfItem(withObjectValue:)`](./indexofitem%28withobjectvalue%29.md) returns `NSNotFound`.

## Discussion

This method logs a warning if [`usesDataSource`](./usesdatasource.md) is [`true`](../../Swift/true.md).

## Parameters

- `object`: The object for which to return the index.

## See Also

### Related Documentation
- [func selectItem(withObjectValue: Any?)](./selectitem%28withobjectvalue%29.md)
  Selects the first pop-up list item that corresponds to the specified object.
### Manipulating the Displayed List
- [func itemObjectValue(at: Int) -> Any](./itemobjectvalue%28at%29.md)
  Returns the object located at the specified location in the internal item list.
- [func noteNumberOfItemsChanged()](./notenumberofitemschanged%28%29.md)
  Informs the combo box that the number of items in its data source has changed.
- [func reloadData()](./reloaddata%28%29.md)
  Marks the combo box as needing redisplay, so that it will reload the data for visible pop-up items and draw the new values.
- [func scrollItemAtIndexToTop(Int)](./scrollitematindextotop%28_%29.md)
  Scrolls the combo box’s pop-up list vertically so that the item at the given index is as close to the top as possible.
- [func scrollItemAtIndexToVisible(Int)](./scrollitematindextovisible%28_%29.md)
  Scrolls the combo box’s pop-up list vertically so that the item at the given index is visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxcell/indexofitem(withobjectvalue:))*